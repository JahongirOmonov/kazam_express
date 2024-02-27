from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (3, 'Shop admin'),
        (2, 'Category admin'),
        (1, 'Product admin'),
    )

    roles = models.PositiveIntegerField(choices=CHOICE_ROLES, default=1)

    def __str__(self):
        return self.username
