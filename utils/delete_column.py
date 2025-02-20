import pandas as pd

df = pd.read_parquet('/home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/taxi-data/0-0d57ccff-7c4e-4da3-aba9-81abb3c3685d-0.parquet')

column_to_remove = 'Airport_fee'

df = df.drop(columns=[column_to_remove])

df.to_parquet('home/maibaduc/Engineering/Capstone-Project-Data-Engineer-main/data/taxi_combined/part0/new-parquet.parquet', index= False)
