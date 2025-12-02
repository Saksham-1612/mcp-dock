# Public GET APIs (Hardcoded) - MCP Server

Generated MCP server from Postman collection.

**Generated:** 20251202 083421

## Overview

This MCP server provides 4 tool(s) based on your Postman collection:

- **get_github_user_octocat**: GET request to api.github.com/users/octocat
- **get_all_posts**: GET request to jsonplaceholder.typicode.com/posts
- **get_post_1**: GET request to jsonplaceholder.typicode.com/posts/1
- **random_cat_fact**: GET request to catfact.ninja/fact

## Environment Variables

No authentication is required for this server.

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
docker build -t Public GET APIs (Hardcoded)-mcp .
```

### Test Locally

```bash
docker run -p 8080:8080 --env-file .env Public GET APIs (Hardcoded)-mcp
```

### Deploy to Cloud Run

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/Public GET APIs (Hardcoded)-mcp

# Deploy to Cloud Run
gcloud run deploy Public GET APIs (Hardcoded)-mcp \
  --image gcr.io/YOUR_PROJECT_ID/Public GET APIs (Hardcoded)-mcp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
```

## Usage

Once deployed, you can use this MCP server with any MCP-compatible client.

### Available Tools

#### `get_github_user_octocat`

GET request to api.github.com/users/octocat

- **Method:** GET
- **URL:** api.github.com/users/octocat

---

#### `get_all_posts`

GET request to jsonplaceholder.typicode.com/posts

- **Method:** GET
- **URL:** jsonplaceholder.typicode.com/posts

---

#### `get_post_1`

GET request to jsonplaceholder.typicode.com/posts/1

- **Method:** GET
- **URL:** jsonplaceholder.typicode.com/posts/1

---

#### `random_cat_fact`

GET request to catfact.ninja/fact

- **Method:** GET
- **URL:** catfact.ninja/fact

---


## Support

This server was automatically generated from a Postman collection. If you encounter any issues, please verify:

1. Environment variables are set correctly
2. API endpoints are accessible
3. Authentication credentials are valid

## License

Generated code - customize as needed for your use case.