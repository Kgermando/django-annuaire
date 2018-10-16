from django.db import models
import datetime
from django.db.models import Q

from .contants import STATES


# Create your models here.


class PostQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(Q(societe__icontains=query) | ~Q(name__icontains=query) |
                               Q(ville__iexact=query) |
                               Q(quartier__icontains=query) |
                               Q(commune__icontains=query) |
                               Q(ville__icontains=query) |
                               Q(province__iexact=query) |
                               Q(site_web__icontains=query)
                               ).distinct()  # distinct() is often necessary with Q lookups
        return self


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Post(models.Model):
    name = models.CharField(max_length=300)
    societe = models.CharField(max_length=300)
    number_1 = models.CharField(max_length=15)
    number_2 = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    adresse = models.TextField(blank=True, unique=True)
    quartier = models.CharField(max_length=300, blank=True)
    commune = models.CharField(max_length=120, blank=True)
    ville = models.CharField(max_length=300)
    province = models.CharField(choices=STATES, max_length=300, blank=True)
    secteur_1 = models.CharField(max_length=300, blank=True)
    secteur_2 = models.CharField(max_length=300, blank=True)
    site_web = models.CharField(max_length=300, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now)

    objects = PostManager()

    def __str__(self):
        return self.societe

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('details', args=[str(self.id)])
