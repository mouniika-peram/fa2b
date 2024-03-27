from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

from product.views import ProductViewset
# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'product', ProductViewset, basename='product')



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]