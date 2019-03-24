"""VueDjango_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from book import urls
from front import urls as fr_ur
from sqlcheck import urls as sql_ur
from rest_framework import routers
from framework_app import urls as rest_url
from framework_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls, namespace='book')),
    path('front/', include(fr_ur, namespace='front')),
    path('sqlcheck/', include(sql_ur, namespace='sqlcheck')),

    # framework-api
    path('api-rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
