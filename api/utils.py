from api.models import Token


def check_token(token):
    try:
        Token.objects.get(token=token)
        return True
    except Token.DoesNotExist:
        return False
