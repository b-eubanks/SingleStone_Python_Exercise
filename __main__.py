import pandas as pd
import pyarrow.parquet
import csv
import json


Class GetInfo:
def files():
	parquet_file = r'C:\Users\Bryon\data_python_exercise\data_engineer\teachers.parquet'

	csv_file = r'C:\Users\Bryon\data_python_exercise\data_engineer\students.csv'

	print('Files found successfully')


def dataframes():
	df1 = pd.read_parquet(parquet_file, engine='auto', columns=['fname','lname','cid'])

	df2 = pd.read_csv(csv_file, sep='_', usecols=['fname','lname','cid'])

	df3 = pd.merge(df1, df2, on='cid')


df3.to_json("results.json")
