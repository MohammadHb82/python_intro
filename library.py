
# # # # # 
# # # # class Student:
  
  
# # # #   def __init__(self,name ,age ,grade ,city ,spec):
# # # #     self.name= name
# # # #     self.age =age
# # # #     self.grade = grade
# # # #     self.city = city
# # # #     self.spec = spec


# # # #   def __str__(self):
   
# # # #     return f'hello {self.name} your age is {self.age} and your grade is {self.grade} and your city is {self.city} and your spec is {self.spec}'  


# # # #   def addcourse (self, course ):
# # # #      return f'hello {self.name} you added {course} to your courses'
    
    
# # # # def __talk__():
# # # #   return f'hello my name is {self.name}'
# # # # print(' hi to my program')

# # # # name=input('enter the students name')
# # # # age = int(input ('enter the age'))
# # # # city =input ('enter the city')
# # # # grade = int(input (' enter the age '))
# # # # spec=  input('enter the spec')

# # # # Student1= Student(name,age,city , grade,spec)


# # # # print (' information added successfully')

# # # # print('add new course')
# # # # print (student1.addcourse(course=input('add a new course')))

# # # # print (student1)



         
# # # class Student:
# # #   def __init__(self,name='ss' ,age =22,grade=22,city='aa',specialise='aa',password='111'):
# # #     self.name=name
# # #     self.age=age
# # #     self.city=city
# # #     self.grade=grade
# # #     self.specialise=specialise
# # #     self.password=password
    
    
# # #   def __str__(self):
# # #     return f'your name is {self.name} ,age is {self.age},grade is {self.grade}, city '     
    
    

  
# # #   def talk(self):
# # #     return f'hello my name is {self.name}'
  
# # # student =[]
# # # while True:
# # #     print('welcome to our program')
# # #     print('1-login')
# # #     print(' 2-register')
# # #     print('3- exit')
    
# # #     choice = int(input ('enter your choice :'))
    
# # #     if choice ==1:
# # #       print('welcome to login')
# # #       while True:
# # #         password1=input('enter your password')
# # #         name1=input('enter your name')
# # #         for i in range (len(student)):
# # #           if student[i].name==name and student[i].password ==password:
# # #             print ('you  logged in succssfully')
# # #             break
# # #           else:
# # #             print ('wrong password, try again')
      
# # #     elif choice ==2:
# # #       name = input('enter your name ') 
# # #       age =int(input('enter your age')) 
      
# # #       grade = int(input ('enter your grade'))
# # #       city =input('enter your city')
# # #       specialise = input('enter your specialise')
# # #       password= input('enter your password')
# # #       student1=Student(name,age,grade,city,specialise,password)
# # #       print(student1.__str__())
# # #       student.append(student1)
# # #       print(student)
# # #     elif choice ==3:
# # #      break
# # # class Product:
# # #       def __init__(self, product_name ='default',expire=2022,origion_price=22,sell_price=33):
# # #         self.name= product_name
# # #         self.expire=expire
# # #         self.__origion_price=origion_price
# # #         self.sell_price =sell_price
        
# # #       def __str__(self):
# # #         return f' hello welcome for our products '  
      
      
        
        
# # #       def get_price(self):
# # #         self.sell_price = self.__origion_price +.3*self.__origion_price
# # #         return f'welcome , the price of {self.name }  is {self.sell_price}  '
    
# # # name=input('enter the product name')
# # # expire =int(input('enter the expire of the product')) 
# # # origion_price = int (input('enter the sell price')) 
# # # product1=Product(name ,expire,origion_price )

# # # print(product1)

# # # print(product1.get_price())


  
      
        

# # # class Father :
  
# # #   def __init__(self,name='ali',age=50):
# # #     self.fathername=name
# # #     self.fatherage=age

    
# # #   def __str__(self):
# # #    return f'hello my name is {self.fathername}'
 
# # #   def talk(self):
# # #     print (self.fathername)
# # #     return f' hi my name is {self.fathername}'
    
 
# # # class Son(Father):
# # #   def __init__(self,name,age,password='12345'):
# # #     super().__init__()
# # #     self.name=name
# # #     self.age=age 
# # #     self.__password=password
    
