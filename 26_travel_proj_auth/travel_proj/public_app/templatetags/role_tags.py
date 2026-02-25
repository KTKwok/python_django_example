from django import template
from public_app.models import UserInRole
register = template.Library()

@register.simple_tag(takes_context=True)
def has_role(context, *roles):
    request = context['request']

    if not request or not request.user.is_authenticated:
        return False

    uir = UserInRole.objects.filter(user=request.user)

    return any(role.role.role_code in roles for role in uir)