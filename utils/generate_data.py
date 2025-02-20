from deltalake.writer import write_deltalake
import pandas as pd
import os
import pyarrow.parquet as pq

#Specify the directory where the Parquet files are stored
parquet_directory = "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/utils/output/"  # Update this to the actual directory path

output_dir = "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/taxi_combined"

#Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Duyệt qua tất cả thư mục con có dạng "part*"
for i, part in enumerate(os.listdir(parquet_directory)):
    temp = os.path.join(parquet_directory, part)
    partition_dir = os.path.join(output_dir, f"part{i}")

    for data in sorted(os.listdir(temp)):
        if data.endswith('.parquet'):
            df = pd.read_parquet(temp + '/' + data)

            # Định dạng lại schema để khớp với Delta Lake
            schema_corrected = {
                "VendorID": "int32",
                "PULocationID": "int32",
                "DOLocationID": "int32",
                "Airport_fee": "int64"
            }
            
            if "airport_fee" in df.columns:
                df.rename(columns={"airport_fee": "Airport_fee"}, inplace=True)

            expected_columns = [
                "VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count",
                "trip_distance", "RatecodeID", "store_and_fwd_flag", "PULocationID", "DOLocationID",
                "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount",
                "improvement_surcharge", "total_amount", "congestion_surcharge", "Airport_fee"
            ]
            
            for col, dtype in schema_corrected.items():
                if dtype in ["int32", "int64"]:
                    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(dtype)
                else:
                    df[col] = df[col].astype(dtype)

            for col, dtype in schema_corrected.items():
                if col in df.columns:
                    df[col] = df[col].astype(dtype)


            df = df[expected_columns]


    write_deltalake(partition_dir, df)
