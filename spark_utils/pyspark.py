import json
from pathlib import Path 

import redis
from redis.commands.search.field import NumericField, TagField, TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.json.path import Path as JsonPath
from redis.commands.search.query import Query

import findspark
findspark.init()
from pyspark.sql import SparkSession 
from pyspark.sql.functions import * 

# TODO: use context managers to handle spark session
try:
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    spark = SparkSession.Builder()\
            .master("local")\
            .appName("fancy_shoes")\
            .getOrCreate()

except Exception as e:
    print("pyspark or redis failed lol: 🤣", e)
    raise e

needed = [col("id"), col("name"), col("dateAdded"), col("dateUpdated"), col("colors"), col("brand"), col("categories"), col("name"), col("`prices.amountMax`"), col("`prices.amountMin`"), col("`prices.dateAdded`")]
root_dir = Path(__file__).parent.parent

# Saving a parquet file requires hadoop. so gave up for now
def get_dataframe():
    df =  spark.read.csv(str(root_dir / "assets/Datafiniti_Womens_Shoes.csv"), header=True, inferSchema=True)
    filtered_df = df.select(needed)\
            .withColumn("brand", regexp_replace(col("brand"), r"[^a-zA-Z0-9 ]", "" ))\
            .withColumn("dateAdded", unix_timestamp(col("dateAdded"), "yyyy-MM-dd HH:mm:ss").cast("Integer"))\
            .withColumn("dateUpdated", unix_timestamp(col("dateUpdated"), "yyyy-MM-dd HH:mm:ss").cast("Integer"))\
            .withColumn("prices.dateAdded", unix_timestamp(col("`prices.dateAdded`"), "yyyy-MM-dd HH:mm:ss").cast("Integer"))\

    return  filtered_df

def jsonify_with_id(row): 
    prices = {
            "amountMax": row["prices.amountMax"],
            "amountMin": row["prices.amountMin"],
            "dateAdded": row["prices.dateAdded"],
            }
    productInfo = {
            "brand": row["brand"],
            "colors": row["colors"],
            "categories": row["categories"],
            "name": row["name"].lower(),
            "prices": prices,
            }
    product = {
            "id": row["id"],
            "dateAdded": row["dateAdded"],
            "dateUpdated": row["dateUpdated"],
            "productInfo": productInfo,
            }
    yield product, row["id"]

def create_redix_index():
    rs_shoes = r.ft("idx:shoes")
    try: 
        rs_shoes.info()
        print("index exists")
        offset = 0 
        color = "silver"
        print("✨", rs_shoes.search(Query(f"@colors:{ {color} }").return_field("$").paging(offset, 10)))

    except Exception as _:
        print("no index found, so creating 😋")
        search_schema = (
                TagField("$.productInfo.brand", as_name="brand"), 
                TagField("$.productInfo.colors", as_name="colors"), 
                TextField("$.productInfo.categories", as_name="categories"), 
                NumericField("$.dateUpdated", as_name="dateUpdated"),
                NumericField("$.dateAdded", as_name="dateAdded"),
                )
        rs_shoes.create_index(
                fields=search_schema, 
                definition=IndexDefinition(
                    prefix=["product:"], 
                    index_type=IndexType.JSON
                    )
                )
        return True

    return False

def write_to_redis(product, number):
    key = f"product:{number}"
    r.json().set(key, JsonPath.root_path(), product)

# ------------------------------- DRIVER CODE --------------------------------- #
def run_population():
    df = get_dataframe()
    print(df.show(1))

    # TODO: use collect() after building search index
    for row in df.collect():
        for product, id  in jsonify_with_id(row):
            # print(product, id)
            write_to_redis(product, id)

    create_redix_index()


if __name__ == "__main__":
    print("running pyspark - redis population")
    run_population()


# def check_file_exists():
#     print(root_dir)
#     if os.path.isfile(root_dir / "assets/Datafiniti_Womens_Shoes.parquet"):
#         return True
#     else:
#         return False
