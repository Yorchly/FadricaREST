from api.models import Token


def get_qs(**kwargs):
    """
    Get one token filtered by arguments passed in **kwargs
    :param kwargs:
    :return:
    """
    return Token.objects.get(**kwargs)
