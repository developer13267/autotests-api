import httpx

login_payload = {
    "email": "qwerty123321@gmail.com",
    "password": "qwerty123321@gmail.com"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

get_users_token = login_response_data['token']['refreshToken']
get_users_headers = {
    "Authorization": f"Bearer {get_users_token}"
}
get_users_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_users_headers )
get_users_response_data = get_users_response .json()
print("Get users response:", get_users_response_data)
print("Status Code:", get_users_response.status_code)