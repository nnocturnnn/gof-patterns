from abc import ABCMeta, abstractmethod

class API:
    def __init__(self):
        self.__endpoint = None
        self.__headers = None
        self.__documentation = None

    def set_endpoint(self, endpoint):
        self.__endpoint = endpoint

    def set_headers(self, headers):
        self.__headers = headers

    def set_documentation(self, documentation):
        self.__documentation = documentation

    def get_api(self):
        return f"API: {self.__endpoint}, {self.__headers}, {self.__documentation}"

class IDeveloper(metaclass=ABCMeta):
    @abstractmethod
    def create_endpoint(self):
        pass

    @abstractmethod
    def create_headers(self):
        pass

    @abstractmethod
    def create_documentation(self):
        pass

    @abstractmethod
    def get_api(self):
        pass

class RESTDeveloper(IDeveloper):
    def __init__(self):
        self.__api = API()

    def create_endpoint(self):
        self.__api.set_endpoint("REST endpoint")

    def create_headers(self):
        self.__api.set_headers("REST headers")

    def create_documentation(self):
        self.__api.set_documentation("REST documentation")

    def get_api(self):
        return self.__api

class SOAPDeveloper(IDeveloper):
    def __init__(self):
        self.__api = API()

    def create_endpoint(self):
        self.__api.set_endpoint("SOAP endpoint")

    def create_headers(self):
        self.__api.set_headers("SOAP headers")

    def create_documentation(self):
        self.__api.set_documentation("SOAP documentation")

    def get_api(self):
        return self.__api

class APIBuilder:
    def __init__(self, developer):
        self.__developer = developer

    def set_developer(self, developer):
        self.__developer = developer

    def create_full_api(self):
        self.__developer.create_endpoint()
        self.__developer.create_headers()
        self.__developer.create_documentation()
        return self.__developer.get_api()

    def create_api(self):
        self.__developer.create_endpoint()
        self.__developer.create_headers()
        return self.__developer.get_api()

if __name__ == "__main__":
    rest_developer = RESTDeveloper()
    soap_developer = SOAPDeveloper()

    api_builder = APIBuilder(rest_developer)
    api = api_builder.create_full_api()
    print(api.get_api())
