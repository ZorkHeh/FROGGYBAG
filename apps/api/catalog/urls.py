from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ImageViewSet, CategoryViewSet

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view())
]

router = DefaultRouter()
router.register('product/image', ImageViewSet, basename='product_image')
router.register('category', CategoryViewSet, basename='category')

urlpatterns += router.urls
