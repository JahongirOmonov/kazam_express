from django.urls import path
from kazam_express import views




urlpatterns = [
    #Shop
    path('shop-list/', views.ShopListApiView.as_view()),
    path('shop-filter-title/', views.ShopFilterTitle.as_view()),
    path('shop-detail-update/<int:pk>', views.ShopUpdateApiView.as_view()),
    path('shop-add-image/', views.ShopAddImageApiView.as_view()),

    #Product
    path('product-list/', views.ProductListApiView.as_view()),
    path('product-filter-id-title/', views.ProductFilterIdTitle.as_view()),
    path('product-update/<int:pk>', views.ProductUpdateApiView.as_view()),
    path('product-order/', views.ProductSortedListApiView.as_view()),
    path('product-filter-flag/', views.ProductFilterFlagListApiView.as_view()),
    path('product-filter-price-range/', views.ProductFilterPriceRange.as_view()),


    #Category
    path('category-list/', views.CategoryListApiView.as_view()),
    path('category-search-id-title-parent/', views.CategorySearchIdTitleParentApiView.as_view()),
    path('category-create/', views.CategoryCreateApiView.as_view()),
    path('category-path/<int:pk>', views.CategoryPathRetrieveApiView.as_view()),

]
