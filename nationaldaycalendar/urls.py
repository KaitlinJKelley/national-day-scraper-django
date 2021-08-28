"""nationaldaycalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from nationaldays.views import YearViewSet, DayViewSet
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register("year", YearViewSet, "day_year")
router.register("month", DayViewSet, "day_month")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
