from django.contrib import admin

from .models import SystemRole, UserInRole


# Register your models here.
@admin.register(SystemRole)
class SystemRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(UserInRole)
class UserInRoleAdmin(admin.ModelAdmin):
    pass