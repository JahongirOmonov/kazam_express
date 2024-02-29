from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from kazam_express import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from kazam_express import permissions
from .admin import ProductAdminPermission, CategoryAdminPermission, ShopAdminPermission


class ShopListApiView(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, ShopAdminPermission)


class ShopFilterTitle(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, ShopAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('title',)
    filterset_fields = ('title',)


class ShopUpdateApiView(generics.UpdateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, ShopAdminPermission)


class ShopAddImageApiView(generics.CreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, ShopAdminPermission)






class ProductListApiView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)


class ProductFilterIdTitle(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('id', 'title')
    filterset_fields = ('id', 'title')


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)


class ProductSortedListApiView(generics.ListAPIView):
    queryset = models.Product.objects.all().order_by("price")
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)


class ProductFilterFlagListApiView(generics.ListAPIView):
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)


class ProductFilterPriceRange(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, ProductAdminPermission)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class CategoryListApiView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, CategoryAdminPermission)


class CategorySearchIdTitleParentApiView(generics.ListAPIView):
    queryset = models.Category.objects.all().filter(parent=None)
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, CategoryAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('id', 'title')
    filterset_fields = ('id', 'title')


class CategoryCreateApiView(generics.CreateAPIView):
    queryset = models.Category.objects.filter(parent=None)
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, CategoryAdminPermission)


class CategoryPathRetrieveApiView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryPathSerializer
    permission_classes = (IsAuthenticated, CategoryAdminPermission)


#>

class ProductImagesAliView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.Product2Serializer
    parser_classes = [MultiPartParser, FormParser]



    # def create(self, request, *args, **kwargs):
    #     instance_data = request.data
    #     data = {key: value for key, value in instance_data.items()}
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save()
    #
    #     if request.FILES:
    #         images = dict((request.FILES).lists()).get('photos', None)
    #         if images:
    #             for image in images:
    #                 image_data = {}
    #                 image_data["product"] = instance.pk
    #                 image_data["image"] = image
    #                 image_serializer = serializers.ImageqSerializer(data=image_data)
    #                 image_serializer.is_valid(raise_exception=True)
    #                 image_serializer.save()
    #     return Response(serializer.data)















