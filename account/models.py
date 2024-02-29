from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# SHOP_ADMIN = 3
# CATEGORY_ADMIN = 2
# PRODUCT_ADMIN = 1
SHOP_ADMIN, CATEGORY_ADMIN, PRODUCT_ADMIN = (3, 2, 1, )


class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (SHOP_ADMIN, 'Shop admin'),
        (CATEGORY_ADMIN, 'Category admin'),
        (PRODUCT_ADMIN, 'Product admin'),
    )

    roles = models.PositiveIntegerField(choices=CHOICE_ROLES, default=1)

    def __str__(self):
        return self.username
