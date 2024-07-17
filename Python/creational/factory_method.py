from enum import Enum


class ApiType(Enum):
    INSTAGRAM = 1
    FACEBOOK = 2
    TWITTER = 3


class Api:
    def __init__(self, flags: str) -> None:
        self.__flags: str = flags

    def get_flags(self) -> str:
        return self.__flags


class InstagramApi(Api):
    def __init__(self) -> None:
        super().__init__("-f -s -d")


class FacebookApi(Api):
    def __init__(self) -> None:
        super().__init__("-f -s -d -t")


class TwitterApi(Api):
    def __init__(self) -> None:
        super().__init__("-f -s -d -t -w")


def create_api(api_type: ApiType) -> Api:
    api_factory = {
        ApiType.INSTAGRAM: InstagramApi,
        ApiType.FACEBOOK: FacebookApi,
        ApiType.TWITTER: TwitterApi,
    }
    return api_factory[api_type]()


if __name__ == "__main__":
    for api_type in ApiType:
        api = create_api(api_type)
        print(api.get_flags())
