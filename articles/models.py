from django.db import models
from users.models import User

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.title)
