import pandas as pd
import pyarrow.parquet
import csv
import json
 

df1 = open(r'C:\Users\Bryon\data_python_exercise\data_engineer\teachers.parquet')
parq_df1 = pd.read_parquet(df1)

teacher_info = []

for row in parq_df1:
	teacher_info.append(row[1,2,6])


df2 = open(r'C:\Users\Bryon\data_python_exercise\data_engineer\students.csv')
csv_df2 = csv.reader(df2)

student_info = []

for row in csv_df2:
	student_info.append(row[1,2,6])

df3 = teacher_info + student_info

x = df3.to_json("results.json")