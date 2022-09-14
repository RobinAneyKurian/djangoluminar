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
from api.views import Findcube, Numcheck, Numfactorial, Wordcount, Palindrome, Armstrong, Primenumber

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube', Findcube.as_view()),
    path('numcheck', Numcheck.as_view()),
    path('factorial', Numfactorial.as_view()),
    path('wordcount', Wordcount.as_view()),
    path("palindrome", Palindrome.as_view()),
    path("armstrong", Armstrong.as_view()),
    path("primenumber", Primenumber.as_view())
    # path('products/', ProductsView.as_view()),
    # path('greetings/', Greetings.as_view()),
    # path('add/', Add.as_view()),
    # path('addnumbers/', AddView.as_view()),
]
