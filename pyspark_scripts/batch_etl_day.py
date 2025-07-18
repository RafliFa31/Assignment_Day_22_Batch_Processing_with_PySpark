from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

def main():
    # Inisialisasi SparkSession
    spark = SparkSession.builder \
        .appName("Daily ETL") \
        .config("spark.jars", "/opt/bitnami/spark/jars/postgresql-42.2.5.jar") \
        .getOrCreate()

    try:
        # Path file input/output
        input_path_flight = "/opt/airflow/data/customer_flight_activity.csv"
        input_path_loyalty = "/opt/airflow/data/customer_loyalty_history.csv"
        output_path_csv = "/opt/airflow/data/output/churn_analysis"

        print("🚀 Membaca file CSV...")
        flight_df = spark.read.option("header", True).csv(input_path_flight)
        loyalty_df = spark.read.option("header", True).csv(input_path_loyalty)

        flight_df = flight_df.withColumn("flight_duration", col("flight_duration").cast("float"))
        joined_df = flight_df.join(loyalty_df, on="customer_id", how="inner")

        print("🔄 Menghitung rata-rata durasi per tier...")
        result_df = joined_df.groupBy("tier").agg(avg("flight_duration").alias("avg_duration"))

        print("💾 Menyimpan hasil ke CSV...")
        result_df.write.mode("overwrite").option("header", True).csv(output_path_csv)

        print("💾 Menyimpan hasil ke PostgreSQL...")
        result_df.write \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://bp22_postgres:5432/airflow") \
            .option("dbtable", "churn_analysis") \
            .option("user", "airflow") \
            .option("password", "airflow") \
            .option("driver", "org.postgresql.Driver") \
            .mode("overwrite") \
            .save()

        print("✅ ETL selesai, hasil:")
        result_df.show()

    except Exception as e:
        print(f"❌ Error dalam proses ETL: {e}")

    finally:
        spark.stop()

if __name__ == "__main__":
    main()
