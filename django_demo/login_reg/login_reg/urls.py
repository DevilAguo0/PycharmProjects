"""login_reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# """
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('/login_reg/login_reg/templates/index.html/', admin.site.urls),
    path('/login_reg/login_reg/templates/index.html/', login_reg.login.views.index),
    path('/login_reg/login_reg/templates/index.html/', login_reg.login.views.login),
    path('/login_reg/login_reg/templates/index.html/', login_reg.login.views.register),
]
