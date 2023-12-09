


pip install names

import pandas as pd;
import names; #generate random numbers
import random; #genrate random numbes
def is_exist(list , number):
  for i in range(0,len(list)):
    if (number == list[i]):
      return True

course_indices = {
    1 : 'Mathematics' ,
    2 :'Physics' ,
    3 : 'Computer Sci' ,
    4 : 'History'
} #course_indices
courses_data = {
    'Mathematics' : {'Course_no' : "MATH55" , 'Credit_hours' : 4  } ,
    'Physics' : {'Course_no' : "PHY444" , 'Credit_hours' : 3  },
    'Computer Sci' : {'Course_no' : "CS111" , 'Credit_hours': 3 } ,
    'History' : {'Course_no' : "HIS124" , 'Credit_hours' : 3 }
} #creating the course data

paid = ['y' , 'n'] #idicate if the student paid for the enrollment or not
tuition_rate = 354 ; # tuition_rate per hour

std_ID = []
std_name =[]
print("Random integers between 0 and 9: ")
for i in range(0,20):
     y=random.randrange(100, 300, 1)
     std_ID.append(y)

print("Random student name generater : ")
for i in range(0, 20 ) :
    y=names.get_full_name();
    std_name.append(y)

students_data = {
  'student_names' : [] ,
  'students_IDs' : [] ,
  'is_paid': [] ,
  'number_of_courses' : []
  }

for  i in  range (0,20):
  students_data['student_names'].append(std_name[i])
  students_data['students_IDs'].append(std_ID[i])
  students_data['is_paid'].append(paid[random.randrange(0,2)]) # 0 or  1 (2) not included
  students_data['number_of_courses'].append(random.randrange(1,5)) #1 2 3 4  (5) not included
print(students_data)

student_list =[]
courses=[]
for i in  range(0,20):
  students = {
    'name'  : names.get_full_name(),
     'ID':random.randrange(100 , 300) ,
     'is_paid':paid[random.randrange(0,2)],
     'number_of_courses': random.randrange(1,5) ,

  }
  student_list.append(students)

for i in  range ( 0 , len(student_list)):
  print(student_list[i])

student_index = {}
for i in  range (0,20):
  student_index[i]= 0


for i in  range(0,20):#0 1 2  ... 19
  random_number = random.randrange(1,5) # 1 2 3 4
  numbers =[]
  std_courses=[]
  std_no_courses = student_list[i]['number_of_courses'] # 1
  count = std_no_courses # 1
  for j in  range (0 , count) : # 0 , 1
    while (is_exist(numbers, random_number)):
      random_number = random.randrange(1,5)
    course = {
        course_indices[random_number],
        courses_data[course_indices[random_number]]['Course_no'] ,
        courses_data[course_indices[random_number]]['Credit_hours'],
    }
    std_courses.append(course)
    numbers.append(random_number)
  student_list[i]['courses'] = std_courses





df = pd.DataFrame(student_list)
print(df)

df.to_csv('students.csv')