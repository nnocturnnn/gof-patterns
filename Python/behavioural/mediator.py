class Middleware:
    def __init__(self):
        self._next_middleware = None

    def link_with(self, next_middleware):
        self._next_middleware = next_middleware
        return next_middleware

    def check(self, request):
        if self._next_middleware:
            return self._next_middleware.check(request)
        return True


class AuthMiddleware(Middleware):
    def check(self, request):
        if not request.get("authenticated"):
            print("Authentication failed")
            return False
        print("Authentication passed")
        return super().check(request)


class ValidationMiddleware(Middleware):
    def check(self, request):
        if "data" not in request:
            print("Validation failed")
            return False
        print("Validation passed")
        return super().check(request)


class LoggingMiddleware(Middleware):
    def check(self, request):
        print(f"Logging request: {request}")
        return super().check(request)


# Example usage
logging_middleware = LoggingMiddleware()
validation_middleware = ValidationMiddleware()
auth_middleware = AuthMiddleware()

auth_middleware.link_with(validation_middleware).link_with(logging_middleware)

request = {"authenticated": True, "data": "Some request data"}

if auth_middleware.check(request):
    print("Request processed successfully")
else:
    print("Request processing failed")
