"""Bazi_proekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, re_path

from online_shop import views
from online_shop.views import kategorii, umetnickiDela, naracki, avtori, dodadiKategorija, home, deleteCategory, \
    dodadiUmetnickoDelo, dodadiNaracka, Register, loginPage, login_view, login, korisnici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('kategorii/', kategorii, name="kategorii"),
    path('korisnici/', korisnici, name="korisnici"),
    path('umetnickiDela/', umetnickiDela, name="umetnickiDela"),
    path('naracki/', naracki, name="naracki"),
    path('avtori/', avtori, name="avtori"),
    path('dodadiKategorija/', dodadiKategorija, name="dodadiKategorija"),
    path('dodadiUmetnickoDelo/', dodadiUmetnickoDelo, name="dodadiUmetnickoDelo"),
    path('login/', login, name="login"),
    path('dodadiNaracka/', dodadiNaracka, name="dodadiNaracka"),
    path('register/', Register, name="register"),
    path('deleteCategory/<int:id_na_kategorija>/', deleteCategory, name="deleteCategory"),



]
