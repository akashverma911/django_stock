from rest_framework import viewsets
from .serializers import CommonSerializer
from .models import Common


class CommonViewSet(viewsets.ModelViewSet):
    serializer_class = CommonSerializer
    queryset = Common.objects.all()
