"""FastMCP Server - Generated from Postman Collection

Collection: Kapture Api
Generated: 20251129 012903
"""

import os
import httpx
from fastmcp import FastMCP
from typing import Optional, Dict, Any

# Initialize FastMCP server
mcp = FastMCP("Kapture Api")

# Load environment variables

# HTTP client
client = httpx.Client(timeout=30.0)

@mcp.tool()
def get_ticket_list(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list
    
    Method: POST
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list
    Body: JSON request body
    
    Example body:
    ```json
    {
      "sort_by_column": "last_conversation_time",
      "type": "5",
      "status": "P"
    }
    ```
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list"
    
    # Build headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KSID=80f29461eaf3498496d11b9957fa116f.3SDmlhjtZ1s2DmlhjtZ; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQzNDg4Nzk0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0MzUxMzMyMyUyQyUyMmxhc3RFdmVudElkJTIyJTNBOTM0JTJDJTIycGFnZUNvdW50ZXIlMjIlM0EzJTdE; _ga_6RBDMB8XTE=GS2.1.s1764343485$o406$g1$t1764343525$j20$l0$h0; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _ga_KKZH5KWGEE=GS2.1.s1764343482$o420$g1$t1764343526$j16$l0$h0; JSESSIONID=FE2B3240AF29DFD94C31255C854BD2FC; JSESSIONID=115BECD3B018CC05C35DC118BD5974D2; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; _KSID=0d021f0a023f46e0bdbc981a1f1550ac.3SDmlhjtZ1s2DmlhjtZ",
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="POST",
            url=url,
            headers=headers,
            json=body,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }

@mcp.tool()
def task_assign(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment
    
    Method: POST
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment
    Body: JSON request body
    
    Example body:
    ```json
    {
      "ticket_id": "9764072089627",
      "task_id": "935920326",
      "assign_to": "217346#Himanshu",
      "task_detail": "test"
    }
    ```
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment"
    
    # Build headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; _KSID=7a5e3061a5b64a5ca68c209e3abe6509.3SDmlhjtZ1s2DmlhjtZ; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _ga_6RBDMB8XTE=GS2.1.s1764346396$o407$g1$t1764347209$j31$l0$h0; JSESSIONID=969A99D1C241DD54E8FAD05AA7AE7BC4; _ga_KKZH5KWGEE=GS2.1.s1764346396$o421$g1$t1764347209$j24$l0$h0; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQ2MzMwNjcxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0NzI0Mzk5OCUyQyUyMmxhc3RFdmVudElkJTIyJTNBOTg1JTJDJTIycGFnZUNvdW50ZXIlMjIlM0E2JTdE",
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="POST",
            url=url,
            headers=headers,
            json=body,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }

@mcp.tool()
def dispose_task(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task
    
    Method: POST
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task
    Body: JSON request body
    
    Example body:
    ```json
    {
      "task_id": "935919331",
      "ticket_id": "9764072018889",
      "selected_folder_list": "1131562",
      "sub_status": "RS",
      "update_folder_id": "1131562",
      "new_ticket_ui": "true",
      "nui": "true",
      "assign_to": "184607#Demo Kapture Airlines",
      "task_detail": "test"
    }
    ```
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task"
    
    # Build headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _ga_6RBDMB8XTE=GS2.1.s1764346396$o407$g1$t1764347288$j59$l0$h0; JSESSIONID=02514F31182496BD17DD123A8096B762; _ga_KKZH5KWGEE=GS2.1.s1764346396$o421$g1$t1764347324$j23$l0$h0; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQ2MzMwNjcxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0NzMyNTA0MSUyQyUyMmxhc3RFdmVudElkJTIyJTNBOTk3JTJDJTIycGFnZUNvdW50ZXIlMjIlM0E3JTdE",
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="POST",
            url=url,
            headers=headers,
            json=body,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }

