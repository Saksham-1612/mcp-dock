"""FastMCP Server - Generated from Postman Collection

Collection: VB Platform
Generated: 20251129 022251
"""

import os
import httpx
from fastmcp import FastMCP
from typing import Optional, Dict, Any

# Initialize FastMCP server
mcp = FastMCP("VB Platform")

# Load environment variables

# HTTP client
client = httpx.Client(timeout=30.0)

@mcp.tool()
def exotel_airtel_local_db(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/call
    
    Method: POST
    URL: http://localhost:8002/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1000295",
        "config_id": "b962",
        "from_phone": "8047491993",
        "to_phone": "9305682895",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def ttsl_airtel_local_db(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/call
    
    Method: POST
    URL: http://localhost:8002/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1006150",
        "config_id": "b1190",
        "from_phone": "917965251573",
        "to_phone": "919305682895",
        "telephony_provider":"ttsl",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def twilio_airtel_local_db(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/call
    
    Method: POST
    URL: http://localhost:8002/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1007202",
        "config_id": "b1494",
        "from_phone": "+15615624778",
        "to_phone": "+919305682895",
        "conversation_context": {
            "prompt_input": {
                "name": "Saksham"
            },
            "pre_call": {
                "at_1": {
                    "name": "Saksham",
                    "phone": "+919305682895"
                }
            },
            "post_call": {
                "at_2": {
                    "conversation_id": "",
                    "ticket_id": "",
                    "name": "",
                    "phone": ""
                }
            }
        }
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def ozontel_airtel_local_db(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/call
    
    Method: POST
    URL: http://localhost:8002/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1000295",
        "config_id": "b962",
        "from_phone": "918041437685",
        "to_phone": "919305682895",
        "telephony_provider":"ozontel",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def acefone(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/call
    
    Method: POST
    URL: http://localhost:8002/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1006150",
        "config_id": "b1274",
        "from_phone": "918069232841",
        "to_phone": "919305682895",
        "telephony_provider":"ttsl",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def convox_direct(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect
    
    Method: POST
    URL: https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect
    Body: JSON request body
    
    Example body:
    ```json
    {
        "From": "9876543210",
        "To": "9305682895",
        "WebsocketUrl": "wss://closing-airedale-moderately.ngrok-free.app/orchestrator/ws/12345678",
        "StatusCallback": "https://closing-airedale-moderately.ngrok-free.app/telephony-callback/call/convox/callback",
        "client_id": "vindhya"
    }
    ```
    """
    # Build URL
    url = "https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect"
    
    # Build headers
    headers = {
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
def convox(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call
    
    Method: POST
    URL: https://voicebot-platform.infra.kapturecrm.com/telephony/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "democrm",
        "config_id": "b1515",
        "from_phone": "7965251102",
        "to_phone": "9305682895",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "https://voicebot-platform.infra.kapturecrm.com/telephony/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
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
def acefone_prod(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://vb-platform.infra.kapturecrm.com/telephony/call
    
    Method: POST
    URL: https://vb-platform.infra.kapturecrm.com/telephony/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1007091",
        "config_id": "b1327",
        "from_phone": "8069232843",
        "to_phone": "9610635575",
        "telephony_provider": "acefone",
        "conversation_context": {
            "prompt_input": {
                "Customer Name": "shalini",
                "Account Number": "JFLP100000004567",
                "Amount": "4527",
                "Due Date": "30th nov",
                "ticket_id": "12345678",
                "email": "shalini.priyadarshini@kapturecrm.com",
                "phone_number": "8789145668",
                "customer_id": "1234567"
            },
            "post_call": {
                "at_1": {
                    "ticket_id": null,
                    "conversation_id": null
                }
            },
            "initial_message":"Welcome to JCL bot"
        }
    }
    ```
    """
    # Build URL
    url = "https://vb-platform.infra.kapturecrm.com/telephony/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
        "Cookie": "INGRESSCOOKIE=1762744259.978.47.586377|39a7961487f1ffdb1025aaec02f726be",
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
def convox_bot(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to http://localhost:8002/telephony/call
    
    Method: POST
    URL: http://localhost:8002/telephony/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY1007058",
        "config_id": "b1222",
        "from_phone": "08047491993",
        "to_phone": "09305682895",
        "telephony_provider" : "convox"
    }
    ```
    """
    # Build URL
    url = "http://localhost:8002/telephony/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
        "Cookie": "INGRESSCOOKIE=1762336126.034.34.903944|39a7961487f1ffdb1025aaec02f726be",
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
def ozontel_direct(url: str = "https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962", callback_url: str = "https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962", outbound_version: str = "2", caller_id: str = "918041437685", phone_no: str = "9305682895", api_key: str = "KK6616644f19cb1d52f444e16b3a87be79", ) -> Dict[str, Any]:
    """GET request to https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79
    
    Method: GET
    URL: https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79
    Query Parameters:
  - url: Query parameter (default: "https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962")
  - callback_url: Query parameter (default: "https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962")
  - outbound_version: Query parameter (default: "2")
  - caller_id: Query parameter (default: "918041437685")
  - phone_no: Query parameter (default: "9305682895")
  - api_key: Query parameter (default: "KK6616644f19cb1d52f444e16b3a87be79")
    """
    # Build URL
    url = "https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79"
    
    # Build headers
    headers = {
        "api_key": "KK4bac48250b76f200910b36f60268533d",
        "phone_no": "9305682895",
        "caller_id": "519308",
        "outbound_version": "2",
        "callback_url": "",
    }
    
    
    # Build query parameters
    params = {
        "url": url,
        "callback_url": callback_url,
        "outbound_version": outbound_version,
        "caller_id": caller_id,
        "phone_no": phone_no,
        "api_key": api_key,
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

@mcp.tool()
def save_keys(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony
    
    Method: POST
    URL: https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony
    Body: JSON request body
    
    Example body:
    ```json
    {
        "bot_id": "b1490",
        "ACEFONE_API_KEY": "",
        "EXOTEL_API_KEY": "",
        "EXOTEL_API_TOKEN": "",
        "EXOTEL_APP_ID": "",
        "EXOTEL_ACCOUNT_SID": "",
        "EXOTEL_AUTH_REGION": "",
        "EXOTEL_SUBDOMAIN": "",
        "TWILIO_ACCOUNT_SID": "",
        "TWILIO_AUTH_TOKEN": "",
        "TWILIO_CALLBACK_URL": "",
        "OZONETEL_CALLER_ID": "",
        "OZONETEL_API_KEY": "",
        "OZONETEL_SIP_ID": "",
        "OZONETEL_SUBDOMAIN": "",
        "OZONETEL_CALLBACK_URL": "",
        "OZONETEL_APPLICATION_URL": ""
    }
    ```
    """
    # Build URL
    url = "https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony"
    
    # Build headers
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZW1vY3JtIiwiZXhwIjoyMDU0NzkxMDkwfQ.b5ZXLw_nq3q-uKA1F4hbdJkTU8Rrkm96ElJzxkM3J8A",
        "Content-Type": "application/json",
        "Cookie": "INGRESSCOOKIE=1762358861.546.43.636739|36aa91b3dbe829107e9a794857bc2a1d",
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
def ozonetel_bb(body: Dict[str, Any] = None) -> Dict[str, Any]:
    """POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call
    
    Method: POST
    URL: https://voicebot-platform.infra.kapturecrm.com/telephony/call
    Body: JSON request body
    
    Example body:
    ```json
    {
        "client_id": "KEY14833",
        "config_id": "b1547",
        "from_phone": "918041437685",
        "to_phone": "919305682895",
        // "telephony_provider":"ozonetel",
        "conversation_context": {}
    }
    ```
    """
    # Build URL
    url = "https://voicebot-platform.infra.kapturecrm.com/telephony/call"
    
    # Build headers
    headers = {
        "Content-Type": "application/json",
        "Cookie": "INGRESSCOOKIE=1763966409.636.37.142457|2dc6476baca7476a7d48411d78acd2c5; INGRESSCOOKIE=1763979130.601.27187.26488|9ee3917376919276244875e88eb27f43",
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