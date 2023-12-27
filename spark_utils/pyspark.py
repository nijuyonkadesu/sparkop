import datetime
import json
import os
from pathlib import Path 

import findspark
findspark.init()

from pyspark.sql import SparkSession 
from pyspark.sql.functions import * 

# TODO: use context managers to handle spark session
try:
    spark = SparkSession.Builder()\
            .master("local")\
            .appName("fancy_shoes")\
            .getOrCreate()

except Exception as e:
    print("pyspark no session: ", e)
    raise e

needed = [col("id"), col("name"), col("dateAdded"), col("dateUpdated"), col("colors"), col("brand"), col("categories"), col("name"), col("`prices.amountMax`"), col("`prices.amountMin`"), col("`prices.dateAdded`")]
root_dir = Path(__file__).parent.parent

# def check_file_exists():
#     print(root_dir)
#     if os.path.isfile(root_dir / "assets/Datafiniti_Womens_Shoes.parquet"):
#         return True
#     else:
#         return False
# 
# Saving a parquet file requires hadoop. so gave up for now
def get_dataframe():
#    if not check_file_exists():
#        df = spark.read.csv(str(root_dir / "assets/Datafiniti_Womens_Shoes.csv"), header=True, inferSchema=True)
#        df.write.parquet(str(root_dir / "assets/Datafiniti_Womens_Shoes.parquet"))
#    else:
#        df = spark.read.parquet(str(root_dir / "assets/Datafiniti_Womens_Shoes.parquet"))
    return spark.read.csv(str(root_dir / "assets/Datafiniti_Womens_Shoes.csv"), header=True, inferSchema=True) 


def jsonify(row): 
    prices = {
            "amountMax": row["prices.amountMax"],
            "amountMin": row["prices.amountMin"],
            "dateAdded": row["prices.dateAdded"],
            }
    productInfo = {
            "brand": row["brand"],
            "colors": row["colors"].lower(),
            "categories": row["categories"].lower(),
            "name": row["name"].lower(),
            "prices": prices,
            }
    product = {
            "id": row["id"],
            "dateAdded": row["dateAdded"],
            "dateUpdated": row["dateUpdated"],
            "productInfo": productInfo,
            }
    yield product

def run_population():
    def default(o):
      if isinstance(o, (datetime.date, datetime.datetime)):
          return o.isoformat()

    df = get_dataframe()
    print(df.show(1))

    for row in df.select(needed).take(5):
      for product in jsonify(row):
        print(json.dumps(product, default=default))

    # TODO: write df to redis

if __name__ == "__main__":
    print("running pyspark - redis population")
    run_population()
