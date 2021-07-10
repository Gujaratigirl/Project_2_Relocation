# Import Dependencies
import pandas as pd
import os

# Establish file locations
file_names = ['name1', 'name2', 'name3']

for name in file_names:
    file_path = os.path.join("Data", f'{name}.csv')
    df = pd.read_csv(file_path)
    output_path = os.path.join("Data", f'{name}.json')
    pd.to_json(output_path)