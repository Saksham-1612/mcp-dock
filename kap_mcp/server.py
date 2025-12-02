from fastmcp import FastMCP
import httpx
from typing import Optional, Dict, Any
import logging

# Initialize FastMCP server
mcp = FastMCP("KaptureCRM MCP Server")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# GLOBAL CONFIGURATION
# ============================================================================

# Base URL for all KaptureCRM API endpoints
BASE_URL = "https://demokapairlines.kapturecrm.com"

# Default session cookies for authentication
class AuthTokens:
    DEFAULT_SESSION_COOKIE = "myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw"
    DEFAULT_JSESSIONID = "115BECD3B018CC05C35DC118BD5974D2"
    DEFAULT_JSESSIONRID = "3SDmlhjtZ1s2DmlhjtZ"
    DEFAULT_KSID = "a50826426bf64abe88d6d7c8f9c41b92.3SDmlhjtZ1s2DmlhjtZ"

# Create global instance
auth_tokens = AuthTokens()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

# AFTER (Updated):
def build_headers(include_ksid: bool = False, 
                  session_cookie: str = None,      # ← Changed from DEFAULT_SESSION_COOKIE to None
                  jsessionid: str = None,          # ← Changed from DEFAULT_JSESSIONID to None
                  jsessionrid: str = None,         # ← Changed from DEFAULT_JSESSIONRID to None
                  ksid: str = None) -> Dict[str, str]:  # ← Changed from DEFAULT_KSID to None
    """
    Build standard headers for KaptureCRM API requests.
    Now uses auth_tokens as fallback if values not provided.
    
    Args:
        include_ksid: Whether to include the _KSID cookie
        session_cookie: _KAPTURECRM_SESSION value (uses auth_tokens if None)
        jsessionid: JSESSIONID value (uses auth_tokens if None)
        jsessionrid: JSESSIONRID value (uses auth_tokens if None)
        ksid: _KSID value (uses auth_tokens if None)
    
    Returns:
        Dictionary of headers
    """
    # Use auth_tokens as fallback if not explicitly provided
    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID
    
    cookie_parts = [
        f"_KAPTURECRM_SESSION={session_cookie}",
        f"JSESSIONID={jsessionid}",
        f"JSESSIONRID={jsessionrid}"
    ]
    
    if include_ksid:
        cookie_parts.append(f"_KSID={ksid}")
    
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "; ".join(cookie_parts)
    }


#refresh-token
@mcp.tool()
async def refresh_session_token(
    session_cookie: str
) -> dict:
    """
    Refresh the DEFAULT_SESSION_COOKIE value in memory.
    
    Args:
        session_cookie: New _KAPTURECRM_SESSION cookie value
    
    Returns:
        dict: Response with old and new token values
    """
    old_token = auth_tokens.DEFAULT_SESSION_COOKIE
    auth_tokens.DEFAULT_SESSION_COOKIE = session_cookie
    
    logger.info(f"Session cookie refreshed: {old_token[:20]}... -> {session_cookie[:20]}...")
    
    return {
        "success": True,
        "old_token": old_token,
        "new_token": session_cookie,
        "message": "Session cookie refreshed successfully"
    }



async def make_api_request(url: str, data: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Make an API request with proper error handling and JSON parsing.
    
    Args:
        url: Full API endpoint URL
        data: Request payload
        headers: Request headers
    
    Returns:
        Response dictionary with success status and data
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=headers,
                data=data,
                timeout=30.0
            )
            response.raise_for_status()
            
            # Try to parse as JSON, but handle non-JSON responses
            response_data = {}
            response_text = response.text
            
            if response_text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response_text}
            
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response_data
            }
            
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text
        }
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        return {
            "success": False,
            "error": str(e)
        }


def extract_ids_from_error(error_text: str) -> Dict[str, Any]:
    """
    Extract ticket_id and task_id information from error messages.
    This helps in providing suggestions for recovery.
    
    Args:
        error_text: Error message text
    
    Returns:
        Dictionary with extracted information
    """
    suggestions = {
        "missing_ticket_id": "ticket_id" in error_text.lower() and "required" in error_text.lower(),
        "missing_task_id": "task_id" in error_text.lower() and "required" in error_text.lower(),
        "invalid_format": "format" in error_text.lower() or "invalid" in error_text.lower()
    }
    return suggestions


# ============================================================================
# EMPLOYEE MANAGEMENT TOOLS
# ============================================================================

@mcp.tool()
async def check_username_availability(
    username: str,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Check if a username is available in KaptureCRM system.
    
    This is a prerequisite check before creating an employee. It verifies that the
    desired username is not already taken in the system.
    
    Args:
        username: The username to check availability for (e.g., "democrmemp")
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: Response indicating if username is available
            {
                "success": true/false,
                "available": true/false,
                "message": "Username is available" or "Username already exists"
            }
    
    Example:
        check_username_availability(username="democrmemp")
    
    Note: Always call this before add_update_employee() to avoid username conflicts.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    
    url = f"{base_url}/ms/employee/api/v1/check-username-availability/{username}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"_KAPTURECRM_SESSION={session_cookie}; JSESSIONID={jsessionid}; JSESSIONRID={jsessionrid}"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()
            
            response_data = {}
            response_text = response.text
            
            if response_text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response_text}
            
            result = {
                "success": True,
                "status_code": response.status_code,
                "data": response_data,
                "available": response_data.get("available", False),
                "message": f"Username '{username}' is {'available' if response_data.get('available') else 'already taken'}"
            }
            logger.info(f"Username '{username}' availability: {result['available']}")
            return result
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to check username availability: {e.response.status_code}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text,
            "available": False,
            "message": f"Failed to check username availability for '{username}'"
        }
    except Exception as e:
        logger.error(f"Username availability check error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "available": False,
            "message": f"Error checking username '{username}'"
        }


