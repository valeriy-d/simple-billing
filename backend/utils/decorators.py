import json
from functools import wraps

from django.http.response import JsonResponse


def json_required(func):
    """
    Декоратор проверяет что полученные данные в формате json
    записывает в request.json
    иначе возвращает 400 ошибку
    """
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            request.json = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            return JsonResponse(
                {"error": "JSON Data required"},
                status=400
            )

        return func(self, request, *args, **kwargs)
    return wrapper
