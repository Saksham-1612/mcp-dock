# VB Collection - MCP Server

Generated MCP server from Postman collection.

**Generated:** 20251202 115743

## Overview

This MCP server provides 1 tool(s) based on your Postman collection:

- **create_call**: POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call

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
docker build -t VB Collection-mcp .
```

### Test Locally

```bash
docker run -p 8080:8080 --env-file .env VB Collection-mcp
```

### Deploy to Cloud Run

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/VB Collection-mcp

# Deploy to Cloud Run
gcloud run deploy VB Collection-mcp \
  --image gcr.io/YOUR_PROJECT_ID/VB Collection-mcp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
```

## Usage

Once deployed, you can use this MCP server with any MCP-compatible client.

### Available Tools

#### `create_call`

POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call

- **Method:** POST
- **URL:** https://voicebot-platform.infra.kapturecrm.com/telephony/call
- **Body:** JSON object

---


## Support

This server was automatically generated from a Postman collection. If you encounter any issues, please verify:

1. Environment variables are set correctly
2. API endpoints are accessible
3. Authentication credentials are valid

## License

Generated code - customize as needed for your use case.