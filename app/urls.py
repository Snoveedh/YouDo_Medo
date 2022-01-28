"""YouDo_MeDo URL Configuration

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
from django.urls import path
from .views import home, signUp, login, add_youdo, signout, delete_youdo, change_status

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login' ),
    path('signup/', signUp, name='signup' ),
    path('add-youdo/', add_youdo, name='add-youdo' ),
    path('logout/', signout, name='logout' ),
    path('delete-youdo/<int:id>', delete_youdo, name='delete-youdo' ),
    path('change-status/<int:id>/<str:status>', change_status, name='change-status' ),
]
