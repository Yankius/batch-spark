from pyspark.sql import SparkSession

# Create a local spark session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("LocalTestSession") \
    .getOrCreate()
    
    
print(spark.version)
    
spark.stop()
    