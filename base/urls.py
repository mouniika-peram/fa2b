from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]