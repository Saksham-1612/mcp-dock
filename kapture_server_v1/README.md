# Kapture Api - MCP Server

Generated MCP server from Postman collection.

**Generated:** 20251129 012903

## Overview

This MCP server provides 6 tool(s) based on your Postman collection:

- **get_ticket_list**: POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list
- **task_assign**: POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment
- **dispose_task**: POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task
- **junk_task**: POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task
- **merge_task**: POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task
- **get_ticket_detail**: GET request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes

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
docker build -t Kapture Api-mcp .
```

### Test Locally

```bash
docker run -p 8080:8080 --env-file .env Kapture Api-mcp
```

### Deploy to Cloud Run

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/Kapture Api-mcp

# Deploy to Cloud Run
gcloud run deploy Kapture Api-mcp \
  --image gcr.io/YOUR_PROJECT_ID/Kapture Api-mcp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
```

## Usage

Once deployed, you can use this MCP server with any MCP-compatible client.

### Available Tools

#### `get_ticket_list`

POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list

- **Method:** POST
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-list
- **Body:** JSON object

---

#### `task_assign`

POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment

- **Method:** POST
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/task-assignment
- **Body:** JSON object

---

#### `dispose_task`

POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task

- **Method:** POST
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/dispose-task
- **Body:** JSON object

---

#### `junk_task`

POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task

- **Method:** POST
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/junk-task
- **Body:** JSON object

---

#### `merge_task`

POST request to https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task

- **Method:** POST
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/merge-task
- **Body:** JSON object

---

#### `get_ticket_detail`

GET request to https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes

- **Method:** GET
- **URL:** https://demokapairlines.kapturecrm.com/api/version3/ticket/get-ticket-detail?id=935878744&data_type=history&cdate=2025-11-25+16:40:25&fetch_action_name=yes
- **Query Parameters:**
  - `id`
  - `data_type`
  - `cdate`
  - `fetch_action_name`

---


## Support

This server was automatically generated from a Postman collection. If you encounter any issues, please verify:

1. Environment variables are set correctly
2. API endpoints are accessible
3. Authentication credentials are valid

## License

Generated code - customize as needed for your use case.