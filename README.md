# Assignment_Day_22_Batch_Processing_with_PySpark
# Batch Processing ETL with PySpark & Apache Airflow
@📌 Project Overview
ETL pipeline yang dibangun menggunakan Apache Airflow dan PySpark untuk menganalisis data penerbangan pelanggan, kemudian menyimpan hasilnya ke dalam PostgreSQL dan file CSV.

@🧰 Tools & Technologies
Apache Airflow – untuk menjadwalkan dan mengorkestrasi job ETL

PySpark – untuk proses transformasi data dalam skala besar

PostgreSQL – penyimpanan hasil akhir (output table)

Docker Compose – untuk menjalankan seluruh stack dalam container

@🔄 Pipeline Overview
Extract
Membaca file CSV hasil analisis sebelumnya yang telah dibersihkan.

Transform
Menganalisis pelanggan berdasarkan tingkat loyalitas dan frekuensi terbang.

Load
Menyimpan hasil analisis ke:

Tabel PostgreSQL: frequent_flyers_by_loyalty

File CSV: output/frequent_flyers_by_loyalty.csv

@📂 Struktur File
kotlin
Copy
Edit
BatchPro22/
├── dags/
│   └── batch_etl_dag.py
├── pyspark_scripts/
│   └── batch_etl_day.py
├── data/
│   ├── customer_flight_activity.csv
│   ├── customer_loyalty_history.csv
│   └── output/
├── jars/
│   └── postgresql-42.2.5.jar
├── docker-compose.yaml
└── Dockerfile.airflow
#🗓️ Airflow DAG
Nama DAG: batch_etl_pyspark

Lokasi File: dags/batch_etl_dag.py

Deskripsi: Menjalankan skrip PySpark batch_etl_day.py via spark-submit

#🚀 Menjalankan Proyek
bash
Copy
Edit
docker-compose up --build
Setelah itu, akses antarmuka berikut:

Airflow UI: http://localhost:8088

Spark UI: http://localhost:8080

#📦 Output
Hasil ETL akan disimpan ke:

PostgreSQL Table: frequent_flyers_by_loyalty

CSV File: data/output/frequent_flyers_by_loyalty.csv

