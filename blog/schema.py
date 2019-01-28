import graphene
from graphene_django.types import DjangoObjectType
from .models import Person, Post


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    all_persons = graphene.List(PersonType)

    def resolve_all_persons(self, info):
        return Person.objects.all()


class CreatePerson(graphene.Mutation):
    person = graphene.Field(PersonType)

    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        new_person = Person(**kwargs)
        new_person.save()

        return CreatePerson(new_person)


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
