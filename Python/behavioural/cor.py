
class Middleware:
    def __init__(self):
        self.next = None

    def set_next(self, middleware):
        self.next = middleware
        return middleware

    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return request


class AuthMiddleware(Middleware):
    def handle(self, request):
        if not request.get('is_authenticated', False):
            raise Exception("Unauthorized")
        print("Аутентификация успешна")
        return super().handle(request)

class LoggerMiddleware(Middleware):
    def handle(self, request):
        print(f"URL запроса: {request.get('url')}")
        return super().handle(request)

class RequestProcessorMiddleware(Middleware):
    def handle(self, request):
        print("Обработка запроса...")
        request['processed'] = True
        return super().handle(request)

if __name__ == "__main__":
    auth = AuthMiddleware()
    logger = LoggerMiddleware()
    processor = RequestProcessorMiddleware()

    auth.set_next(logger).set_next(processor)

    request = {
        'url': '/api/data',
        'is_authenticated': True,
        'processed': False
    }

    try:
        auth.handle(request)
        print("Запрос успешно обработан:", request)
    except Exception as error:
        print(error)
