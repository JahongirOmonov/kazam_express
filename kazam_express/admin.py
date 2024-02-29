from django.contrib import admin
from django.apps import apps
from kazam_express import models
from account.models import SHOP_ADMIN, CATEGORY_ADMIN, PRODUCT_ADMIN


class Photos(admin.TabularInline):
    fk_name = 'product'
    model = models.Image
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'main_photo', "amount", "price", "category")
    inlines = [Photos]
    list_display_links = ("title", "amount", "price")
    actions = ("make_one", )
    list_per_page = 5
    search_fields = ("title", "price")
    list_select_related = ("category", )




    def make_one(self, request, queryset):
        queryset.update(amount=19)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'shop', 'parent')
    list_display_links = ('id', 'title', 'description', 'shop', 'parent')
    actions = ("change",)

    def change(self, request, queryset):
        queryset.update(description="wonderful")

@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'imageUrl')
    list_display_links = ('id', 'title', 'description', 'imageUrl')
    actions = ("change",)

    def change(self, request, queryset):
        queryset.update(description="nice")

from rest_framework.permissions import BasePermission
class ProductAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == PRODUCT_ADMIN:
            return True
        return False

# admin.site.register(ProductAdminPermission)

class CategoryAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == CATEGORY_ADMIN:
            return True
        return False

# admin.site.register(CategoryAdminPermission)

class ShopAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == SHOP_ADMIN:
            return True
        return False

# admin.site.register(ShopAdminPermission)













models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
