"""FastMCP Server - Generated from Postman Collection

Collection: VB Collection
Generated: 20251202 115743
"""

import os
import httpx
from fastmcp import FastMCP
from typing import Optional, Dict, Any

# Initialize FastMCP server
mcp = FastMCP("VB Collection")

# Load environment variables

# HTTP client
client = httpx.Client(timeout=30.0)

@mcp.tool()
def create_call(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call
    
    Method: POST
    URL: https://voicebot-platform.infra.kapturecrm.com/telephony/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1007185",
        "config_id": "b1512",
        "from_phone": "+63282313181",
        "to_phone": "+919305682895",
        "conversation_context": {
            "prompt_input": {
                "consultation_fees": "567",
                "Doctor_Name": "Saksham",
                "Customer_Name": "Anshuman",
                "Doctor_Specialty": "Brain",
                "Booking_Date": "17-11-2025",
                "Hospital_Name": "okok Hospitals",
                "Booking_Slot": "first",
                "Alternate_Doctor_Name": "Nonu",
                "Customer_Number": "7357190759",
                "Customer_Age": "22",
                "Customer_Gender": "Male"
            },
            "post_call": {
                "at_1": {
                    "conversation_id": "456678de78e7878e",
                    "ticket_id": "4545676543456",
                    "appointment_id": "4567876586798"
                }
            }
        }
    }
    ```
    """
    # Build URL
    url = "https://voicebot-platform.infra.kapturecrm.com/telephony/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
        "Cookie": "INGRESSCOOKIE=1762867015.179.40.829476|39a7961487f1ffdb1025aaec02f726be; INGRESSCOOKIE=1763620985.191.3757.782960|04b8272669bef83866ee77f27c3359ed; INGRESSCOOKIE=1763620992.326.3757.838243|9ee3917376919276244875e88eb27f43",
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


if __name__ == "__main__":
    # Run the MCP server with HTTP transport (remote)
    # Access the server at http://localhost:8080/mcp
    mcp.run(transport="http", host="0.0.0.0", port=8080)