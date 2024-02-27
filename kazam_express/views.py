from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from kazam_express import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from kazam_express import permissions


class ShopListApiView(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, permissions.ShopAdminPermission)


class ShopFilterTitle(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, permissions.ShopAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('title',)
    filterset_fields = ('title',)


class ShopUpdateApiView(generics.UpdateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, permissions.ShopAdminPermission)


class ShopAddImageApiView(generics.CreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAuthenticated, permissions.ShopAdminPermission)


class ProductListApiView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)


class ProductFilterIdTitle(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('id', 'title')
    filterset_fields = ('id', 'title')


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)


class ProductSortedListApiView(generics.ListAPIView):
    queryset = models.Product.objects.all().order_by("price")
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)


class ProductFilterFlagListApiView(generics.ListAPIView):
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)


class ProductFilterPriceRange(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated, permissions.ProductAdminPermission)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class CategoryListApiView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, permissions.CategoryAdminPermission)


class CategorySearchIdTitleParentApiView(generics.ListAPIView):
    queryset = models.Category.objects.all().filter(parent=None)
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, permissions.CategoryAdminPermission)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('id', 'title')
    filterset_fields = ('id', 'title')


class CategoryCreateApiView(generics.CreateAPIView):
    queryset = models.Category.objects.filter(parent=None)
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, permissions.CategoryAdminPermission)


class CategoryPathRetrieveApiView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryPathSerializer
    permission_classes = (IsAuthenticated, permissions.CategoryAdminPermission)
