from abc import ABCMeta, abstractmethod
from typing import Optional


class API:
    def __init__(self) -> None:
        self.__endpoint: Optional[str] = None
        self.__headers: Optional[str] = None
        self.__documentation: Optional[str] = None

    def set_endpoint(self, endpoint: str) -> None:
        self.__endpoint = endpoint

    def set_headers(self, headers: str) -> None:
        self.__headers = headers

    def set_documentation(self, documentation: str) -> None:
        self.__documentation = documentation

    def get_api(self) -> str:
        return f"API: {self.__endpoint}, {self.__headers}, {self.__documentation}"


class IDeveloper(metaclass=ABCMeta):
    @abstractmethod
    def create_endpoint(self) -> None:
        pass

    @abstractmethod
    def create_headers(self) -> None:
        pass

    @abstractmethod
    def create_documentation(self) -> None:
        pass

    @abstractmethod
    def get_api(self) -> API:
        pass


class RESTDeveloper(IDeveloper):
    def __init__(self) -> None:
        self.__api = API()

    def create_endpoint(self) -> None:
        self.__api.set_endpoint("REST endpoint")

    def create_headers(self) -> None:
        self.__api.set_headers("REST headers")

    def create_documentation(self) -> None:
        self.__api.set_documentation("REST documentation")

    def get_api(self) -> API:
        return self.__api


class SOAPDeveloper(IDeveloper):
    def __init__(self) -> None:
        self.__api = API()

    def create_endpoint(self) -> None:
        self.__api.set_endpoint("SOAP endpoint")

    def create_headers(self) -> None:
        self.__api.set_headers("SOAP headers")

    def create_documentation(self) -> None:
        self.__api.set_documentation("SOAP documentation")

    def get_api(self) -> API:
        return self.__api


class APIBuilder:
    def __init__(self, developer: IDeveloper) -> None:
        self.__developer: IDeveloper = developer

    def set_developer(self, developer: IDeveloper) -> None:
        self.__developer = developer

    def create_full_api(self) -> API:
        self.__developer.create_endpoint()
        self.__developer.create_headers()
        self.__developer.create_documentation()
        return self.__developer.get_api()

    def create_api(self) -> API:
        self.__developer.create_endpoint()
        self.__developer.create_headers()
        return self.__developer.get_api()


if __name__ == "__main__":
    rest_developer = RESTDeveloper()
    soap_developer = SOAPDeveloper()

    api_builder = APIBuilder(rest_developer)
    api = api_builder.create_full_api()
    print(api.get_api())
