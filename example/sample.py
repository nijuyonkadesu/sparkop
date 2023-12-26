from pyspark.sql import SparkSession 
from pyspark.sql.functions import *

spark = SparkSession.Builder()\
        .master("local")\
        .appName("Pyspark sample")\
        .getOrCreate()

df = spark.read.csv("assets/product-catalog.csv", header=True, inferSchema=True)
df.write.parquet("assets/product-catelog.parquet")

print(df.head())

spark.stop()

## There are methods to write to csv and json
#pandas vs spark df
