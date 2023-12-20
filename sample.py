from pyspark.sql import SparkSession 

spark = SparkSession.Builder()\
        .master("local")\
        .appName("Pyspark sample")\
        .getOrCreate()

print("version", spark.version)
