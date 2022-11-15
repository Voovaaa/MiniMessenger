from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    contacts = models.ManyToManyField("self")


class Dialog(models.Model):
    user1 = models.ForeignKey("User", related_name="users1", on_delete=models.CASCADE)
    user2 = models.ForeignKey("User", related_name="users2", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user1", "user2")


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    dialog = models.ForeignKey(to=Dialog, on_delete=models.CASCADE)
