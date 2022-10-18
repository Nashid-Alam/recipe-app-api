from rest_framework import serializers
from core.models import Recipe,Ingredient




class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'time_minutes',
            'price', 'link'
        )
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields 



