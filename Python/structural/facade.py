import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data)
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}")
        return response.status_code


class UserAuthentication:
    def __init__(self, api_client):
        self.api_client = api_client

    def login(self, credentials):
        return self.api_client.post("login", credentials)

    def logout(self, user_id):
        return self.api_client.post(f"logout/{user_id}", {})


class UserFetcher:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id):
        return self.api_client.get(f"users/{user_id}")

    def get_all_users(self):
        return self.api_client.get("users")


class UserUpdater:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_user(self, user_data):
        return self.api_client.post("users", user_data)

    def update_user(self, user_id, user_data):
        return self.api_client.put(f"users/{user_id}", user_data)

    def delete_user(self, user_id):
        return self.api_client.delete(f"users/{user_id}")


class UserFacade:
    def __init__(self, api_client):
        self.auth = UserAuthentication(api_client)
        self.fetcher = UserFetcher(api_client)
        self.updater = UserUpdater(api_client)

    def login(self, credentials):
        return self.auth.login(credentials)

    def logout(self, user_id):
        return self.auth.logout(user_id)

    def create_user(self, user_data):
        return self.updater.create_user(user_data)

    def get_user(self, user_id):
        return self.fetcher.get_user(user_id)

    def get_all_users(self):
        return self.fetcher.get_all_users()

    def update_user(self, user_id, user_data):
        return self.updater.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.updater.delete_user(user_id)


if __name__ == "__main__":
    base_url = "https://example.com/api"
    api_client = APIClient(base_url)
    user_facade = UserFacade(api_client)

    credentials = {"username": "john_doe", "password": "password123"}
    print("Logging in...")
    login_response = user_facade.login(credentials)
    print("Login response:", login_response)

    new_user = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    print("\nCreating user...")
    created_user = user_facade.create_user(new_user)
    print("Created user:", created_user)

    user_id = created_user["id"]
    print("\nGetting user...")
    user_info = user_facade.get_user(user_id)
    print("User info:", user_info)

    updated_user = {"name": "Jane Smith", "email": "jane.smith@example.com"}
    print("\nUpdating user...")
    updated_user_info = user_facade.update_user(user_id, updated_user)
    print("Updated user info:", updated_user_info)

    print("\nGetting all users...")
    all_users = user_facade.get_all_users()
    print("All users:", all_users)