@mcp.tool()
def junk_task(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task
    
    Method: POST
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task
    Body: JSON request body
    
    Example body:
    ```json
    {
      "task_id": "935920326",
      "remark": "test"
    }
    ```
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task"
    
    # Build headers
    headers = {
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _ga_6RBDMB8XTE=GS2.1.s1764346396$o407$g1$t1764347288$j59$l0$h0; JSESSIONID=02514F31182496BD17DD123A8096B762; _ga_KKZH5KWGEE=GS2.1.s1764346396$o421$g1$t1764347324$j23$l0$h0; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQ2MzMwNjcxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0NzMyNTA0MSUyQyUyMmxhc3RFdmVudElkJTIyJTNBOTk3JTJDJTIycGFnZUNvdW50ZXIlMjIlM0E3JTdE",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="POST",
            url=url,
            headers=headers,
            json=body,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }

@mcp.tool()
def merge_task(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task
    
    Method: POST
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task
    Body: JSON request body
    
    Example body:
    ```json
    {
      "ticket_ids": "9764070979477,9764070704527",
      "task_ids": "935905686,935901656",
      "status": "P"
    }
    ```
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task"
    
    # Build headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _KSID=48e1e3b7da6f4747a163b806f225fed6.3SDmlhjtZ1s2DmlhjtZ; _ga_6RBDMB8XTE=GS2.1.s1764346396$o407$g1$t1764347459$j57$l0$h0; JSESSIONID=70B8035185F55066353071862BB71641; _ga_KKZH5KWGEE=GS2.1.s1764346396$o421$g1$t1764347468$j48$l0$h0; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQ2MzMwNjcxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0NzQ3OTkyNSUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTAzMyUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMTIlN0Q=",
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="POST",
            url=url,
            headers=headers,
            json=body,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }

@mcp.tool()
def get_ticket_detail(id: str = "935878744", data_type: str = "history", cdate: str = "2025-11-25+16:40:25", fetch_action_name: str = "yes", ) -> Dict[str, Any]:
    """GET request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes
    
    Method: GET
    URL: https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes
    Query Parameters:
  - id: Query parameter (default: "935878744")
  - data_type: Query parameter (default: "history")
  - cdate: Query parameter (default: "2025-11-25+16:40:25")
  - fetch_action_name: Query parameter (default: "yes")
    """
    # Build URL
    url = "https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes"
    
    # Build headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.1.490591123.1739451680; JSESSIONRID=3SDmlhjtZ1s2DmlhjtZ; timeOffset=0; AMP_MKTG_c2b5ae8605=JTdCJTdE; _KAPTURECRM_SESSION_AUTH_ADMIN=OVB1Y1FkSXNsU2ZRTkpnaXg2MzBqdz09|U2o5RkJNeWFRKzNiQ29LenVMckZRdz09; _KAPTURECRM_SESSION=myoohqks0snimda493ossnigol184607myoohqks0s74lse4u5pw; av=uilt; session_expire=eyJzeXN0ZW1UaW1lIjoxNzY0MzQzNDg1NTY5LCJleHBpcnlUaW1lIjoxNzY0Mzk3NDg1NTY5fQ==; mp_6c02537f8f758b0feedfd53581fbaeec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24device_id%22%3A%22194ff66421e21f-00b07dad795bff-16462c6e-ff000-194ff66421e21f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24search_engine%22%3A%22google%22%7D; _KSID=48e1e3b7da6f4747a163b806f225fed6.3SDmlhjtZ1s2DmlhjtZ; JSESSIONID=70B8035185F55066353071862BB71641; _ga_KKZH5KWGEE=GS2.1.s1764346396$o421$g1$t1764347496$j20$l0$h0; _ga_6RBDMB8XTE=GS2.1.s1764346396$o407$g1$t1764347496$j20$l0$h0; AMP_c2b5ae8605=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1YjdiZjE0NC01ZWU1LTRkYTctYThhMS0xNTg1YWZkYmFkMzMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIxODQ2MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MzQ2MzMwNjcxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDM0NzQ5NjA1NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTAzNyUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMTMlN0Q=",
        "Referer": "https://demokapairlines.kapturecrm.com/nui/tickets/assigned_to_me/5/-1/0/detail/935878744/9764069025216",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-KapTrace-ID": "febfb394-7184-4be4-a77f-202188e4236b###184607",
        "sec-ch-ua": ""Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": ""Linux"",
    }
    
    
    # Build query parameters
    params = {
        "id": id,
        "data_type": data_type,
        "cdate": cdate,
        "fetch_action_name": fetch_action_name,
    }
    
    try:
        # Make request
        response = client.request(
            method="GET",
            url=url,
            headers=headers,
            params=params,
        )
        
        # Return response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500,
        }


if __name__ == "__main__":
    # Run the MCP server with HTTP transport (remote)
    # Access the server at http://localhost:8080/mcp
    mcp.run(transport="http", host="0.0.0.0", port=8080)