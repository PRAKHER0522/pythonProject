data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)
import numpy as np
grades= np.array(data)
print(grades)
print(type(data))
print(type(grades))
print(grades.shape)
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
student_data = np.array([grades,study_hours])
print(student_data)
print(student_data.shape)
print("mean of the grades")
print(grades.mean())
print("numpy array all function")
print(grades.all())
print(grades.size)
print(student_data.size)
print(student_data)
print(student_data.transpose())
import pandas as pd
df_student = pd.DataFrame({'Name':['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                   'StudyHours' : student_data[0],
                    'Grade':student_data[1]
                   })
print('student data:' )
print(df_student)
"""#print(df_student.loc[4])
print(df_student.loc[0:5])
print(df_student.iloc[0:5])
print(df_student.iloc[0,[1,2]])
print(df_student.loc[0,'Grade'])
#import data from file
file_name = 'D:/ml-basics-master/ml-basics-master/data/grades.csv'
df_students =pd.read_csv(file_name,delimiter=',')
print("*****header name*******")
print(df_students.head())
print("*****values*******")
print(df_students.values)
print("*****search for null*******")
print(df_students.isnull())
print("*****sum of missing values for each column*******")
print(df_students.isnull().sum())
print("*****we can filter the dataframe to include only rows where any of the columns*******")
print(df_students[df_students.isnull().any(axis=1)])
print(" if the number of study hours is missing, we could just assume that the student studied for an average amount of time and replace the missing value with the mean study hours. To do this, we can use the fillna method, like this:")
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print(df_students)
df_students.Grade = df_students.Grade.fillna(df_students.Grade.mean())
print(df_students)
print("*****explore data*******")
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))
print('Get students who studied for the mean or more hours')
print(df_students[df_students.StudyHours > mean_study])"""