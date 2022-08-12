from django.urls import path,include
from rest_framework import routers
from cinomeapp import views

router = routers.DefaultRouter()
router.register(r'test', views.TestView, 'test')

urlpatterns = [
    path('api/', include(router.urls))
]