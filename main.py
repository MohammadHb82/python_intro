# # 
# class Student:
  
  
#   def __init__(self,name ,age ,grade ,city ,spec):
#     self.name= name
#     self.age =age
#     self.grade = grade
#     self.city = city
#     self.spec = spec


#   def __str__(self):
   
#     return f'hello {self.name} your age is {self.age} and your grade is {self.grade} and your city is {self.city} and your spec is {self.spec}'  


#   def addcourse (self, course ):
#      return f'hello {self.name} you added {course} to your courses'
    
    
# def __talk__():
#   return f'hello my name is {self.name}'
# print(' hi to my program')

# name=input('enter the students name')
# age = int(input ('enter the age'))
# city =input ('enter the city')
# grade = int(input (' enter the age '))
# spec=  input('enter the spec')

# Student1= Student(name,age,city , grade,spec)


# print (' information added successfully')

# print('add new course')
# print (student1.addcourse(course=input('add a new course')))

# print (student1)



         
class Student:
  def __init__(self,name='ss' ,age =22,grade=22,city='aa',specialise='aa',password='111'):
    self.name=name
    self.age=age
    self.city=city
    self.grade=grade
    self.specialise=specialise
    self.password=password
    
    
  def __str__(self):
    return f'your name is {self.name} ,age is {self.age},grade is {self.grade}, city '     
    
    

  
  def talk(self):
    return f'hello my name is {self.name}'
  
student =[]
while True:
    print('welcome to our program')
    print('1-login')
    print(' 2-register')
    print('3- exit')
    
    choice = int(input ('enter your choice :'))
    
    if choice ==1:
      print('welcome to login')
      while True:
        password1=input('enter your password')
        name1=input('enter your name')
        for i in range (len(student)):
          if student[i].name==name and student[i].password ==password:
            print ('you  logged in succssfully')
            break
          else:
            print ('wrong password, try again')
      
    elif choice ==2:
      name = input('enter your name ') 
      age =int(input('enter your age')) 
      
      grade = int(input ('enter your grade'))
      city =input('enter your city')
      specialise = input('enter your specialise')
      password= input('enter your password')
      student1=Student(name,age,grade,city,specialise,password)
      print(student1.__str__())
      student.append(student1)
      print(student)
    elif choice ==3:
     break
    