from rest_framework import serializers
from kazam_express import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = (
            'id',
            'title',
            'description',
            'imageUrl'
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'id',
            'image'
        )


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.title')
    # images = ImageSerializer(many=True, read_only=True)

    main_photo = serializers.SerializerMethodField()

    def get_main_photo(self, xx):
        if xx.main_photo:
            return xx.main_photo.name
        else:
            photo = xx.images.first()
            if photo:
                return photo.image.name
            else:
                return None

    class Meta:
        model = models.Product
        fields = (
            'id',
            'title',
            'description',
            'amount',
            'price',
            'active',
            'category',
            'main_photo',
        )


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(source='parent.title')
    shop = serializers.StringRelatedField(source='shop.title')

    class Meta:
        model = models.Category
        fields = (
            'id',
            'title',
            'description',
            'shop',
            'parent'
        )


class CategoryPathSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(source='parent.title')
    shop = serializers.StringRelatedField(source='shop.title')
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = (
            'id',
            'title',
            'description',
            'shop',
            'parent',
            'products'
        )
