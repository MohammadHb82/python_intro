# 
class Student:
  
  
  def __init__(self,name ,age ,grade ,city ,spec):
    self.name= name
    self.age =age
    self.grade = grade
    self.city = city
    self.spec = spec


  def __str__(self):
   
    return f'hello {self.name} your age is {self.age} and your grade is {self.grade} and your city is {self.city} and your spec is {self.spec}'  


  def addcourse (self, course ):
     return f'hello {self.name} you added {course} to your courses'
    
    
def __talk__():
  return f'hello my name is {self.name}'
print(' hi to my program')

name=input('enter the students name')
age = int(input ('enter the age'))
city =input ('enter the city')
grade = int(input (' enter the age '))
spec=  input('enter the spec')

Student1= Student(name,age,city , grade,spec)


print (' information added successfully')

print('add new course')
print (student1.addcourse(course=input('add a new course')))

print (student1)



         

  