from graphene_django import DjangoObjectType
from . import models


class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site


class BenefitsType(DjangoObjectType):
    class Meta:
        model = models.Benefits


class MenuType(DjangoObjectType):
    class Meta:
        model = models.Menu
