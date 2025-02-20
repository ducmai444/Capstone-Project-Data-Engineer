import pandas as pd
import pyarrow.parquet as pq




if __name__ == '__main__':
#List the paths to the 12 Parquet files
    parquet_file_paths = [
        "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/yellow_tripdata_2022-08.parquet",
        "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/yellow_tripdata_2022-09.parquet",
        "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/yellow_tripdata_2022-10.parquet",
        "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/yellow_tripdata_2022-11.parquet",
        "/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/yellow_tripdata_2022-12.parquet",
        # Add the paths for the other files here
    ]

    # #Initialize an empty DataFrame to store the combined data
    # combined_df = pd.DataFrame()

    # #Read and concatenate the Parquet files
    # for path in parquet_file_paths:
    #     table = pq.read_table(path)
    #     df = table.to_pandas()
    #     combined_df = pd.concat([combined_df, df])

    # #Write the combined DataFrame to a new Parquet file
    # combined_output_path = "path_to_combined_file.parquet"
    # table = pq.Table.from_pandas(combined_df)
    # pq.write_table(table, combined_output_path)


    with pq.ParquetWriter("output.parquet", schema=pq.ParquetFile(parquet_file_paths[0]).schema_arrow) as writer:
        for file in parquet_file_paths:
            writer.write_table(pq.read_table(file))