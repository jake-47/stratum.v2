# API Reference

Complete reference for the Product API.

## Endpoints

### GET /api/v1/users

Retrieves a list of users.

#### Parameters

| Name | Type | Description |
|------|------|-------------|
| `limit` | integer | Maximum number of results |
| `offset` | integer | Number of results to skip |

#### Response

```json
{
  "users": [
    {
      "id": "user-123",
      "name": "Example User"
    }
  ],
  "total": 1
}