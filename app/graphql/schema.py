import strawberry

from app.graphql.resolvers import Query, Mutation, Subscription


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
