from django.db import models

# Create your models here.

from utils.models import BaseModel


class Shop(BaseModel):
    title = models.CharField(max_length=31)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=31)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    main_photo = models.ImageField(upload_to='images/', blank=True, null=True,
                                   editable=False)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=31)
    description = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             related_name='categories', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title


class Image(BaseModel):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_main:
            self.product.main_photo = self.image
            self.product.save()
        # self.is_main = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.image}"
