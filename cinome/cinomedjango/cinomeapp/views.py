from .serializers import TestSerializer
from rest_framework import viewsets
from .models import Test

class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()