from django.utils import translation
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin as BaseMiddleware


class LocaleMiddleware(BaseMiddleware):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def process_request(cls, request):
        translation.activate(translation.get_language_from_request(request))
        request.LANGUAGE_CODE = translation.get_language()

    @classmethod
    def process_response(cls, request, response):
        patch_vary_headers(response, ("Accept-Language",))
        response["Content-Language"] = translation.get_language()
        translation.deactivate()
        return response
