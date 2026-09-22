from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response

class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """ Клиент для публичных методов API пользователей.

        Предназначен для работы с эндпоинтами, которые не требуют авторизации,
        например — создание пользователя.

        Наследуется от APIClient и использует общий HTTP-клиент
        для выполнения запросов.
    """
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """  Метод создает нового пользователя.

        :param request: словарь с CreateUserRequest
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/users", json=request)