import pandas as pd
filename = "D:/ml-basics-master/ml-basics-master/data/grades.csv"
student_data = pd.read_csv(filename,delimiter=',',header=0,usecols=[0,1,2])
print(student_data)
student_data.StudyHours = student_data.StudyHours.fillna(student_data.StudyHours.mean())
student_data.Grade = student_data.Grade.fillna(student_data.Grade.mean())
print(student_data)
mean_stu = student_data['StudyHours'].mean()
print('maen : ' +str(mean_stu))
mean_grade = student_data['Grade'].mean()
print('Grade : ' +str(mean_grade))
passes = student_data.Grade > 60
student_data = pd.concat([student_data,passes.rename("pass1")],axis=1)
group_st = student_data.groupby(student_data.pass1).Name.count()
print(group_st)