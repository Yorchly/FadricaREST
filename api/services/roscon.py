from api.models import Roscon


def get_qs(**kwargs):
    """
    Get one roscon filtered by arguments passed in **kwargs
    :param kwargs:
    :return:
    """
    return Roscon.objects.get(**kwargs)


def filter_qs(limit=None, **kwargs):
    """
    Get roscones filtered by arguments passed in **kwargs
    :param limit:
    :param kwargs:
    :return:
    """
    return Roscon.objects.filter(**kwargs)[:limit]
