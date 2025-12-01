# Sample API - MCP Server

Generated MCP server from Postman collection.

**Generated:** 20251129 001803

## Overview

This MCP server provides 5 tool(s) based on your Postman collection:

- **get_users**: Retrieve a list of users with pagination
- **get_user_by_id**: Get a specific user by ID
- **create_user**: Create a new user
- **update_user**: Update an existing user
- **delete_user**: Delete a user by ID

## Environment Variables

The following environment variables are required for authentication:

- `BEARER_TOKEN`: Bearer token for authentication
- `API_KEY`: API key for authentication
- `BASIC_AUTH_USERNAME`: Username for basic authentication
- `BASIC_AUTH_PASSWORD`: Password for basic authentication

Create a `.env` file based on `env.example`:

```bash
cp env.example .env
# Edit .env with your credentials
```

## Local Development

### Installation

```bash
pip install -r requirements.txt
```

### Running the Server

```bash
python server.py
```

The MCP server will start on **http://localhost:8080/mcp** using HTTP transport.

You can test the server is running by visiting:
```bash
curl http://localhost:8080/health
```

### Connecting to the Server

Use any MCP client with the server URL:
```
http://localhost:8080/mcp
```

## Cloud Run Deployment

### Build Docker Image

```bash
docker build -t Sample API-mcp .
```

### Test Locally

```bash
docker run -p 8080:8080 --env-file .env Sample API-mcp
```

### Deploy to Cloud Run

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/Sample API-mcp

# Deploy to Cloud Run
gcloud run deploy Sample API-mcp \
  --image gcr.io/YOUR_PROJECT_ID/Sample API-mcp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
--set-env-vars BEARER_TOKEN=your-token-here```

## Usage

Once deployed, you can use this MCP server with any MCP-compatible client.

### Available Tools

#### `get_users`

Retrieve a list of users with pagination

- **Method:** GET
- **URL:** https://api.example.com/users?page=1&limit=10
- **Query Parameters:**
  - `page`
  - `limit`

---

#### `get_user_by_id`

Get a specific user by ID

- **Method:** GET
- **URL:** https://api.example.com/users/{userId}
- **Path Parameters:**
  - `userId`

---

#### `create_user`

Create a new user

- **Method:** POST
- **URL:** https://api.example.com/users
- **Body:** JSON object

---

#### `update_user`

Update an existing user

- **Method:** PUT
- **URL:** https://api.example.com/users/{id}
- **Path Parameters:**
  - `id`
- **Body:** JSON object

---

#### `delete_user`

Delete a user by ID

- **Method:** DELETE
- **URL:** https://api.example.com/users/{userId}
- **Path Parameters:**
  - `userId`

---


## Support

This server was automatically generated from a Postman collection. If you encounter any issues, please verify:

1. Environment variables are set correctly
2. API endpoints are accessible
3. Authentication credentials are valid

## License

Generated code - customize as needed for your use case.