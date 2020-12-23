from api.models import Token
from api.services.token import get_qs


def check_token(token):
    """
    Check if token passed as argument is registered in database
    :param token:
    :type token: str
    :return:
    """
    try:
        get_qs(token=token)
        return True
    except Token.DoesNotExist:
        return False
