from enum import Enum


class ApiType(Enum):
    INSTAGRAM = 1
    FACEBOOK = 2
    TWITTER = 3


class Api:
    def __init__(self, flags):
        self.__flags = flags

    def get_flags(self):
        return self.__flags


class InstagramApi(Api):
    def __init__(self):
        super().__init__("-f -s -d")


class FacebookApi(Api):
    def __init__(self):
        super().__init__("-f -s -d -t")


class TwitterApi(Api):
    def __init__(self):
        super().__init__("-f -s -d -t -w")


def create_api(api_type: ApiType) -> Api:
    api_factory = {
        ApiType.INSTAGRAM: InstagramApi,
        ApiType.FACEBOOK: FacebookApi,
        ApiType.TWITTER: TwitterApi,
    }
    return api_factory[api_type]()


if __name__ == "__main__":
    for i in ApiType:
        api = create_api(i)
        print(api.get_flags())
