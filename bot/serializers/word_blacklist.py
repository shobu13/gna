from rest_framework import serializers

from bot.models import WordBlackList, Role


class WordBlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordBlackList
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
