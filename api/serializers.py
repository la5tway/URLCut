from rest_framework import serializers

from .models import Client, UrlCut


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Client
        fields = '__all__'


class UrlCutSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlCut
        fields = '__all__'