# Import Dependencies
import pandas as pd
import os

file_path = os.path.join("Data", "state_migrations_2019.xlsx")
df = pd.read_excel(file_path)