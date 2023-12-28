import redis
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

user1 = {
    "name": "Paul John",
    "email": "paul.john@example.com",
    "age": 42,
    "city": "London, Chennai, Akihabara, Fuyuki city"
}
user2 = {
    "name": "Eden Zamir",
    "email": "eden.zamir@example.com",
    "age": 29,
    "city": "Tel Aviv"
}
user3 = {
    "name": "Paul Zamir",
    "email": "paul.zamir@example.com",
    "age": 35,
    "city": "Tel Aviv"
}
search_schema = (
    TextField("$.name", as_name="name"), 
    TagField("$.city", as_name="city"), 
    NumericField("$.age", as_name="age")
)

r.json().set("user:1", Path.root_path(),  user1)
r.json().set("user:2", Path.root_path(),  user2)
r.json().set("user:3", Path.root_path(),  user3)

rs_user = r.ft("idx:users_comma")
rs_user.create_index(
        fields=search_schema, 
        definition=IndexDefinition(
            prefix=["user:"], 
            index_type=IndexType.JSON
            )
        )

rs_user.search(Query("Paul @age:[30 50]").return_field("$"))

req = aggregations.AggregateRequest("*").group_by("@city", reducers.count().alias("count"))
print(rs_user.aggregate(req).rows)


