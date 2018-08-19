from django.db import models
from django.conf import settings

SYSTEM_CHOICES = (
    ('4E', 'D&D 4th'),
    ('5E', 'D&D 5th'),
    ('BIND', 'Blades in the Dark'),
    ('DW', 'Dungeon World'),
)


class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    system = models.CharField(max_length=16, choices=SYSTEM_CHOICES, default='5E')


class Folder(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    order = models.PositiveIntegerField


class Item(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    description = models.TextField(null='true')
