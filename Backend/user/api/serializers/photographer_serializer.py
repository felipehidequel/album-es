from rest_framework import serializers

from user.models import Photographer


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = ['user', 'type_user', 'name_photographer', 'name_company']
        read_only_fields = ['id']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
