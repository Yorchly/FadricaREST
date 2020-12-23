from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from api.utils import check_token


class CheckTokenMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_token(request.GET.get("token", None)):
            return super(CheckTokenMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse(content=JSONRenderer().render({"message": "you have not permissions to use this API."}),
                                status=403, content_type="json")
