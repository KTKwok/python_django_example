from django.contrib import admin
from django.contrib.auth.models import User

from .models import SystemRole, UserInRole, UserProfile


# Register your models here.
@admin.register(SystemRole)
class SystemRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(UserInRole)
class UserInRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass