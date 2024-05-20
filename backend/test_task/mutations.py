import graphene
from . import models, types


class CreateBenefits(graphene.Mutation):
    benefit = graphene.Field(types.BenefitsType)

    class Arguments:
        top_text = graphene.String(required=True)
        integer = graphene.String(required=True)
        bot_text = graphene.String(required=True)
        slug = graphene.String(required=True)

    def mutate(self, info, top_text, integer, bot_text, slug):

        benefit = models.Benefits(
            top_text=top_text,
            integer=integer,
            bot_text=bot_text,
            slug=slug
        )
        benefit.save()

        return CreateBenefits(benefit=benefit)


class CreateMenu(graphene.Mutation):
    menu = graphene.Field(types.BenefitsType)

    class Arguments:
        text = graphene.String(required=True)
        slug = graphene.String(required=True)

    def mutate(self, info, text, slug):

        menu = models.Benefits(
            text=text,
            slug=slug
        )
        menu.save()

        return CreateMenu(menu=menu)
