subject_1 = input('please enter 1st subject name:')
subject_2 = input('please enter 2nd subject name:')
subject_3 = input('please enter 3rd subject name:')
subject_4 = input('please enter 4th subject name:')
subject_5 = input('please enter 5th subject name:')

subject1_marks = int(input(f" Please enter {subject_1} total Marks:"))
subject2_marks = int(input(f" Please enter {subject_2} total Marks:"))
subject3_marks = int(input(f" Please enter {subject_3} total Marks:"))
subject4_marks = int(input(f" Please enter {subject_4} total Marks:"))
subject5_marks = int(input(f" Please enter {subject_5} total Marks:"))

subject1_omarks = int(input(f" Please enter {subject_1} obtained Marks:"))
subject2_omarks = int(input(f" Please enter {subject_2} obtained Marks:"))
subject3_omarks = int(input(f" Please enter {subject_3} obtained Marks:"))
subject4_omarks = int(input(f" Please enter {subject_4} obtained Marks:"))
subject5_omarks = int(input(f" Please enter {subject_5} obtained Marks:"))

subject1_C_Hour = int(input(f" Please enter {subject_1} Total Credit Hours:"))
subject2_C_Hour = int(input(f" Please enter {subject_2} Total Credit Hours:"))
subject3_C_Hour = int(input(f" Please enter {subject_3} Total Credit Hours:"))
subject4_C_Hour = int(input(f" Please enter {subject_4} Total Credit Hours:"))
subject5_C_Hour = int(input(f" Please enter {subject_5} Total Credit Hours:"))

subject1_Average = (subject1_omarks/subject1_marks) * 100
subject2_Average = (subject2_omarks/subject2_marks) * 100
subject3_Average = (subject3_omarks/subject3_marks) * 100
subject4_Average = (subject4_omarks/subject4_marks) * 100
subject5_Average = (subject5_omarks/subject5_marks) * 100

if subject1_Average >= 80 and subject1_Average <= 100:
  sgpa1 = 4
  print(f'SGPA of Subject {subject_1} is {sgpa1}')

elif subject1_Average >= 70 and subject1_Average <= 79:
  sgpa1 = 3
  print(f'SGPA of Subject {subject_1} is {sgpa1}')

elif subject1_Average >= 60 and subject1_Average <= 69:
  sgpa1 = 2
  print(f'SGPA of Subject {subject_1} is {sgpa1}')

elif subject1_Average >= 50 and subject1_Average <= 59:
  sgpa1 = 1
  print(f'SGPA of Subject {subject_1} is {sgpa1}')

else:
  sgpa1 = 0
  print(f'SGPA of Subject {subject_1} is {sgpa1}')
  

if subject2_Average >= 80 and subject2_Average <= 100:
  sgpa2 = 4
  print(f'SGPA of Subject {subject_2} is {sgpa2}')

elif subject2_Average >= 70 and subject2_Average <= 79:
  sgpa2 = 3
  print(f'SGPA of Subject {subject_2} is {sgpa2}')

elif subject2_Average >= 60 and subject2_Average <= 69:
  sgpa2 = 2
  print(f'SGPA of Subject {subject_2} is {sgpa2}')

elif subject2_Average >= 50 and subject2_Average <= 59:
  sgpa2 = 1
  print(f'SGPA of Subject {subject_2} is {sgpa2}')

else:
  sgpa2 = 0
  print(f'SGPA of Subject {subject_2} is {sgpa2}')
  

if subject3_Average >= 80 and subject3_Average <= 100:
  sgpa3 = 4
  print(f'SGPA of Subject {subject_3} is {sgpa3}')

elif subject3_Average >= 70 and subject3_Average <= 79:
  sgpa3 = 3
  print(f'SGPA of Subject {subject_3} is {sgpa3}')

elif subject3_Average >= 60 and subject3_Average <= 69:
  sgpa3 = 2
  print(f'SGPA of Subject {subject_3} is {sgpa3}')

elif subject3_Average >= 50 and subject3_Average <= 59:
  sgpa3 = 1
  print(f'SGPA of Subject {subject_3} is {sgpa3}')

else:
  sgpa3 = 0
  print(f'SGPA of Subject {subject_3} is {sgpa3}')
  
if subject4_Average >= 80 and subject4_Average <= 100:
  sgpa4 = 4
  print(f'SGPA of Subject {subject_4} is {sgpa4}')

elif subject4_Average >= 70 and subject4_Average <= 79:
  sgpa4 = 3
  print(f'SGPA of Subject {subject_4} is {sgpa4}')

elif subject4_Average >= 60 and subject4_Average <= 69:
  sgpa4 = 2
  print(f'SGPA of Subject {subject_4} is {sgpa4}')

elif subject4_Average >= 50 and subject4_Average <= 59:
  sgpa4 = 1
  print(f'SGPA of Subject {subject_4} is {sgpa4}')

else:
  sgpa4 = 0
  print(f'SGPA of Subject {subject_4} is {sgpa4}')
  

if subject5_Average >= 80 and subject5_Average <= 100:
  sgpa5 = 4
  print(f'SGPA of Subject {subject_5} is {sgpa4}')

elif subject5_Average >= 70 and subject5_Average <= 79:
  sgpa5 = 3
  print(f'SGPA of Subject {subject_5} is {sgpa4}')

elif subject5_Average >= 60 and subject5_Average <= 69:
  sgpa5 = 2
  print(f'SGPA of Subject {subject_5} is {sgpa4}')

elif subject5_Average >= 50 and subject5_Average <= 59:
  sgpa5 = 1
  print(f'SGPA of Subject {subject_5} is {sgpa4}')

else:
  sgpa5 = 0
  print(f'SGPA of Subject {subject_5} is {sgpa4}')

quality_point1 = subject1_C_Hour * sgpa1
quality_point2 = subject2_C_Hour * sgpa2
quality_point3 = subject3_C_Hour * sgpa3
quality_point4 = subject4_C_Hour * sgpa4
quality_point5 = subject5_C_Hour * sgpa5

print(f"Quality point of {subject_1} ,{subject_2}, {subject_3} ,{subject_4} ,{subject_5} is respectevely  {quality_point1}, {quality_point2}, {quality_point3},{quality_point4}, {quality_point5}")

sum_qp = quality_point1 + quality_point2 + quality_point3 + quality_point4 + quality_point5

sum_credit_hour = subject1_C_Hour + subject2_C_Hour + subject3_C_Hour + subject4_C_Hour + subject5_C_Hour 

CGPA = (sum_qp/sum_credit_hour)
print(f"CGPA is {CGPA}")