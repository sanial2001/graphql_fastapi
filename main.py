from fastapi import FastAPI
from schema import schema
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

app = FastAPI()


@app.get('/')
def func():
    return {"Hello": "Everyone"}


app.mount('/graphql', GraphQLApp(schema=schema, on_get=make_graphiql_handler()))
