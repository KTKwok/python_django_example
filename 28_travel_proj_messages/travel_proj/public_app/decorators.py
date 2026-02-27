from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .models import UserInRole

def unauthenticated_user_only(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("You are not allowed to view this page.")
        return view(request, *args, **kwargs)
    return wrapper

def allowed_user(allowed_roles=[]):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            uir = UserInRole.objects.filter(user=request.user)

            for u in uir:
                if u.role.role_code in allowed_roles:
                    return view(request, *args, **kwargs)

            return HttpResponse("You are not allowed to view this page.")
        return wrapper
    return decorator

class AllowedUserMixin(AccessMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        uir = UserInRole.objects.filter(user=request.user)

        if not any(role.role.role_code in self.allowed_roles for role in uir):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)