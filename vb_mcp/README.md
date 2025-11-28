# VB Platform - MCP Server

Generated MCP server from Postman collection.

**Generated:** 20251129 022251

## Overview

This MCP server provides 12 tool(s) based on your Postman collection:

- **exotel_airtel_local_db**: POST request to http://localhost:8002/call
- **ttsl_airtel_local_db**: POST request to http://localhost:8002/call
- **twilio_airtel_local_db**: POST request to http://localhost:8002/call
- **ozontel_airtel_local_db**: POST request to http://localhost:8002/call
- **acefone**: POST request to http://localhost:8002/call
- **convox_direct**: POST request to https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect
- **convox**: POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call
- **acefone_prod**: POST request to https://vb-platform.infra.kapturecrm.com/telephony/call
- **convox_bot**: POST request to http://localhost:8002/telephony/call
- **ozontel_direct**: GET request to https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79
- **save_keys**: POST request to https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony
- **ozonetel_bb**: POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call

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
docker build -t VB Platform-mcp .
```

### Test Locally

```bash
docker run -p 8080:8080 --env-file .env VB Platform-mcp
```

### Deploy to Cloud Run

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/VB Platform-mcp

# Deploy to Cloud Run
gcloud run deploy VB Platform-mcp \
  --image gcr.io/YOUR_PROJECT_ID/VB Platform-mcp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
```

## Usage

Once deployed, you can use this MCP server with any MCP-compatible client.

### Available Tools

#### `exotel_airtel_local_db`

POST request to http://localhost:8002/call

- **Method:** POST
- **URL:** http://localhost:8002/call
- **Body:** JSON object

---

#### `ttsl_airtel_local_db`

POST request to http://localhost:8002/call

- **Method:** POST
- **URL:** http://localhost:8002/call
- **Body:** JSON object

---

#### `twilio_airtel_local_db`

POST request to http://localhost:8002/call

- **Method:** POST
- **URL:** http://localhost:8002/call
- **Body:** JSON object

---

#### `ozontel_airtel_local_db`

POST request to http://localhost:8002/call

- **Method:** POST
- **URL:** http://localhost:8002/call
- **Body:** JSON object

---

#### `acefone`

POST request to http://localhost:8002/call

- **Method:** POST
- **URL:** http://localhost:8002/call
- **Body:** JSON object

---

#### `convox_direct`

POST request to https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect

- **Method:** POST
- **URL:** https://server13.vindhyainfo.com/api/v1/Accounts/vindhya2386/Calls/connect
- **Body:** JSON object

---

#### `convox`

POST request to https://voicebot-platform.infra.kapturecrm.com/telephony/call

- **Method:** POST
- **URL:** https://voicebot-platform.infra.kapturecrm.com/telephony/call
- **Body:** JSON object

---

#### `acefone_prod`

POST request to https://vb-platform.infra.kapturecrm.com/telephony/call

- **Method:** POST
- **URL:** https://vb-platform.infra.kapturecrm.com/telephony/call
- **Body:** JSON object

---

#### `convox_bot`

POST request to http://localhost:8002/telephony/call

- **Method:** POST
- **URL:** http://localhost:8002/telephony/call
- **Body:** JSON object

---

#### `ozontel_direct`

GET request to https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79

- **Method:** GET
- **URL:** https://kookoo.in/outbound/outbound.php?url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&callback_url=https://ozonetel.ngrok.io/telephony/inbound/KEY1000295/b962&outbound_version=2&caller_id=918041437685&phone_no=9305682895&api_key=KK6616644f19cb1d52f444e16b3a87be79
- **Query Parameters:**
  - `url`
  - `callback_url`
  - `outbound_version`
  - `caller_id`
  - `phone_no`
  - `api_key`

---

#### `save_keys`

POST request to https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony

- **Method:** POST
- **URL:** https://voicebot-platform.infra.kapturecrm.com/baseenginenew/save-keys/telephony
- **Body:** JSON object

---

#### `ozonetel_bb`

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