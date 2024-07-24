from abc import ABC, abstractmethod


class DataService(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def update_data(self, data):
        pass


class RealDataService(DataService):
    def __init__(self):
        self.data = "Sensitive data"

    def get_data(self):
        return self.data

    def update_data(self, data):
        self.data = data
        print("Data updated to:", self.data)


class AuthorizationProxy(DataService):
    def __init__(self, real_service: DataService, user_roles: dict):
        self._real_service = real_service
        self._user_roles = user_roles

    def get_data(self):
        if self._user_roles.get("read"):
            return self._real_service.get_data()
        else:
            raise PermissionError("User does not have read access")

    def update_data(self, data):
        if self._user_roles.get("write"):
            self._real_service.update_data(data)
        else:
            raise PermissionError("User does not have write access")


if __name__ == "__main__":
    real_service = RealDataService()

    user_roles_with_access = {"read": True, "write": True}
    user_roles_without_access = {"read": False, "write": False}

    proxy_with_access = AuthorizationProxy(real_service, user_roles_with_access)
    proxy_without_access = AuthorizationProxy(real_service, user_roles_without_access)

    try:
        print("Authorized user reading data:", proxy_with_access.get_data())
        proxy_with_access.update_data("New sensitive data")
    except PermissionError as e:
        print(e)

    try:
        print("Unauthorized user reading data:", proxy_without_access.get_data())
    except PermissionError as e:
        print(e)

    try:
        proxy_without_access.update_data("Another data")
    except PermissionError as e:
        print(e)
