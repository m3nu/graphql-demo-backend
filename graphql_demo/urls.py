from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from graphene_django.views import GraphQLView

import graphql_demo.schema

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=graphql_demo.schema.schema)),
]
