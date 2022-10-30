from rest_framework import serializers
from userscrud.models import UsersCrud

class UsersCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsersCrud
        fields=(
            'id', 
            'first_name', 
            'last_name', 
            'document',
            'age', 
            'address', 
            'email', 
            'phone_number', 
            'profession', 
            'created_at'
            )
        read_only_fields=('created_at', )
