from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from cinomeapp import views

router = routers.DefaultRouter()
router.register(r'test', views.TestView, 'test')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]