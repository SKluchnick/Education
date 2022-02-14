import pandas as pd
import numpy as np

# StudentsPerformance = pd.read_csv('C:\\Users\\User\\Desktop\\статистика\\StudentsPerformance.csv')
StudentsPerformance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
# print(StudentsPerformance)
# print(StudentsPerformance.head(5))
# print(StudentsPerformance.tail())
# print(StudentsPerformance.describe())
# print(StudentsPerformance.dtypes)
# print(StudentsPerformance.shape)

print(StudentsPerformance.groupby('gender').aggregate({'writing score':'mean'}))
