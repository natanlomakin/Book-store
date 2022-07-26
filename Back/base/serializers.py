from rest_framework import serializers
from .models import AllBooks
 
class APIsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllBooks # Table
        fields=['image'] # ['title','content','image']
