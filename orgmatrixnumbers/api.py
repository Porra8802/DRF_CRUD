from orgmatrixnumbers.models import OrgMatrixNumbers
from rest_framework import viewsets, permissions
from orgmatrixnumbers.serializers import OrgMatrixNumbersSerializer

class OrgMatrixNumbersViewSet(viewsets.ModelViewSet):
    queryset=OrgMatrixNumbers.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=OrgMatrixNumbersSerializer