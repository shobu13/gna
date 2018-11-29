from django.db import models
from django.db.models.signals import pre_save


class WordBlackList(models.Model):
    """
    Cette classe définie les mots banni des messages discord, les mots sont séparer par un point
    virgule.
    """
    words = models.TextField()

    def __str__(self):
        return self.words[:100]


class Role(models.Model):
    """
    Cette classe définie les rôles du serveur
    id : identifiant du role
    name : nom du role
    """

    identifiant = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name
