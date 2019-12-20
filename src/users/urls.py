"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from user_data.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('home/', home_view,name='home-view'),
    path('user/create/', user_create_view,name='create-view'),
    path('user/list/',user_list_view,name='list-view'),
    path('user/details/<int:user_id>/',user_details_view),
    path('user/details/<int:user_delete_id>/delete_user/',user_delete_view, name='delete-view'),
    path('user/details/<int:user_update_id>/update_user/',user_update_view, name='update-view')
]
