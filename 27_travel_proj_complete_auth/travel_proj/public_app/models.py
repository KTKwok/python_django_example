from django.contrib.auth.models import User
from django.db import models


class SystemRole(models.Model):
    role_code  = models.CharField(max_length=10, unique=True)
    role_name = models.TextField()

    def __str__(self):
        return self.role_name

class UserInRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(SystemRole, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='I am so smart')
    avatar = models.ImageField(blank=True, null=True, upload_to='img/avatar')

    def __str__(self):
        return f"{self.user.username}"