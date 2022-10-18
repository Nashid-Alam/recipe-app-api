from multiprocessing import AuthenticationError
from requests import request
from asyncio import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe,Ingredient

from recipe import serializer


# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializer.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""

        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializer.RecipeDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class IngredientViewSet(mixins.DestroyModelMixin,   
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin, 
                        viewsets.GenericViewSet):
    serializer_class = serializer.IngredientSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')





