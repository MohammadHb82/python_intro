# # # # if 1==2:
# # # #    print('1')
# # # # elif 1==3:
# # # #    print('2')
# # # # else:
# # # #    print('unknown')      
   
# # # #    switch:
# # # #      case1:
# # # #        print('1')
# # # #      case2:
# # # #        print('2')
# # # #      default:
# # # #        print('unknown')    
# # # num=0
# # # while num < 10:
# # #  print(num)
# # #  num=num+1
# # secretworld='python'
# # c=0
# # check = True
# # while check :
     
 
# #    userinput = print('enter your word')
# #    c= c + 1
# # if userinput==secretworld:
# #    print('correct') 
# # else:
# #      print('wrong')
# #      if c==2:
# #          check=False
# #          print('you have reached the limit')
# #          break
  
# #  counter =0
# #  while counter<5:
# #      userinput=('enter your string')
# #      print('-'*50)
# #      for i in range(0,len):
# #          ifuserinput[i]=='l'or  userinput[i]=='u'
# #             userinput=userinput.replace(userinput[i],'*')
# #             print(userinput[i])
# #             counter=counter+1
             
         
          
    

                
# names = ['Alice','David','Caroline']
# def magicTrick(names):
#      for i in (names):
#          print(i +' that was a great trick!')
#          print('i cant wait to see you next trick'+ i +'.\n')
# magicTrick(names)       
names = ['Alice ', 'David', 'Caroline']
counter = 0
for i in names:
    print(counter)
    if i == 'Alice':
       names = names[0:counter] + names[counter +1:]
       print(names)
    counter = counter +1    