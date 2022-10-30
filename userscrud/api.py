from .models import UsersCrud
from rest_framework import viewsets, permissions
from .serializers import UsersCrudSerializer

class UserCrudViewSet(viewsets.ModelViewSet):
    queryset=UsersCrud.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=UsersCrudSerializer

