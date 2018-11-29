from django.db.models import QuerySet
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework import mixins

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings

from bot.models import WordBlackList, Role
from bot.serializers.word_blacklist import WordBlackListSerializer, RoleSerializer


# Create your viewsets here.

class MultiSerializerViewSet(viewsets.GenericViewSet):
    """
    MultiSerializerViewSet est une class custom permettant l'usage de plusieurs serializer
    en fonction de l'action.
    Elle permet aussi de sélectionner les permissions à accorder en fonction de l'action.
    """
    serializers = {
        'default': None,
    }

    permission_classes = {
        'default': api_settings.DEFAULT_PERMISSION_CLASSES
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])

    def get_permissions(self):
        permission_list = self.permission_classes.get(self.action,
                                                      self.permission_classes['default'])
        return [permission() for permission in permission_list]


class WordBlackListViewset(MultiSerializerViewSet):
    """
    Viewset utilisé pour récupérer les blacklists

    list:
    Renvoie la première blacklist
    """
    queryset = WordBlackList.objects.all()

    permission_classes = {
        'default': (permissions.AllowAny,),
    }

    serializers = {
        'default': WordBlackListSerializer,
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        assert isinstance(queryset, QuerySet)
        serializer = self.get_serializer(queryset.last(), many=False)
        return Response(serializer.data)


class RoleViewset(MultiSerializerViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    """
    Viewset utilisé pour gérer les roles du serveur.

    list:
    renvoie la liste de tout les role enregistrer.
    create:
    permet de créer un role, prend un identifiant et un nom.
    destroy:
    permet de supprimer un role
    partial_update:
    Permet de mettre à jour la totalitée ou une partie d'un role, prend en parametre un identifiant
    et/ou un nom.
    """
    queryset = Role.objects.all()
    permission_classes = {
        'default': (permissions.AllowAny, ),
        'create': (permissions.IsAdminUser, ),
        'destroy': (permissions.IsAdminUser,),
        'update': (permissions.IsAdminUser,),
        'partial_update': (permissions.IsAdminUser, ),
    }
    serializers = {
        'default': RoleSerializer,
    }

    @action(methods=['get'], detail=False)
    def get_default(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        assert isinstance(queryset, QuerySet)
        serializer = self.get_serializer(queryset.get(is_default=True))
        return Response(serializer.data)
