import pyspark.sql 
from pyspark.sql.functions import *

sess = pyspark.sql.SparkSession.Builder().config("spark.yarn.tags", tag)\
        .appName(app)\
        .enableHiveSupport().getOrCreate()
