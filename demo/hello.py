import os
import sys

# Wskazanie ścieżki do Pythona z Twojego środowiska Anaconda
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("QuickStart").getOrCreate()  
# Create a DataFrame
df = spark.createDataFrame([("Alice", 1), ("Bob", 2), ("Charlie", 3)], ["name", "age"])  
# Show the DataFrame
df.show()  
# Perform a simple transformation
result = df.select("name").where("age > 1")
result.show()
