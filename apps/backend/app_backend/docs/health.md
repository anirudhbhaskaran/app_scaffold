# Health Endpoint

## Route
GET /health

## Description
Basic liveness check.

## Response
200 OK

{
  "status": "ok"
}

## CURL
curl -X GET http://localhost:8000/health

## Test Route
curl -X GET "http://localhost:8000/test?route=health"
