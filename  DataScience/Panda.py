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

# print(StudentsPerformance.groupby('gender').aggregate({'writing score':'mean'}))

# print(StudentsPerformance.size)

# print(StudentsPerformance.iloc[0:5,0:3])
# print(StudentsPerformance.iloc[[0,2],0:3])
first_date_frame = StudentsPerformance.iloc[[0,3]]
# print(first_date_frame)
first_date_frame.index = ["one","two"]
# print(first_date_frame)
# print(first_date_frame.loc[["one"]])
# print(first_date_frame.loc[["one"],["gender"]])

# print1 = pd.Series([11,22,33],index=["one","two","three"])
# print2 = pd.Series([111,222,333],index=["one","two","three"])
#
# print(pd.DataFrame({'col name-1':print1,'col name-2':print2}))
# print(first_date_frame['gender'])
# print(first_date_frame[['gender']])

# step = pd.read_csv(r'C:\\Users\\User\\Downloads\\titanic.csv')
# print(step)
titanic = pd.read_csv('https://stepik.org/media/attachments/course/4852/titanic.csv')
# print(titanic)
print(titanic.shape) # вывод числа строк, столбцов датафрейма
print(titanic.dtypes) # вывод имен и типов полей датафрейма
print(titanic.describe) # вывод описания датафрейма
# print(titanic.get_dtype_counts()) #  вывод количества типов полей датафрейма
print(titanic.info()) # вывод информации по датафрейму: число строк, столбцов, типы полей и количество данных по каждоу полю