# # #   def __str__(self):
# # #     return f'hi my name is {self.name}'  
  
# # #   def talk(self):
# # #     print(self.name)
# # #     print (super().talk())
# # #     return f'hi my name is {self.name}'
  
# # #   def getpass(self):
# # #     return (self.__password)
  

    

# # # son1 =Son('ahmed',20)
# # # print(son1)
# # # print(son1.talk())
# # # print(son1.getpass())
   
   
# # # class Square:
# # #   def __init__(self,x=30):
# # #      self.x=x
     
# # #   def __str__(self):
# # #     return f'the square length is {self.x}'
  
# # #   def area(self):

# # #     return  self.x*self.x
    

# # # class Rectangle(Square):
 
# # #   def __init__(self,y):
# # #     super().__init__() 
# # #     self.y=y 
# # #   def area(self):
# # #     return self.x*self.y  
        
# # # area1=Square(30)
# # # print(area1)   
  

# # # area2=Rectangle(50) 
# # # print(area2.area())
     
     
# # class Father :
# #   def __init__(self,name,age,haircolor):
# #     self.fathname=name
# #     self.fathage=age
# #     self.haircolor=haircolor
    
# #   def __str__(self):
# #     return f'fathes name is {self.fathname} , father age is {self.fathage} , haircolor is {self.haircolor}' 
  
  
# #   def talk(self):
# #     return f'hello fathers name is {self.fathname}' 
  
# # class Mother:
# #   def __init__(self, name ,age ,eyecolor):
# #     self.mumname=name
# #     self.mumage=age
# #     self.eyecolor=eyecolor
    
# #   def __str__(self):
# #       return f'mothers name is {self.mumname} , mother age is {self.mumage} , eyecolor is {self.eyecolor}'  
    

# # class Party:
# #   def __init__(self,location):
# #     self.location=location
    
# #   def __str__(self):
# #     return f' the party location is {self.location}' 
    
    
# # # class Friends:
  
# # #   def __init__(self, friends=[]):
# # #     self.n    
# # class Son(Father,Mother,Party):
# #   def __init__(self , name, age,fathname,fathage,haircolor,mumname,mumage,eyecolor,location):
# #     self.sonname=name
# #     self.sonage=age
# #     Father.__init__( self,fathname,fathage,haircolor)
# #     Mother.__init__(self, mumname,mumage,eyecolor)
# #     Party.__init__(self,location)
  
# #   def talk(self):
# #     print (super().talk())
  
# #   def __str__(self):
# #     return f' son name is {self.sonname} , son age is {self.sonage} , father name is {self.fathname}, mother name is {self.mumname} mother age is {self.mumage} and the location of party is {self.location}'
        
        
        
# # son1= Son('ali',20,'ahmed',50,'black','sara',40,'blue','amman')

# # print(son1)   
# # son1.talk()    

# class Animals:
#   def __init__(self ,name , type):
#     self.name=name
#     self.type=type
    
#   def __str__(self):
#     return f' the animals name is {self.name}, and the animals type is {self.type}'
  
#   def __eq__(self, other):
#     return self.name == other.name and self.type == other.type
  
  
# animal1=Animals('cat','mammal')

# print('animal 1 is :',animal1)
# animal2=Animals('cat','mammal')  

# print ('animal2 is :',animal2)

# print('check if equal :',animal1==animal2)
# print ('check type of obj1 :', type(animal1))
# print ('check type of obj2 :', type(animal1))

from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# def name():
#   print('hi from tkinter')
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=1, row=1)
# ttk.Button(frm, text="Quit", command=name()).grid(column=1, row=0)
# root.mainloop()    
window=Tk()

window.title('welcome')
window.geometry('350x200')
lb1=Label(window, text='hello')
lb1.grid(column=0,row=0)
count1=0
def clicked():
  global count1
  count1+=1
  print(count1)
  lb1.configure(text=f"count={count1}") 
inputtxt=Text(window,height=5,width=20)
inputtxt.pack()
bin=Button(window,text='click me',command=clicked)
bin.grid(column=1,row=0)
window.mainloop()
