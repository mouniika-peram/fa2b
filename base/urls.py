from django.urls import path, include
from rest_framework.routers import DefaultRouter

from base.views import CustomAuthToken

from user.views import UserViewSet
from product.views import ProductViewset
from cart.views import CartViewset

from categoryQnA.views import CategoryQnAViewset
# Create a router and register our ViewSets with it.
from rest_framework.authtoken.views import obtain_auth_token

from categoryQnAExamples.views import show_examples

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'product', ProductViewset, basename='product')
router.register(r'cart', CartViewset, basename='cart')
router.register(r'categoryqna', CategoryQnAViewset, basename='categoryqna')



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('examples/', show_examples, name='show-examples'),




]