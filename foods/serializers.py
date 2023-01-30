# snippets/serializers
from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('name', 'description', 'flavor', 'owner',
                  'created_at', 'updated_at',)

