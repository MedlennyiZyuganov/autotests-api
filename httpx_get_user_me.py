import httpx

payload = {
  "email": "user@example.com",
  "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {access_token}"}
access_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
access_response_data = access_response.json()

print("Access response:", access_response_data)
print("Status Code:", access_response.status_code)