@mcp.tool()
async def add_update_employee(
    name: str,
    email: str,
    username: str,
    password: str,
    parent_emp_id: int = 308157,
    designation_id: int = 35515,
    created_by: int = 184607,
    emp_code: str = "",
    phone: Optional[str] = None,
    address: str = "",
    photo_path: str = "",
    shift_id: str = "",
    area_code_id: str = "",
    two_factor_auth: int = 0,
    join_date: str = "2025-11-29T07:15:38.722Z",
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Add or update an employee in KaptureCRM system.
    
    This API creates a new employee or updates an existing one. When creating a new employee,
    empCode should be empty. For updates, empCode should contain the employee ID.
    
    IMPORTANT: Always call check_username_availability() BEFORE this API to ensure
    the username is not already taken.
    
    Args:
        name: Full name of the employee (e.g., "Test Employee")
        email: Valid email address (e.g., "testemployee@example.com")
               Email format will be validated
        username: Unique username for login (e.g., "democrmemp")
                  Must be checked for availability first
        password: Password for login (e.g., "Democrm@123")
        parent_emp_id: ID of the parent/manager employee (default: 308157)
        designation_id: ID of the employee's designation/role (default: 35515)
        created_by: ID of the user creating this employee (default: 184607)
        emp_code: Employee code - empty string for new employee, employee ID for update
        phone: Contact phone number (optional)
        address: Physical address of the employee
        photo_path: Path to profile picture media
        shift_id: ID of the assigned shift
        area_code_id: ID of the area/region handled by employee
        two_factor_auth: Enable/disable 2FA - 0 (disabled) or 1 (enabled)
        join_date: Employee joining date in ISO format (e.g., "2025-11-29T07:15:38.722Z")
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: Response containing employee creation/update result with employee ID
            {
                "success": true/false,
                "employee_id": 123456,
                "data": {...}
            }
    
    Example:
        add_update_employee(
            name="Test Employee",
            email="testemployee@example.com",
            username="democrmemp",
            password="Democrm@123",
            parent_emp_id=308157,
            designation_id=35515
        )
    
    Workflow:
        1. First call: check_username_availability(username)
        2. If available, call: add_update_employee(...)
        3. On success, optionally call: add_employee_to_queue(employee_id, queue_id)
    
    Note: All JSON fields are required. Use empty strings for optional text fields.
    """
    # Validate email format
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        return {
            "success": False,
            "error": "Invalid email format",
            "message": f"Email '{email}' is not in valid format"
        }

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    
    url = f"{base_url}/ms/employee/api/v1/add-update-employee"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"_KAPTURECRM_SESSION={session_cookie}; JSESSIONID={jsessionid}; JSESSIONRID={jsessionrid}"
    }
    
    payload = {
        "name": name,
        "email": email,
        "empCode": emp_code,
        "phone": phone,
        "address": address,
        "parentEmpId": parent_emp_id,
        "photoPath": photo_path,
        "designationId": designation_id,
        "shiftId": shift_id,
        "areaCodeId": area_code_id,
        "twoFactorAuth": two_factor_auth,
        "joinDate": join_date,
        "createdBy": created_by,
        "loginInfo": {
            "userName": username,
            "password": password
        }
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            
            response_data = {}
            response_text = response.text
            
            if response_text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response_text}
            
            # Extract employee ID from response
            employee_id = response_data.get("employeeId") or response_data.get("empId") or response_data.get("id")
            
            result = {
                "success": True,
                "status_code": response.status_code,
                "data": response_data,
                "employee_id": employee_id,
                "message": f"Employee '{name}' {'updated' if emp_code else 'created'} successfully"
            }
            
            logger.info(f"Employee '{name}' (username: {username}) {'updated' if emp_code else 'created'} successfully")
            return result
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to add/update employee: {e.response.status_code}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text,
            "message": f"Failed to {'update' if emp_code else 'create'} employee '{name}'",
            "suggestion": "Check if username already exists by calling check_username_availability()"
        }
    except Exception as e:
        logger.error(f"Employee add/update error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": f"Error {'updating' if emp_code else 'creating'} employee '{name}'"
        }



@mcp.tool()
async def merge_kapture_tickets(
    ticket_ids: str,
    task_ids: str,
    status: str = "P",
) -> dict:
    """
    Merge tickets and tasks in KaptureCRM system.
    
    This API endpoint merges multiple tickets and their associated tasks into a consolidated view.
    
    IMPORTANT: ticket_ids and task_ids are SEPARATE entities:
    - ticket_ids: The main ticket identifiers (e.g., "9764070979477,9764070704527")
    - task_ids: Associated task identifiers (e.g., "935905686,935901656")
    - They refer to different aspects of the same tickets but use different ID values
    
    Args:
        ticket_ids: Comma-separated TICKET IDs to merge (e.g., "9764070979477,9764070704527")
                    These are the primary ticket identifiers
        task_ids: Comma-separated TASK IDs to merge (e.g., "935905686,935901656")
                  These are the task identifiers associated with the tickets
        status: Status code for the merge operation (default: "P" for Pending)
    
    Returns:
        dict: API response containing merge operation result
    
    Example:
        merge_kapture_tickets(
            ticket_ids="9764070979477,9764070704527",
            task_ids="935905686,935901656",
            status="P"
        )
    
    Recovery: If this fails, you can try to get ticket details using other tools first.
    """
    url = f"{BASE_URL}/api/version3/ticket/merge-task"
    headers = build_headers()
    data = {
        "ticket_ids": ticket_ids,
        "task_ids": task_ids,
        "status": status
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = "Tickets and tasks merged successfully"
        logger.info(f"Merged tickets: {ticket_ids} with tasks: {task_ids}")
    else:
        result["message"] = "Failed to merge tickets and tasks"
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Merge failed for tickets: {ticket_ids}, tasks: {task_ids}")
    
    return result


@mcp.tool()
async def mark_kapture_ticket_as_junk(
    task_id: str,
    remark: str
) -> dict:
    """
    Mark tickets/tasks as junk in KaptureCRM system.
    
    This API endpoint allows you to flag one or multiple tickets as junk/spam with a remark.
    
    IMPORTANT: task_id vs ticket_id:
    - This API uses task_id parameter (NOT ticket_id)
    - task_id and ticket_id are SEPARATE but RELATED identifiers
    - They both represent the same ticket object but have different numeric values
    - Example: task_id="935920326" might correspond to ticket_id="9764072089627"
    
    Args:
        task_id: Single task ID or comma-separated task IDs to mark as junk
                 (e.g., "935920326" or "935920326,935920327,935920328")
                 Note: This is the TASK identifier, not the ticket identifier
        remark: Explanation or reason for marking as junk (e.g., "spam", "duplicate")
    
    Returns:
        dict: API response containing the junk marking operation result
    
    Example:
        mark_kapture_ticket_as_junk(
            task_id="935920326",
            remark="spam email"
        )
    
    Recovery: If task_id is not found, try searching for related tickets first.
    """
    url = f"{BASE_URL}/api/version3/ticket/junk-task"
    headers = build_headers(include_ksid=True)
    data = {
        "task_id": task_id,
        "remark": remark
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Task(s) {task_id} marked as junk successfully"
        result["remark"] = remark
        logger.info(f"Marked task {task_id} as junk")
    else:
        result["message"] = f"Failed to mark task(s) {task_id} as junk"
        result["task_id"] = task_id
        logger.error(f"Failed to mark task {task_id} as junk")
    
    return result


@mcp.tool()
async def get_kapture_ticket(
    id: str,
    data_type: str,
    cdate: str,
    fetch_action_name: str = "yes"
) -> dict:
    """
    Fetch ticket details from the KaptureCRM API.
    
    **Endpoint Used**
    GET https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail
    
    **IMPORTANT RULE FOR LLMs**
    You MUST use the exact values exactly as written below.
    Do NOT change case, do NOT convert to uppercase/lowercase, do NOT add spaces,
    do NOT shorten, and do NOT invent new values.
    Only the following exact strings are valid.
    
    **Query Parameters**
    - id → Ticket ID (string).
    - data_type → MUST be exactly one of the following values (EXACT match required):
        "history" - If nothing use this value
        "SUB_TASKS"
        "NOTES"
        "EXECUTED_ESCALATION_RULES"
        "TICKET". - USE when you need to know about basic ticket info
        "SIDE_CONVERSATIONS" 
    These values must be passed exactly as shown above.
    No other values are allowed.
    Do NOT use words like "all", "everything", "default", or any variation.
    - cdate → Created date and time in the exact format "YYYY-MM-DD HH:MM:SS".
    - fetch_action_name → Default value is the exact string "yes".
    
    **Headers Required**
    - Content-Type: application/x-www-form-urlencoded
    - Cookie: (Uses global configuration; automatically included)
    
    **Returns**
    Raw JSON response from the KaptureCRM API.
    
    Example:
        get_kapture_ticket(
            id="9764070979477",
            data_type="history",
            cdate="2025-11-29 10:30:00"
        )
    """
    url = f"{BASE_URL}/api/version3/ticket/get-ticket-detail"
    
    params = {
        "id": id,
        "data_type": data_type,
        "cdate": cdate,
        "fetch_action_name": fetch_action_name,
    }
    
    headers = build_headers()
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            
            response_data = {}
            if response.text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response.text}
            
            result = {
                "success": True,
                "status_code": response.status_code,
                "data": response_data,
                "message": f"Successfully fetched ticket details for ID: {id}"
            }
            
            logger.info(f"Fetched ticket {id} with data_type: {data_type}")
            return result
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to fetch ticket: {e.response.status_code}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text,
            "message": f"Failed to fetch ticket details for ID: {id}"
        }
    except Exception as e:
        logger.error(f"Get ticket error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": f"Error fetching ticket ID: {id}"
        }

@mcp.tool()
async def dispose_kapture_ticket(
    task_id: str,
    ticket_id: str,
    selected_folder_list: str,
    sub_status: str,
    update_folder_id: str,
    assign_to: str,
    task_detail: str
) -> dict:
    """
    Dispose/close a ticket in KaptureCRM system with folder assignment and status update.
    
    CRITICAL: This API requires BOTH task_id AND ticket_id - they are SEPARATE identifiers:
    - task_id: The task identifier (e.g., "935920326")
    - ticket_id: The ticket identifier (e.g., "9764072089627")
    - Both refer to the SAME ticket object but use DIFFERENT numeric values
    - You MUST provide BOTH values - they are NOT interchangeable
    
    Args:
        task_id: TASK ID of the ticket to dispose (e.g., "935920326")
        ticket_id: TICKET ID of the ticket to dispose (e.g., "9764072089627")
                   This is a DIFFERENT identifier for the SAME ticket object
        selected_folder_list: Single or comma-separated folder IDs (e.g., "1131562")
        sub_status: Sub-status code (e.g., "PS", "CL", "RS")
        update_folder_id: Primary folder ID (e.g., "1131562")
        assign_to: Assignment in format "ID#Name" or "QUEUE#name"
                   Examples: "217346#Himanshu" or "QUEUE#es_qu"
        task_detail: Description of disposition action
    
    Returns:
        dict: API response containing the disposition operation result
    
    Example:
        dispose_kapture_ticket(
            task_id="935920326",
            ticket_id="9764072089627",
            selected_folder_list="1131562",
            sub_status="PS",
            update_folder_id="1131562",
            assign_to="217346#Himanshu",
            task_detail="Resolved customer issue"
        )
    
    Recovery: If either ID is missing or invalid, use other tools to retrieve the correct IDs.
    """
    url = f"{BASE_URL}/api/version3/ticket/dispose-task"
    headers = build_headers(include_ksid=True, ksid="5694f03d820742968a319751ec3738ac.3SDmlhjtZ1s2DmlhjtZ")
    data = {
        "task_id": task_id,
        "ticket_id": ticket_id,
        "selected_folder_list": selected_folder_list,
        "sub_status": sub_status,
        "update_folder_id": update_folder_id,
        "assign_to": assign_to,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket {ticket_id} (Task: {task_id}) disposed successfully"
        result["disposition_details"] = {
            "ticket_id": ticket_id,
            "task_id": task_id,
            "assigned_to": assign_to,
            "sub_status": sub_status,
            "folders": selected_folder_list,
            "detail": task_detail
        }
        logger.info(f"Disposed ticket {ticket_id} (task: {task_id})")
    else:
        result["message"] = f"Failed to dispose ticket {ticket_id} (Task: {task_id})"
        result["ticket_id"] = ticket_id
        result["task_id"] = task_id
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Failed to dispose ticket {ticket_id} (task: {task_id})")
    
    return result


@mcp.tool()
async def assign_kapture_ticket(
    ticket_id: str,
    task_id: str,
    assign_to: str,
    task_detail: str
) -> dict:
    """
    Assign a ticket to an employee in KaptureCRM system.
    
    CRITICAL: This API requires BOTH ticket_id AND task_id - they are SEPARATE identifiers:
    - ticket_id: The ticket identifier (e.g., "9764070704527")
    - task_id: The task identifier (e.g., "935901656")
    - Both refer to the SAME ticket object but use DIFFERENT numeric values
    - You MUST provide BOTH values - they are NOT interchangeable
    
    Args:
        ticket_id: TICKET ID to assign (e.g., "9764070704527")
        task_id: TASK ID to assign (e.g., "935901656")
                 This is a DIFFERENT identifier for the SAME ticket object
        assign_to: Employee assignment in format "EmployeeID#EmployeeName"
                   Example: "217346#Himanshu"
        task_detail: Description of assignment action
    
    Returns:
        dict: API response containing the assignment operation result
    
    Example:
        assign_kapture_ticket(
            ticket_id="9764070704527",
            task_id="935901656",
            assign_to="217346#Himanshu",
            task_detail="Assigning for follow-up"
        )
    
    Recovery: If either ID is missing, use other tools to find the correct ticket and task IDs.
    """
    url = f"{BASE_URL}/api/version3/ticket/task-assignment"
    headers = build_headers()
    data = {
        "ticket_id": ticket_id,
        "task_id": task_id,
        "assign_to": assign_to,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket {ticket_id} (Task: {task_id}) assigned successfully to {assign_to}"
        result["assignment_details"] = {
            "ticket_id": ticket_id,
            "task_id": task_id,
            "assigned_to": assign_to,
            "detail": task_detail
        }
        logger.info(f"Assigned ticket {ticket_id} (task: {task_id}) to {assign_to}")
    else:
        result["message"] = f"Failed to assign ticket {ticket_id} (Task: {task_id})"
        result["ticket_id"] = ticket_id
        result["task_id"] = task_id
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Failed to assign ticket {ticket_id} (task: {task_id})")
    
    return result


@mcp.tool()
async def resolve_kapture_tickets(
    task_id: str,
    task_detail: str,
    sub_status: str = "RS"
) -> dict:
    """
    Resolve tickets in KaptureCRM system with a specific status.
    
    IMPORTANT: task_id vs ticket_id:
    - This API uses task_id parameter (NOT ticket_id)
    - task_id and ticket_id are SEPARATE but RELATED identifiers
    - They both represent the same ticket object but have different numeric values
    - Example: task_id="935920326" might correspond to ticket_id="9764072089627"
    
    Args:
        task_id: Single task ID or comma-separated task IDs to resolve
                 (e.g., "935920326" or "935920326,935919331")
                 Note: This is the TASK identifier, not the ticket identifier
        task_detail: Description of resolution action
        sub_status: Sub-status code (default: "RS")
                    - "RS" = Resolved
                    - "P" = Pending
    
    Returns:
        dict: API response containing the resolution operation result
    
    Example:
        resolve_kapture_tickets(
            task_id="935920326",
            task_detail="Issue resolved by restarting server",
            sub_status="RS"
        )
    
    Recovery: If task_id is invalid, try reopening the ticket first or checking its status.
    """
    url = f"{BASE_URL}/api/version3/ticket/task-resolve"
    headers = build_headers()
    data = {
        "task_id": task_id,
        "task_detail": task_detail,
        "sub_status": sub_status
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket(s) {task_id} resolved successfully with status {sub_status}"
        result["resolution_details"] = {
            "task_id": task_id,
            "sub_status": sub_status,
            "detail": task_detail
        }
        logger.info(f"Resolved task {task_id} with status {sub_status}")
    else:
        result["message"] = f"Failed to resolve ticket(s) {task_id}"
        result["task_id"] = task_id
        logger.error(f"Failed to resolve task {task_id}")
    
    return result


@mcp.tool()
async def reopen_kapture_tickets(
    task_ids: str,
    task_detail: str
) -> dict:
    """
    Reopen closed or disposed tickets in KaptureCRM system.
    
    IMPORTANT: task_ids vs ticket_ids:
    - This API uses task_ids parameter (NOT ticket_ids) - note the plural
    - task_ids and ticket_ids are SEPARATE but RELATED identifiers
    - They both represent the same ticket objects but have different numeric values
    - Example: task_ids="935920326" might correspond to ticket_id="9764072089627"
    
    Args:
        task_ids: Single task ID or comma-separated task IDs to reopen
                  (e.g., "935920326" or "935920326,935919331,935905686")
                  Note: This is the TASK identifier, not the ticket identifier
        task_detail: Description of why reopening
    
    Returns:
        dict: API response containing the reopen operation result
    
    Example:
        reopen_kapture_tickets(
            task_ids="935920326,935919331",
            task_detail="Customer reported issue not resolved"
        )
    
    Recovery: If reopening fails, try resolving or assigning the ticket instead.
    """
    url = f"{BASE_URL}/api/version3/ticket/reopen-task"
    headers = build_headers()
    data = {
        "task_ids": task_ids,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket(s) {task_ids} reopened successfully"
        result["reopen_details"] = {
            "task_ids": task_ids,
            "detail": task_detail
        }
        logger.info(f"Reopened tasks {task_ids}")
    else:
        result["message"] = f"Failed to reopen ticket(s) {task_ids}"
        result["task_ids"] = task_ids
        logger.error(f"Failed to reopen tasks {task_ids}")
    
    return result


@mcp.tool()
async def get_queues(
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Get all queues with their configurations in KaptureCRM system.
    
    This API retrieves all ticket queues including their names, routing types,
    assignment orders, and current employee assignments. This information is needed
    before adding an employee to a queue.
    
    Args:
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: Response containing list of all queues with their details
            {
                "success": true/false,
                "queues": [
                    {
                        "queueId": 17396,
                        "queueName": "Escalated queue",
                        "routingType": "Round Robin",
                        "assignmentOrder": "Follow-Up First",
                        "stickyKeyMode": false,
                        "employeeIds": [184607, 308157]
                    },
                    ...
                ]
            }
    
    Example:
        get_queues()
    
    Use Case:
        Call this to get existing queue details before updating a queue with
        a new employee. The response contains the current employeeIds array
        which you'll need to append the new employee ID to.
    
    Note: This is called automatically by add_employee_to_queue() composite tool.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID

    url = f"{base_url}/ms/ticket-configuration/queue"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"_KAPTURECRM_SESSION={session_cookie}; JSESSIONID={jsessionid}; JSESSIONRID={jsessionrid}"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()
            
            response_data = {}
            response_text = response.text
            
            if response_text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response_text}
            
            result = {
                "success": True,
                "status_code": response.status_code,
                "data": response_data,
                "queues": response_data if isinstance(response_data, list) else response_data.get("queues", []),
                "message": "Successfully retrieved queues"
            }
            
            logger.info(f"Retrieved {len(result['queues'])} queues")
            return result
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to get queues: {e.response.status_code}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text,
            "message": "Failed to retrieve queues"
        }
    except Exception as e:
        logger.error(f"Get queues error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Error retrieving queues"
        }


@mcp.tool()
async def update_queue(
    queue_id: int,
    queue_name: str,
    routing_type: str,
    assignment_order: str,
    employee_ids: list,
    sticky_key_mode: bool = False,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Update a queue configuration in KaptureCRM system.
    
    This API updates an existing queue's configuration including adding/removing employees.
    
    IMPORTANT: employee_ids should contain ALL employee IDs (existing + new ones).
    To add a new employee to a queue:
    1. Call get_queues() to get current employee_ids
    2. Append new employee_id to the list
    3. Call update_queue() with the complete list
    
    Args:
        queue_id: ID of the queue to update (e.g., 17396)
        queue_name: Name of the queue (e.g., "Escalated queue")
        routing_type: Type of routing for the queue
                      Examples: "Round Robin", "Load Balancing", "Skill Based"
        assignment_order: Order in which tickets are assigned
                          Examples: "Follow-Up First", "FIFO", "Priority Based"
        employee_ids: Complete list of employee IDs in this queue (e.g., [184607, 308157, 123456])
                      This should include BOTH existing and newly added employee IDs
        sticky_key_mode: Enable/disable sticky mode - true or false (default: false)
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: Response containing queue update result
            {
                "success": true/false,
                "queue_id": 17396,
                "message": "Queue updated successfully"
            }
    
    Example:
        update_queue(
            queue_id=17396,
            queue_name="Escalated queue",
            routing_type="Round Robin",
            assignment_order="Follow-Up First",
            employee_ids=[184607, 308157, 123456],
            sticky_key_mode=False
        )
    
    Note: Don't call this directly to add employees. Use add_employee_to_queue() instead.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID

    url = f"{base_url}/ms/ticket-configuration/queue/{queue_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"_KAPTURECRM_SESSION={session_cookie}; JSESSIONID={jsessionid}; JSESSIONRID={jsessionrid}"
    }
    
    payload = {
        "queueName": queue_name,
        "routingType": routing_type,
        "assignmentOrder": assignment_order,
        "stickyKeyMode": sticky_key_mode,
        "employeeIds": employee_ids
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url,
                headers=headers,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            
            response_data = {}
            response_text = response.text
            
            if response_text:
                try:
                    response_data = response.json()
                except Exception:
                    response_data = {"response_text": response_text}
            
            result = {
                "success": True,
                "status_code": response.status_code,
                "data": response_data,
                "queue_id": queue_id,
                "employee_ids": employee_ids,
                "message": f"Queue '{queue_name}' (ID: {queue_id}) updated successfully"
            }
            
            logger.info(f"Updated queue {queue_id} with {len(employee_ids)} employees")
            return result
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to update queue: {e.response.status_code}")
        return {
            "success": False,
            "status_code": e.response.status_code,
            "error": str(e),
            "response_text": e.response.text,
            "queue_id": queue_id,
            "message": f"Failed to update queue '{queue_name}' (ID: {queue_id})"
        }
    except Exception as e:
        logger.error(f"Update queue error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "queue_id": queue_id,
            "message": f"Error updating queue '{queue_name}' (ID: {queue_id})"
        }


# ============================================================================
# COMPOSITE WORKFLOW TOOL
# ============================================================================

@mcp.tool()
async def create_employee_and_add_to_queue(
    name: str,
    email: str,
    username: str,
    password: str,
    queue_id: int,
    parent_emp_id: int = 308157,
    designation_id: int = 35515,
    created_by: int = 184607,
    emp_code: str = "",
    phone: Optional[str] = None,
    address: str = "",
    photo_path: str = "",
    shift_id: str = "",
    area_code_id: str = "",
    two_factor_auth: int = 0,
    join_date: str = "2025-11-29T07:15:38.722Z",
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Complete workflow to create an employee and add them to a queue.
    
    This composite tool orchestrates the entire employee creation workflow:
    1. check_username_availability() - Verify username is available
    2. add_update_employee() - Create the employee
    3. get_queues() - Get current queue configuration
    4. update_queue() - Add employee to the specified queue
    
    Each step can be performed individually if needed for custom workflows.
    
    Args:
        name: Full name of the employee (e.g., "Test Employee")
        email: Valid email address (e.g., "testemployee@example.com")
        username: Unique username for login (e.g., "democrmemp")
        password: Password for login (e.g., "Democrm@123")
        queue_id: ID of the queue to add employee to (e.g., 17396)
        parent_emp_id: ID of the parent/manager employee (default: 308157)
        designation_id: ID of the employee's designation/role (default: 35515)
        created_by: ID of the user creating this employee (default: 184607)
        emp_code: Employee code - leave empty for new employee
        phone: Contact phone number (optional)
        address: Physical address of the employee
        photo_path: Path to profile picture media
        shift_id: ID of the assigned shift
        area_code_id: ID of the area/region handled by employee
        two_factor_auth: Enable/disable 2FA - 0 (disabled) or 1 (enabled)
        join_date: Employee joining date in ISO format
        base_url: KaptureCRM base URL
    
    Returns:
        dict: Detailed response with results from each step
            {
                "success": true/false,
                "employee_id": 123456,
                "queue_id": 17396,
                "workflow_steps": [
                    {"step": "check_username", "success": true, ...},
                    {"step": "create_employee", "success": true, ...},
                    {"step": "get_queues", "success": true, ...},
                    {"step": "update_queue", "success": true, ...}
                ],
                "message": "Employee created and added to queue successfully"
            }
    
    Example:
        create_employee_and_add_to_queue(
            name="Test Employee",
            email="testemployee@example.com",
            username="democrmemp",
            password="Democrm@123",
            queue_id=17396
        )
    
    Error Handling:
        - If username is taken, workflow stops at step 1
        - If employee creation fails, workflow stops at step 2
        - If queue retrieval fails, workflow stops at step 3
        - Each step's result is included in the response for debugging
    
    Individual Tools:
        You can call these separately for custom workflows:
        - check_username_availability(username)
        - add_update_employee(name, email, username, password, ...)
        - get_queues()
        - update_queue(queue_id, queue_name, routing_type, ...)
    """
    workflow_results = {
        "success": False,
        "workflow_steps": [],
        "employee_id": None,
        "queue_id": queue_id
    }
    
    # Step 1: Check username availability
    logger.info(f"Step 1: Checking username availability for '{username}'")
    username_check = await check_username_availability(username, base_url)
    workflow_results["workflow_steps"].append({
        "step": "check_username_availability",
        "success": username_check["success"],
        "available": username_check.get("available", False),
        "data": username_check
    })
    
    if not username_check["success"] or not username_check.get("available", False):
        workflow_results["message"] = f"Username '{username}' is not available"
        workflow_results["suggestion"] = "Try a different username and call create_employee_and_add_to_queue() again"
        logger.warning(f"Workflow stopped: Username '{username}' not available")
        return workflow_results
    
    # Step 2: Create employee
    logger.info(f"Step 2: Creating employee '{name}'")
    employee_result = await add_update_employee(
        name=name,
        email=email,
        username=username,
        password=password,
        parent_emp_id=parent_emp_id,
        designation_id=designation_id,
        created_by=created_by,
        emp_code=emp_code,
        phone=phone,
        address=address,
        photo_path=photo_path,
        shift_id=shift_id,
        area_code_id=area_code_id,
        two_factor_auth=two_factor_auth,
        join_date=join_date,
        base_url=base_url
    )
    
    workflow_results["workflow_steps"].append({
        "step": "add_update_employee",
        "success": employee_result["success"],
        "employee_id": employee_result.get("employee_id"),
        "data": employee_result
    })
    
    if not employee_result["success"]:
        workflow_results["message"] = f"Failed to create employee '{name}'"
        workflow_results["suggestion"] = "Check employee details and call add_update_employee() directly to debug"
        logger.error(f"Workflow stopped: Failed to create employee '{name}'")
        return workflow_results
    
    employee_id = employee_result.get("employee_id")
    workflow_results["employee_id"] = employee_id
    
    if not employee_id:
        workflow_results["message"] = "Employee created but ID not returned in response"
        workflow_results["suggestion"] = "Check the employee list to find the new employee ID"
        logger.warning("Employee created but ID not found in response")
        return workflow_results
    
    # Step 3: Get queues to find target queue details
    logger.info(f"Step 3: Getting queue details for queue_id={queue_id}")
    queues_result = await get_queues(base_url)
    workflow_results["workflow_steps"].append({
        "step": "get_queues",
        "success": queues_result["success"],
        "data": queues_result
    })
    
    if not queues_result["success"]:
        workflow_results["message"] = f"Employee created (ID: {employee_id}) but failed to get queues"
        workflow_results["suggestion"] = f"Manually add employee {employee_id} to queue {queue_id} using update_queue()"
        logger.error(f"Workflow stopped: Failed to get queues")
        return workflow_results
    
    # Find the target queue
    target_queue = None
    for queue in queues_result.get("queues", []):
        if queue.get("queueId") == queue_id or queue.get("id") == queue_id:
            target_queue = queue
            break
    
    if not target_queue:
        workflow_results["message"] = f"Employee created (ID: {employee_id}) but queue {queue_id} not found"
        workflow_results["suggestion"] = f"Check if queue_id {queue_id} is correct. Call get_queues() to see available queues"
        logger.error(f"Workflow stopped: Queue {queue_id} not found")
        return workflow_results
    
    # Step 4: Update queue with new employee
    logger.info(f"Step 4: Adding employee {employee_id} to queue {queue_id}")
    current_employee_ids = target_queue.get("employeeIds", [])
    updated_employee_ids = current_employee_ids + [employee_id]
    
    queue_update_result = await update_queue(
        queue_id=queue_id,
        queue_name=target_queue.get("queueName", ""),
        routing_type=target_queue.get("routingType", "Round Robin"),
        assignment_order=target_queue.get("assignmentOrder", "Follow-Up First"),
        employee_ids=updated_employee_ids,
        sticky_key_mode=target_queue.get("stickyKeyMode", False),
        base_url=base_url
    )
    
    workflow_results["workflow_steps"].append({
        "step": "update_queue",
        "success": queue_update_result["success"],
        "queue_id": queue_id,
        "employee_ids": updated_employee_ids,
        "data": queue_update_result
    })
    
    if not queue_update_result["success"]:
        workflow_results["message"] = f"Employee created (ID: {employee_id}) but failed to add to queue {queue_id}"
        workflow_results["suggestion"] = f"Manually call update_queue() to add employee {employee_id} to queue {queue_id}"
        logger.error(f"Workflow stopped: Failed to update queue {queue_id}")
        return workflow_results
    
    # Success!
    workflow_results["success"] = True
    workflow_results["message"] = f"Employee '{name}' (ID: {employee_id}) created and added to queue {queue_id} successfully"
    logger.info(f"Workflow completed successfully: Employee {employee_id} added to queue {queue_id}")
    
    return workflow_results


# ============================================================================
# TOOL IMPLEMENTATIONS
# ============================================================================

@mcp.tool()
async def merge_kapture_tickets(
    ticket_ids: str,
    task_ids: str,
    status: str = "P",
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Merge tickets and tasks in KaptureCRM system.
    
    This API endpoint merges multiple tickets and their associated tasks into a consolidated view.
    
    IMPORTANT: ticket_ids and task_ids are SEPARATE entities:
    - ticket_ids: The main ticket identifiers (e.g., "9764070979477,9764070704527")
    - task_ids: Associated task identifiers (e.g., "935905686,935901656")
    - They refer to different aspects of the same tickets but use different ID values
    
    Args:
        ticket_ids: Comma-separated TICKET IDs to merge (e.g., "9764070979477,9764070704527")
                    These are the primary ticket identifiers
        task_ids: Comma-separated TASK IDs to merge (e.g., "935905686,935901656")
                  These are the task identifiers associated with the tickets
        status: Status code for the merge operation (default: "P" for Pending)
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value for authentication
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: API response containing merge operation result
    
    Example:
        merge_kapture_tickets(
            ticket_ids="9764070979477,9764070704527",
            task_ids="935905686,935901656",
            status="P"
        )
    
    Recovery: If this fails, you can try to get ticket details using other tools first.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    
    url = f"{base_url}/api/version3/ticket/merge-task"
    headers = build_headers(session_cookie=session_cookie, jsessionid=jsessionid, jsessionrid=jsessionrid)
    data = {
        "ticket_ids": ticket_ids,
        "task_ids": task_ids,
        "status": status
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = "Tickets and tasks merged successfully"
        logger.info(f"Merged tickets: {ticket_ids} with tasks: {task_ids}")
    else:
        result["message"] = "Failed to merge tickets and tasks"
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Merge failed for tickets: {ticket_ids}, tasks: {task_ids}")
    
    return result


@mcp.tool()
async def mark_kapture_ticket_as_junk(
    task_id: str,
    remark: str,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Mark tickets/tasks as junk in KaptureCRM system.
    
    This API endpoint allows you to flag one or multiple tickets as junk/spam with a remark.
    
    IMPORTANT: task_id vs ticket_id:
    - This API uses task_id parameter (NOT ticket_id)
    - task_id and ticket_id are SEPARATE but RELATED identifiers
    - They both represent the same ticket object but have different numeric values
    - Example: task_id="935920326" might correspond to ticket_id="9764072089627"
    
    Args:
        task_id: Single task ID or comma-separated task IDs to mark as junk
                 (e.g., "935920326" or "935920326,935920327,935920328")
                 Note: This is the TASK identifier, not the ticket identifier
        remark: Explanation or reason for marking as junk (e.g., "spam", "duplicate")
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
        ksid: _KSID cookie value
    
    Returns:
        dict: API response containing the junk marking operation result
    
    Example:
        mark_kapture_ticket_as_junk(
            task_id="935920326",
            remark="spam email"
        )
    
    Recovery: If task_id is not found, try searching for related tickets first.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID
    
    url = f"{base_url}/api/version3/ticket/junk-task"
    headers = build_headers(include_ksid=True, session_cookie=session_cookie, 
                           jsessionid=jsessionid, jsessionrid=jsessionrid, ksid=ksid)
    data = {
        "task_id": task_id,
        "remark": remark
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Task(s) {task_id} marked as junk successfully"
        result["remark"] = remark
        logger.info(f"Marked task {task_id} as junk")
    else:
        result["message"] = f"Failed to mark task(s) {task_id} as junk"
        result["task_id"] = task_id
        logger.error(f"Failed to mark task {task_id} as junk")
    
    return result


@mcp.tool()
async def dispose_kapture_ticket(
    task_id: str,
    ticket_id: str,
    selected_folder_list: str,
    sub_status: str,
    update_folder_id: str,
    assign_to: str,
    task_detail: str,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Dispose/close a ticket in KaptureCRM system with folder assignment and status update.
    
    CRITICAL: This API requires BOTH task_id AND ticket_id - they are SEPARATE identifiers:
    - task_id: The task identifier (e.g., "935920326")
    - ticket_id: The ticket identifier (e.g., "9764072089627")
    - Both refer to the SAME ticket object but use DIFFERENT numeric values
    - You MUST provide BOTH values - they are NOT interchangeable
    
    Args:
        task_id: TASK ID of the ticket to dispose (e.g., "935920326")
        ticket_id: TICKET ID of the ticket to dispose (e.g., "9764072089627")
                   This is a DIFFERENT identifier for the SAME ticket object
        selected_folder_list: Single or comma-separated folder IDs (e.g., "1131562")
        sub_status: Sub-status code (e.g., "PS", "CL", "RS")
        update_folder_id: Primary folder ID (e.g., "1131562")
        assign_to: Assignment in format "ID#Name" or "QUEUE#name"
                   Examples: "217346#Himanshu" or "QUEUE#es_qu"
        task_detail: Description of disposition action
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
        ksid: _KSID cookie value
    
    Returns:
        dict: API response containing the disposition operation result
    
    Example:
        dispose_kapture_ticket(
            task_id="935920326",
            ticket_id="9764072089627",
            selected_folder_list="1131562",
            sub_status="PS",
            update_folder_id="1131562",
            assign_to="217346#Himanshu",
            task_detail="Resolved customer issue"
        )
    
    Recovery: If either ID is missing or invalid, use other tools to retrieve the correct IDs.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID
    
    url = f"{base_url}/api/version3/ticket/dispose-task"
    headers = build_headers(include_ksid=True, session_cookie=session_cookie,
                           jsessionid=jsessionid, jsessionrid=jsessionrid, ksid=ksid)
    data = {
        "task_id": task_id,
        "ticket_id": ticket_id,
        "selected_folder_list": selected_folder_list,
        "sub_status": sub_status,
        "update_folder_id": update_folder_id,
        "assign_to": assign_to,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket {ticket_id} (Task: {task_id}) disposed successfully"
        result["disposition_details"] = {
            "ticket_id": ticket_id,
            "task_id": task_id,
            "assigned_to": assign_to,
            "sub_status": sub_status,
            "folders": selected_folder_list,
            "detail": task_detail
        }
        logger.info(f"Disposed ticket {ticket_id} (task: {task_id})")
    else:
        result["message"] = f"Failed to dispose ticket {ticket_id} (Task: {task_id})"
        result["ticket_id"] = ticket_id
        result["task_id"] = task_id
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Failed to dispose ticket {ticket_id} (task: {task_id})")
    
    return result


@mcp.tool()
async def assign_kapture_ticket(
    ticket_id: str,
    task_id: str,
    assign_to: str,
    task_detail: str,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Assign a ticket to an employee in KaptureCRM system.
    
    CRITICAL: This API requires BOTH ticket_id AND task_id - they are SEPARATE identifiers:
    - ticket_id: The ticket identifier (e.g., "9764070704527")
    - task_id: The task identifier (e.g., "935901656")
    - Both refer to the SAME ticket object but use DIFFERENT numeric values
    - You MUST provide BOTH values - they are NOT interchangeable
    
    Args:
        ticket_id: TICKET ID to assign (e.g., "9764070704527")
        task_id: TASK ID to assign (e.g., "935901656")
                 This is a DIFFERENT identifier for the SAME ticket object
        assign_to: Employee assignment in format "EmployeeID#EmployeeName"
                   Example: "217346#Himanshu"
        task_detail: Description of assignment action
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: API response containing the assignment operation result
    
    Example:
        assign_kapture_ticket(
            ticket_id="9764070704527",
            task_id="935901656",
            assign_to="217346#Himanshu",
            task_detail="Assigning for follow-up"
        )
    
    Recovery: If either ID is missing, use other tools to find the correct ticket and task IDs.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    
    url = f"{base_url}/api/version3/ticket/task-assignment"
    headers = build_headers(session_cookie=session_cookie, jsessionid=jsessionid, jsessionrid=jsessionrid)
    data = {
        "ticket_id": ticket_id,
        "task_id": task_id,
        "assign_to": assign_to,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket {ticket_id} (Task: {task_id}) assigned successfully to {assign_to}"
        result["assignment_details"] = {
            "ticket_id": ticket_id,
            "task_id": task_id,
            "assigned_to": assign_to,
            "detail": task_detail
        }
        logger.info(f"Assigned ticket {ticket_id} (task: {task_id}) to {assign_to}")
    else:
        result["message"] = f"Failed to assign ticket {ticket_id} (Task: {task_id})"
        result["ticket_id"] = ticket_id
        result["task_id"] = task_id
        suggestions = extract_ids_from_error(result.get("response_text", ""))
        result["suggestions"] = suggestions
        logger.error(f"Failed to assign ticket {ticket_id} (task: {task_id})")
    
    return result


@mcp.tool()
async def resolve_kapture_tickets(
    task_id: str,
    task_detail: str,
    sub_status: str = "RS",
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Resolve tickets in KaptureCRM system with a specific status.
    
    IMPORTANT: task_id vs ticket_id:
    - This API uses task_id parameter (NOT ticket_id)
    - task_id and ticket_id are SEPARATE but RELATED identifiers
    - They both represent the same ticket object but have different numeric values
    - Example: task_id="935920326" might correspond to ticket_id="9764072089627"
    
    Args:
        task_id: Single task ID or comma-separated task IDs to resolve
                 (e.g., "935920326" or "935920326,935919331")
                 Note: This is the TASK identifier, not the ticket identifier
        task_detail: Description of resolution action
        sub_status: Sub-status code (default: "RS")
                    - "RS" = Resolved
                    - "P" = Pending
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
        ksid: _KSID cookie value
    
    Returns:
        dict: API response containing the resolution operation result
    
    Example:
        resolve_kapture_tickets(
            task_id="935920326",
            task_detail="Issue resolved by restarting server",
            sub_status="RS"
        )
    
    Recovery: If task_id is invalid, try reopening the ticket first or checking its status.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID
    
    url = f"{base_url}/api/version3/ticket/task-resolve"
    headers = build_headers(include_ksid=True, session_cookie=session_cookie,
                           jsessionid=jsessionid, jsessionrid=jsessionrid, ksid=ksid)
    data = {
        "task_id": task_id,
        "task_detail": task_detail,
        "sub_status": sub_status
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket(s) {task_id} resolved successfully with status {sub_status}"
        result["resolution_details"] = {
            "task_id": task_id,
            "sub_status": sub_status,
            "detail": task_detail
        }
        logger.info(f"Resolved task {task_id} with status {sub_status}")
    else:
        result["message"] = f"Failed to resolve ticket(s) {task_id}"
        result["task_id"] = task_id
        logger.error(f"Failed to resolve task {task_id}")
    
    return result


@mcp.tool()
async def reopen_kapture_tickets(
    task_ids: str,
    task_detail: str,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Reopen closed or disposed tickets in KaptureCRM system.
    
    IMPORTANT: task_ids vs ticket_ids:
    - This API uses task_ids parameter (NOT ticket_ids) - note the plural
    - task_ids and ticket_ids are SEPARATE but RELATED identifiers
    - They both represent the same ticket objects but have different numeric values
    - Example: task_ids="935920326" might correspond to ticket_id="9764072089627"
    - x-www-form-urlencoded format requires task_ids as comma-separated string and everything goes in that only not in

    Args:
        task_ids: Single task ID or comma-separated task IDs to reopen
                  (e.g., "935920326" or "935920326,935919331,935905686")
                  Note: This is the TASK identifier, not the ticket identifier
        task_detail: Description of why reopening
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
        ksid: _KSID cookie value
    
    Returns:
        dict: API response containing the reopen operation result
    
    Example:
        reopen_kapture_tickets(
            task_ids="935920326,935919331",
            task_detail="Customer reported issue not resolved"
        )
    
    Recovery: If reopening fails, try resolving or assigning the ticket instead.
    """

    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID
    
    url = f"{base_url}/api/version3/ticket/reopen-task"
    headers = build_headers(include_ksid=True, session_cookie=session_cookie,
                           jsessionid=jsessionid, jsessionrid=jsessionrid, ksid=ksid)
    data = {
        "task_ids": task_ids,
        "task_detail": task_detail
    }
    
    result = await make_api_request(url, data, headers)
    
    if result["success"]:
        result["message"] = f"Ticket(s) {task_ids} reopened successfully"
        result["reopen_details"] = {
            "task_ids": task_ids,
            "detail": task_detail
        }
        logger.info(f"Reopened tasks {task_ids}")
    else:
        result["message"] = f"Failed to reopen ticket(s) {task_ids}"
        result["task_ids"] = task_ids
        logger.error(f"Failed to reopen tasks {task_ids}")
    
    return result



@mcp.tool()
async def search_kapture_employees(
    search_value: str = "",
    offset: int = 0,
    page_size: int = 10,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """Search and retrieve employees from KaptureCRM system.
    
    This API searches for employees based on a search value and returns paginated results.
    You can search by employee name, email, username, or other employee attributes.
    
    **Endpoint Used**
    POST https://demokapairlines.kapturecrm.com/ms/employee/api/v1/employee-search
    
    **Search Functionality**
    - Pass an empty string "" in search_value to retrieve all employees (paginated)
    - Pass a specific name, email, or username to filter results
    - Results are paginated using offset and page_size parameters
    
    Args:
        search_value: Employee search term (name, email, username, etc.)
                     Use empty string "" to retrieve all employees
                     Examples: "John Doe", "john@example.com", "johndoe123"
        offset: Starting position for pagination (default: 0)
                Example: offset=0 gets first page, offset=10 gets second page
        page_size: Number of records per page (default: 10)
                   Example: page_size=10 returns 10 employees per request
        base_url: KaptureCRM base URL
        session_cookie: _KAPTURECRM_SESSION cookie value
        jsessionid: JSESSIONID cookie value
        jsessionrid: JSESSIONRID cookie value
    
    Returns:
        dict: API response containing employee search results
            {
                "success": true/false,
                "employees": [...],
                "totalCount": 100,
                "offset": 0,
                "pageSize": 10
            }
    
    Example:
        # Search for all employees
        search_kapture_employees(search_value="")
        
        # Search for specific employee
        search_kapture_employees(search_value="John Doe")
        
        # Get second page of results
        search_kapture_employees(search_value="", offset=10, page_size=10)
    
    Use Cases:
        - Finding an employee by name before assigning tickets
        - Listing all available employees in a team
        - Searching for employees by email or username
        - Paginating through large employee lists
    
    Note: search_value is mandatory - always pass it even if empty string.
    """
    # Use default auth tokens if not provided
    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    
    # Construct the API endpoint
    url = f"{base_url}/ms/employee/api/v1/employee-search"
    
    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"_KAPTURECRM_SESSION={session_cookie}; JSESSIONID={jsessionid}; JSESSIONRID={jsessionrid}"
    }
    
    # Prepare request payload
    payload = {
        "offset": offset,
        "pageSize": page_size,
        "searchValue": search_value
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to search employees in KaptureCRM"
        }

@mcp.tool()
async def get_kapture_employee_by_id(
    employee_id: str = None,
    employee_name: str = None,
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None
) -> dict:
    """
    Retrieve detailed employee information from the KaptureCRM system.

    This API fetches a specific employee's complete details using the employee ID.
    It supports multiple access patterns:
    
    1. **Direct ID Lookup (Recommended)**
       - If `employee_id` is provided, the tool directly calls the
         `get-employee-by-employeeid/{employeeId}` endpoint.
       
    2. **Name-based Lookup (Flexible)**
       - If `employee_name` is provided and `employee_id` is not:
         - The tool internally calls `search_kapture_employees(search_value=employee_name)`
         - Extracts the most relevant employee result
         - Uses its ID to call the current API
         
       This is useful when the user only knows the employee name.

    ------------------------------------------------------------------

    **Endpoint Used**
    GET https://demokapairlines.kapturecrm.com/ms/employee/api/v1/get-employee-by-employeeid/{employeeId}

    **Input Modes**
    - Provide `employee_id` directly  
      → Fastest and most accurate  
    - Provide `employee_name`  
      → Tool will search and resolve to an ID automatically

    ------------------------------------------------------------------

    Args:
        employee_id: Employee ID to look up.
                     Example: "308263"
                     If provided, name-based search is skipped.

        employee_name: Name of employee to search for.
                       Example: "John Doe"
                       Used only if `employee_id` is not provided.

        base_url: KaptureCRM base URL.

        session_cookie: _KAPTURECRM_SESSION cookie value.
        jsessionid:     JSESSIONID cookie value.
        jsessionrid:    JSESSIONRID cookie value.

    ------------------------------------------------------------------

    Returns:
        dict: Employee details returned by the KaptureCRM API.
              Example:
              {
                  "success": true,
                  "employee": { ... },
                  "message": "...",
              }

    ------------------------------------------------------------------

    Example:
        # Direct lookup by ID
        get_kapture_employee_by_id(employee_id="308263")

        # Name-based lookup (ID resolved automatically)
        get_kapture_employee_by_id(employee_name="John Doe")

        # If both are passed, employee_id takes priority
        get_kapture_employee_by_id(employee_id="308263", employee_name="John")

    ------------------------------------------------------------------

    Use Cases:
        - Retrieve detailed employee info after searching employees
        - Validate employee existence before ticket assignment
        - Fetch employee details using either name or ID
        - Automatically resolve names → IDs → details in one tool call

    ------------------------------------------------------------------

    Notes:
        - If employee_name is used, the tool will internally call:
              search_kapture_employees(search_value=employee_name)
        - Do not change any quoted values.
        - Session tokens follow the same pattern as the previous tool.
    """

    # Use default auth tokens if not provided (same pattern as previous tool)
    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID

    # If employee_id is NOT provided but employee_name is
    if not employee_id and employee_name:
        try:
            # Search employees by name
            search_result = await search_kapture_employees(
                search_value=employee_name,
                session_cookie=session_cookie,
                jsessionid=jsessionid,
                jsessionrid=jsessionrid
            )

            if (
                search_result.get("success") is False
                or "employees" not in search_result
                or len(search_result.get("employees", [])) == 0
            ):
                return {
                    "success": False,
                    "message": f"No employee found matching name '{employee_name}'",
                    "searchResponse": search_result,
                }

            # Pick the most relevant employee (first entry)
            top_employee = search_result["employees"][0]
            employee_id = str(top_employee.get("employeeId") or top_employee.get("id"))

            if not employee_id:
                return {
                    "success": False,
                    "message": f"Unable to extract employeeId from search result for '{employee_name}'",
                    "searchResponse": search_result,
                }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Failed resolving employee name '{employee_name}' to an employeeId"
            }

    # Final validation: employee_id must exist now
    if not employee_id:
        return {
            "success": False,
            "message": "Either employee_id or employee_name must be provided."
        }

    # Build API URL using employee_id
    url = f"{base_url}/ms/employee/api/v1/get-employee-by-employeeid/{employee_id}"

    # Prepare headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": (
            f"_KAPTURECRM_SESSION={session_cookie}; "
            f"JSESSIONID={jsessionid}; "
            f"JSESSIONRID={jsessionrid}"
        ),
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to fetch employee details for employeeId={employee_id}"
        }

@mcp.tool()
async def get_kapture_ticket_list(
    sort_by_column: str = "last_conversation_time",
    type: str = "5",
    status: str = "P",
    folder_id: str = "-1",
    page_no: int = 0,
    sort_type: str = "desc",
    page_size: int = 50,
    query: str = "status=P&reopened=&sub_status=&emp_id=-1&type=&emp_queue=&priority=&viewfilter_id=&cus_customer_code=&customer_name=&customer_phone=&customer_email=&folder_id=-1",
    response_type: str = "json",
    base_url: str = BASE_URL,
    session_cookie: str = None,
    jsessionid: str = None,
    jsessionrid: str = None,
    ksid: str = None
) -> dict:
    """
    Retrieve a list of tickets from the KaptureCRM system.

    This API returns ticket data based on filter, sort and pagination parameters.
    The request is made as *x-www-form-urlencoded* and supports multiple ticket types,
    statuses, sub-statuses and employee-level filters.

    ------------------------------------------------------------------

    **Endpoint Used**
    POST https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list

    **Core Parameters**
    - "sort_by_column": Sorting field (default "last_conversation_time")
    - "type": Ticket type (default "5")
    - "status": Ticket status (default "P")
    - "folder_id": Folder filter (default "-1")
    - "page_no": Pagination index (default 0)
    - "sort_type": Sorting order ("asc" / "desc")
    - "page_size": Items per page (default 50)
    - "query": Extensive filter query string
    - "response_type": Always "json"

    ------------------------------------------------------------------

    **Status Reference**
        TASK_PENDING = 'P'
        TASK_COMPLETE = 'C'
        JUNK_TASK = 'J'

    **Ticket Type Reference**
        CALL_TASK = 'B'
        CHAT_TASK = 'D'
        AMC_TICKET = 'A'
        GENERAL_TASK = 'G'
        TWITTER_TASK = 'T'
        FACEBOOK_TASK = 'F'
        INTERNAL_TICKET = 'I'
        GOOGLE_PLAY_TASK = 'X'
        INSTAGRAM_TASK = 'M'
        EMAIL_TICKET_TASK = 'E'
        OTHER_COMMUNICATION_TASK = 'O'
        CUSTOMER_TASK = 'H'
        WHATSAPP_TASK = 'W'
        YOUTUBE_TASK = 'Y'
        GOOGLE_REVIEW_TASK = 'Q'
        LINKEDIN_TASK = 'R'
        GOOGLE_BUSINESS_MESSAGES_TASK = 'S'
        APPLE_APP_STORE_TASK = 'x'
        LINE_TASK = 'P'

    **SubStatus Reference**
        PENDING_SUB_STATUS = "PS"
        REPLIED_SUB_STATUS = "RES"
        RESOLVED_SUB_STATUS = "RS"
        ANSWERED_SUB_STATUS = "AS"
        UNANSWERED_SUB_STATUS = "UAS"
        UNATTENDED_SUB_STATUS = "US"
        CUSTOMER_REPLIED_SUB_STATUS = "CRS"

    Note:
        - emp_id=-1 means "all employees"
        - The "query" parameter must always contain the exact raw string you pass.

    ------------------------------------------------------------------

    Args:
        sort_by_column: Column name for sorting ("last_conversation_time").
        type: Ticket type.
        status: Ticket status.
        folder_id: Folder filter.
        page_no: Page number for pagination.
        sort_type: Sorting order.
        page_size: Page size.
        query: Raw query string for filters (must be passed as-is).
        response_type: "json" (default).
        base_url: Base URL for KaptureCRM system.
        session_cookie: _KAPTURECRM_SESSION value.
        jsessionid: JSESSIONID value.
        jsessionrid: JSESSIONRID value.
        ksid: _KSID cookie value.

    ------------------------------------------------------------------

    Returns:
        dict: Response object containing ticket list, pagination details, and metadata.

    ------------------------------------------------------------------

    Example:
        # Get default ticket list (pending tickets)
        get_kapture_ticket_list()

        # Sort by priority
        get_kapture_ticket_list(sort_by_column="priority")

        # Get next page
        get_kapture_ticket_list(page_no=1)

        # Fetch tickets of specific type
        get_kapture_ticket_list(type="E")  # email tickets

        # Custom query string
        get_kapture_ticket_list(query="status=P&emp_id=123&folder_id=-1")

    ------------------------------------------------------------------

    Use Cases:
        - Fetch all pending tickets for an agent dashboard
        - Get tickets sorted by conversation time or priority
        - Filter tickets by employee, customer, type, or status
        - Create custom ticket reports or insights
        - Paginate through large ticket sets

    ------------------------------------------------------------------

    Notes:
        - All parameters with quotes MUST be preserved exactly.
        - Cookie handling follows the same pattern as previous tools.
        - Request must use x-www-form-urlencoded, not JSON.

    """

    # Token fallback (same pattern as previous tools)
    session_cookie = session_cookie or auth_tokens.DEFAULT_SESSION_COOKIE
    jsessionid = jsessionid or auth_tokens.DEFAULT_JSESSIONID
    jsessionrid = jsessionrid or auth_tokens.DEFAULT_JSESSIONRID
    ksid = ksid or auth_tokens.DEFAULT_KSID

    url = f"{base_url}/api/version3/ticket/get-ticket-list"

    # Headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": (
            f"_KAPTURECRM_SESSION={session_cookie}; "
            f"JSESSIONID={jsessionid}; "
            f"JSESSIONRID={jsessionrid}; "
            f"_KSID={ksid}"
        )
    }

    # Payload for x-www-form-urlencoded
    form_data = {
        "sort_by_column": sort_by_column,
        "type": type,
        "status": status,
        "folder_id": folder_id,
        "query": query,
        "page_no": page_no,
        "sort_type": sort_type,
        "page_size": page_size,
        "response_type": response_type
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                data=form_data,
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to retrieve ticket list from KaptureCRM"
        }

@mcp.tool(name="get_folders_by_level")
def get_folders_by_level(level: int = 2) -> dict:
    """
    KaptureCRM - Get Folders By Level API

    This tool calls the remote KaptureCRM API to retrieve folder details for a specific folder hierarchy level.

    ---
    ### 🔍 **Description**
    This API fetches ticket folders based on the folder level.  
    It accepts a JSON body with a single field:

    - `level`: (number) The folder level you want to fetch.  
      Example: level = 2

    ---
    ### 📌 **Request Type**
    `POST`  
    `Content-Type: application/json`

    ---
    ### 🧩 **Session Token Handling**
    - Uses the same cookie format and handling pattern used in previous tools.
    - The caller must supply the session cookie before invoking this tool.
    - Cookie must contain values in **exact same format** as:

        ```
        _KAPTURECRM_SESSION=rmdjjhnjjcnimda493ossnigol184607rmdjjhnjjchwrxu8tgd5;; 
        JSESSIONID=C530D631B5D92AE541E08FE157AB54DA; 
        JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ
        ```

    ---
    ### 📝 **Parameters**
    - `level` (int) → folder level to fetch  
      **Default:** `2` (matches your example request)

    ---
    ### 📤 **Returns**
    - JSON response from KaptureCRM
    - If an error occurs, returns a structured error payload with status code and message.

    ---
    ### 🧪 **Example Invocation**
    ```json
    {
      "tool": "get_folders_by_level",
      "arguments": {
        "level": 2
      }
    }
    ```

    ---
    ### 🚦 **Notes for the LLM**
    - Do not change the value of `level` unless user gives a new value.
    - Do not modify any string literals inside cookies.
    - This tool must use `application/json` and send body as raw JSON exactly like the curl example.
    """

    import requests
    import json

    url = "https://demokapairlines.kapturecrm.com/ms/ticket-configuration/ticket-configuration/get-folders-by-level"

    # Retrieve session cookie from env / global session store (same as previous MCP tools)
    session_cookie = SESSION.get("cookie")
    if not session_cookie:
        return {
            "error": "SESSION_COOKIE_MISSING",
            "message": "Session cookie is required. Use set_kapture_session_cookie() before calling this tool."
        }

    headers = {
        "Content-Type": "application/json",
        "Cookie": session_cookie
    }

    payload = {
        "level": level
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return {
            "status_code": response.status_code,
            "data": response.json() if response.text else {}
        }
    except Exception as e:
        return {
            "error": "REQUEST_FAILED",
            "message": str(e)
        }

@mcp.tool(name="get_pr_config_template_by_key")
def get_pr_config_template_by_key(
    prKey: str = "TWITTER_DM_AND_TWEET_SAME_USER_NO_MERGE"
) -> dict:
    """
    KaptureCRM - Get Partner Resource Configuration Template By Key API

    This tool calls the remote KaptureCRM API to retrieve the configuration template
    structure for a given *partner resource key* (prKey). This API helps determine the
    exact JSON structure or value format that should be provided when entering or
    updating a partner resource value.

    ---
    ### 🔍 Description
    This API fetches the *partner-resource configuration template* based on the given prKey.  
    It accepts a single **request query param**:

    - `prKey`: A partner resource key that maps to a specific template structure.  
      Example (must stay exactly as provided):  
      `"TWITTER_DM_AND_TWEET_SAME_USER_NO_MERGE"`

    The response defines **how PR values should be structured/formatted** during create/update operations.

    ---
    ### 📌 Request Type
    `POST` request  
    No body is passed.  
    `prKey` is passed strictly via **query parameters**.

    ---
    ### 🧩 Session Token Handling
    - Uses the **same session cookie management** pattern as previous MCP tools.
    - User must first call:  
      `set_kapture_session_cookie("_KAPTURECRM_SESSION=...; JSESSIONID=...; JSESSIONRID=...")`
    - Cookies must remain **exactly as provided**.  
      Nothing inside quotes should be altered.

    Example cookie format expected (unchanged):
    ```
    _KAPTURECRM_SESSION=tkkd8ehb4znimda493ossnigol184607tkkd8ehb4zho0tr202e1;; 
    JSESSIONID=40D61D29CCAA43BFBB3E3D499828FC01; 
    JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; 
    _KSID=01f69559a32849629767f3b397d1f383.3SDmlhjtZ1s2DmlhjtZ
    ```

    ---
    ### 📝 Parameters
    - `prKey` (string) – Partner resource key used to retrieve the config structure.  
      **Default:** `"TWITTER_DM_AND_TWEET_SAME_USER_NO_MERGE"`

    ---
    ### 📤 Returns
    - JSON response containing the configuration template.
    - Or an error dictionary with details.

    ---
    ### 🧪 Example Invocation
    ```json
    {
      "tool": "get_pr_config_template_by_key",
      "arguments": {
        "prKey": "TWITTER_DM_AND_TWEET_SAME_USER_NO_MERGE"
      }
    }
    ```

    ---
    ### ⚠ Notes for the LLM
    - Do **not** modify `prKey` unless the user provides a new value.
    - Do **not** modify cookie text under any condition.
    - This is a **POST** API with **no body** and **only query params**.
    """

    import requests

    base_url = (
        "https://demokapairlines.kapturecrm.com/api/version3/ticket/"
        "get-pr-config-template-by-key"
    )

    # Retrieve cookie from global session store
    session_cookie = SESSION.get("cookie")
    if not session_cookie:
        return {
            "error": "SESSION_COOKIE_MISSING",
            "message": (
                "Session cookie is required. "
                "Use set_kapture_session_cookie() before calling this tool."
            )
        }

    headers = {
        "Cookie": session_cookie
    }

    params = {
        "prKey": prKey  # must remain exactly as user passed
    }

    try:
        response = requests.post(base_url, headers=headers, params=params)
        return {
            "status_code": response.status_code,
            "data": response.json() if response.text else {}
        }
    except Exception as e:
        return {
            "error": "REQUEST_FAILED",
            "message": str(e)
        }



if __name__ == "__main__":
    # Run the MCP server with HTTP transport (remote)
    mcp.run(transport="http", host="0.0.0.0", port=8080)
