# from rest_framework.permissions import BasePermission
#
#
# class ProductAdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.roles == 1:
#             return True
#         return False
#
#
# class CategoryAdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.roles == 2:
#             return True
#         return False
#
#
# class ShopAdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.roles == 3:
#             return True
#         return False
