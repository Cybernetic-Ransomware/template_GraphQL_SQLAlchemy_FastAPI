import strawberry

from app.graphql.resolvers import Query, Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)
