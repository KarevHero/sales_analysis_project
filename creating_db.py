import os
import pandas as pd
from file_conversion import conversion

folders = 'sales_2024'
out_folders = 'File_for_analysis'

all_dfs = []

for filename in os.listdir(folders):
    file_path = os.path.join(folders, filename)

    df = conversion(file_path)
    all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)

final_df.to_csv('all_data.csv', index=False, sep=';')
