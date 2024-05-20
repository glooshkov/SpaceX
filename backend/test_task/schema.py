import graphene
from . import queries, mutations

schema = graphene.Schema(query=queries.Query, auto_camelcase=False)