from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

import graphql_demo.schema

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=graphql_demo.schema.schema))),
]
