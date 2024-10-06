from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


def main():
    conf = SparkConf()

    conf.setAll(
        [
            ("spark.master", "spark://0607b887a6fd:7077"),
            # ("spark.driver.host", "local[*]"),
            ("spark.submit.deployMode", "client"),
            ("spark.driver.bindAddress", "0.0.0.0"),
            ("spark.appName", "SparkOnDocker")
        ]
    )
    # Initialize SparkSession
    spark = SparkSession.builder \
            .config(conf=conf) \
        .getOrCreate()

    # Create an RDD containing numbers from 1 to 1000
    numbers_rdd = spark.sparkContext.parallelize(range(1, 1000))

    # Count the elements in the RDD
    count = numbers_rdd.count()

    print(f"Count of numbers from 1 to 1000 is: {count}")

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    main()