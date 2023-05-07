from graphene import ObjectType, String, Int, List, Schema
from models import data


class PersonType(ObjectType):
    first_name = String()
    last_name = String()
    email = String()
    age = Int()

    def resolve_first_name(self, info):
        return self.first_name

    def resolve_last_name(self, info):
        return self.last_name

    def resolve_email(self, info):
        return self.email

    def resolve_age(self, info):
        return self.age


class Query(ObjectType):
    all_people = List(PersonType)

    def resolve_all_people(self, info):
        return data.values()


schema = Schema(query=Query)

# query_string = "{allPeople{email lastName firstName}}"
# print(schema.execute(query_string))
