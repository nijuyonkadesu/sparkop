# Pyspark workshop ~


## Installation of pyspark in windows
follow [this](https://medium.com/@dipan.saha/getting-started-with-pyspark-day-1-37e5e6fdc14b) and try that sample program

## spark df vs pandas df

spark supports:
- A distributed collection of data grouped into named columns
- lazy & parallel computation
- in memory operations
- immutable

## install pyspark
- https://medium.com/@dipan.saha/getting-started-with-pyspark-day-1-37e5e6fdc14b

## install redis 
https://redis.io/docs/install/install-stack/linux/
```bash


```bash
sudo systemctl start redis-stack-server
redis-cli -h 127.0.0.1 -p 6379
```

## Debug
```bash
FT._LIST
KEYS *user*
```
## Nice findings
- sc <- spark context [used to perform distributed operation, processing in parallel, writing to external storage]
- [parquet](https://www.linkedin.com/pulse/why-apache-parquet-instead-csv-files-mariano-silva)
- [all about pyspark](https://github.com/spark-examples/pyspark-examples)
- shard redis database - for multicore processing
- 1DB per redis instance (to reduce expiry key overhead) - 1 DB per feature
- clustering
- [redis examples](https://redis.readthedocs.io/en/stable/examples)

## Reffered Articles:
- https://www.linkedin.com/pulse/redis-design-patterns-high-volume-applications-melvin-rook
- 

## TODO
- read basics of dataframes

