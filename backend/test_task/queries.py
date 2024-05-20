import graphene
from . import models
from . import types


class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)
    all_benefits = graphene.List(types.BenefitsType)
    all_menu = graphene.List(types.MenuType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )

    def resolve_all_benefits(root, info):
        return (
            models.Benefits.objects.all()
        )

    def resolve_all_menu(root, info):
        return (
            models.Menu.objects.all()
        )
