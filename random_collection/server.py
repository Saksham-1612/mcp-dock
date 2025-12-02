"""FastMCP Server - Generated from Postman Collection

Collection: Public GET APIs (Hardcoded)
Generated: 20251202 083421
"""

import os
import httpx
from fastmcp import FastMCP
from typing import Optional, Dict, Any

# Initialize FastMCP server
mcp = FastMCP("Public GET APIs (Hardcoded)")

# Load environment variables

# HTTP client
client = httpx.Client(timeout=30.0)

@mcp.tool()
def get_github_user_octocat() -> Dict[str, Any]:
    """GET request to api.github.com/users/octocat
    
    Method: GET
    URL: api.github.com/users/octocat
    """
    # Build URL
    url = "api.github.com/users/octocat"
    
    # Build headers
    headers = {
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="GET",
            url=url,
            headers=headers,
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
def get_all_posts() -> Dict[str, Any]:
    """GET request to jsonplaceholder.typicode.com/posts
    
    Method: GET
    URL: jsonplaceholder.typicode.com/posts
    """
    # Build URL
    url = "jsonplaceholder.typicode.com/posts"
    
    # Build headers
    headers = {
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="GET",
            url=url,
            headers=headers,
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
def get_post_1() -> Dict[str, Any]:
    """GET request to jsonplaceholder.typicode.com/posts/1
    
    Method: GET
    URL: jsonplaceholder.typicode.com/posts/1
    """
    # Build URL
    url = "jsonplaceholder.typicode.com/posts/1"
    
    # Build headers
    headers = {
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="GET",
            url=url,
            headers=headers,
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
def random_cat_fact() -> Dict[str, Any]:
    """GET request to catfact.ninja/fact
    
    Method: GET
    URL: catfact.ninja/fact
    """
    # Build URL
    url = "catfact.ninja/fact"
    
    # Build headers
    headers = {
    }
    
    
    # Build query parameters
    params = {}
    
    try:
        # Make request
        response = client.request(
            method="GET",
            url=url,
            headers=headers,
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