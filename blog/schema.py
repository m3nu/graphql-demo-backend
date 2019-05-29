import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth import authenticate, login
from .models import Person, Post

# Type Definitions

class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class PostType(DjangoObjectType):
    class Meta:
        model = Post


# Queries

class Query(graphene.ObjectType):
    all_persons = graphene.List(PersonType)
    all_posts = graphene.List(PostType)

    def resolve_all_persons(self, info):
        return Person.objects.all()

    def resolve_all_posts(self, info):
        return Post.objects.all()


# Mutations

class Login(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **input):
        user = authenticate(username=input['username'], password=input['password'])
        if user is not None:
            login(info.context, user)
            return Login(True)
        else:
            raise Exception('Invalid username or password!')


class CreatePerson(graphene.Mutation):
    person = graphene.Field(PersonType)

    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception('Please authenticate first.')

        new_person = Person(**kwargs)
        new_person.save()
        return CreatePerson(new_person)


class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String(required=True)
        author = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        new_post = Post(
            title=kwargs['title'],
            author=Person.objects.get(pk=kwargs['author'])
        )
        new_post.save()

        return CreatePost(new_post)


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    create_post = CreatePost.Field()
    login = Login.Field()
