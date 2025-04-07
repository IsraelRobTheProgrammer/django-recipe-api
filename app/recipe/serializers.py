"""
Serializers for recipe apis.
"""

from core.models import Recipe
from rest_framework import serializers

# from django.utils.translation import gettext as _


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the recipes"""

    class Meta:
        model = Recipe
        # fields = ["id", "title", "time_minutes", ""]
        fields = ["id", "title", "time_minutes", "price", "link"]
        read_only_fields = ["id"]


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["desc"]
