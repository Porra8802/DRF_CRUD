from rest_framework import serializers
from orgmatrixnumbers.models import OrgMatrixNumbers

class OrgMatrixNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrgMatrixNumbers
        fields=(
            'sin_clasificar',
            'clasificado',
            
        )
    
