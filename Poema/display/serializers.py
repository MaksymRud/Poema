from rest_framework import serializers
from display.models import *

class PoemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poem
        exclude = ['id']
        
class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        exclude = ['id']
        
    