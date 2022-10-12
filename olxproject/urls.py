"""olxproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import ProductsView
# from api.views import Greetings, Add, AddView
from api.views import Findcube, Numcheck, Numfactorial, Wordcount, Palindrome, Armstrong, Primenumber, Products, ProductDetailsView

from api.views import ReviewView, ReviewDetails, ProductsViewSetView, ProductModelViewSet, ReviewsModelViewSet, UserSerializer


#Import defualt to map ViewSet views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("api/v1/products", ProductsViewSetView, basename="products")
router.register("api/v2/products", ProductModelViewSet, basename="items")
router.register("api/v3/reviews", ReviewsModelViewSet, basename="reviews")

#Token
from rest_framework.authtoken.views import ObtainAuthToken

# Password
router.register("register", UserSerializer, basename="user")

# Import simple JWT

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products', Products.as_view()),
    path('products/<int:pk>', ProductDetailsView.as_view()),
    path("reviews", ReviewView.as_view()),
    path("reviews/<int:pk>", ReviewDetails.as_view()),
    # path("token/", ObtainAuthToken.as_view())

    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view())

      # path('cube', Findcube.as_view()),
      # path('numcheck', Numcheck.as_view()),
      # path('factorial', Numfactorial.as_view()),
      # path('wordcount', Wordcount.as_view()),
      # path("palindrome", Palindrome.as_view()),
      # path("armstrong", Armstrong.as_view()),
      # path("primenumber", Primenumber.as_view()),
    # path('products/', ProductsView.as_view()),
    # path('greetings/', Greetings.as_view()),
    # path('add/', Add.as_view()),
    # path('addnumbers/', AddView.as_view()),

] + router.urls
