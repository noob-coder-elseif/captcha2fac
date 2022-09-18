from enum import Enum

class Group(Enum):
    admin = "Administrator"
    manager = "Manager"


from django.http import Http404
# from .constants import Group

def check_user_able_to_see_page(*groups: Group):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(
                name__in=[group.name for group in groups]
            ).exists():
                return function(request, *args, **kwargs)
            raise Http404

        return wrapper

    return decorator


@check_user_able_to_see_page(Group.admin)
def hidden_page(request):
    pass