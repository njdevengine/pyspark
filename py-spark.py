# Import our SparkSession so we can use it
from pyspark.sql import SparkSession
# Create our SparkSession, this can take a couple minutes locally
spark = SparkSession.builder.appName("basics").getOrCreate()

from pyspark import SparkFiles
url = "https://s3.amazonaws.com/dataviz-curriculum/day_1/food.csv"
spark.sparkContext.addFile(url)
df = spark.read.csv(SparkFiles.get("food.csv"), sep=",", header=True)

#view data
df.show()

# Print our schema
df.printSchema()


# Show the columns
df.columns

# Describe our data
df.describe()

# Import struct fields that we can use
from pyspark.sql.types import StructField, StringType, IntegerType, StructType

# Next we need to create the list of struct fields
schema = [StructField("food", StringType(), True), StructField("price", IntegerType(), True),]
schema


# Pass in our fields
final = StructType(fields=schema)
final

# Read our data with our new schema
dataframe = spark.read.csv(SparkFiles.get("food.csv"), sep=",", header=True, schema=final)
dataframe


# Print it out
dataframe.printSchema()

dataframe['price']

type(dataframe['price'])

dataframe.select('price')

type(dataframe.select('price'))

dataframe.select('price').show()


import pandas as pd
pandas_df = dataframe.toPandas()
