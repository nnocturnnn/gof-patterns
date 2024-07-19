from abc import ABC, abstractmethod

class RequestHandler(ABC):
    @abstractmethod
    def handle(self, request):
        pass

class BaseRequestHandler(RequestHandler):
    def handle(self, request):
        print("Handling request:", request)

class HandlerDecorator(RequestHandler):
    def __init__(self, wrapped_handler: RequestHandler):
        self._wrapped_handler = wrapped_handler

    def handle(self, request):
        self._wrapped_handler.handle(request)

class LoggingDecorator(HandlerDecorator):
    def handle(self, request):
        print(f"Logging request: {request}")
        super().handle(request)

class AuthenticationDecorator(HandlerDecorator):
    def handle(self, request):
        if self.authenticate(request):
            print("Authentication successful")
            super().handle(request)
        else:
            print("Authentication failed")

    def authenticate(self, request):
        return request.get("authenticated", False)

class CachingDecorator(HandlerDecorator):
    def __init__(self, wrapped_handler: RequestHandler):
        super().__init__(wrapped_handler)
        self._cache = {}

    def handle(self, request):
        if request in self._cache:
            print(f"Cache hit for request: {request}")
            print(f"Cache response: {self._cache[request]}")
        else:
            print(f"Cache miss for request: {request}")
            response = self._wrapped_handler.handle(request)
            self._cache[request] = response
            return response

if __name__ == "__main__":
    request = {"url": "/api/data", "authenticated": True}
    base_handler = BaseRequestHandler()
    logging_handler = LoggingDecorator(base_handler)
    auth_handler = AuthenticationDecorator(logging_handler)
    caching_handler = CachingDecorator(auth_handler)
    caching_handler.handle(request)