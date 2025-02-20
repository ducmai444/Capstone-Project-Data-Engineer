from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

def main():
    # The entrypoint to access all functions of Spark
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("Python Spark query optimizer")
        .getOrCreate()
    )

    # Read Data from parquet file
    
    taxi_data = spark.read.parquet(r'/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/taxi-data/0-0d57ccff-7c4e-4da3-aba9-81abb3c3685d-0.parquet')

    # Register the DataFrame as a temporary SQL table
    taxi_data.createOrReplaceTempView("taxi_data")

    # Run SQL queries on the DataFrame
    querry = spark.sql("SELECT * FROM taxi_data WHERE passenger_count > 0")

    # Show the result
    querry.show()


if __name__ == "__main__":
    main()


