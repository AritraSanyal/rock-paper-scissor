from random import randrange as r


def play():
   turns=int(input('HOW MANY TIMES DO YOU WANNA PLAY: '))
   user_points=0
   computer_points=0
   for i in range(1,turns+1):
      print('\nFROM THE OPTIONS OF "rock","paper","scissor" choose your option')
      user_choice=input('\n\t\t\tYOUR CHOICE: ')
      option=['rock','paper','scissor']
      
      comp_choice=option[r(0,3)]
      print("\t\t\tCOMPUTER'S CHOICE:",comp_choice,'\n')
      if comp_choice == user_choice:
       print('YOU MADE A DRAW')
      else:
        if comp_choice == option[0]:#when the computer select rock
           if user_choice == option[1]:
               print('YOU LOST.')
               computer_points +=1
           elif user_choice == option[2]:
               print('YOU WON.')
               user_points += 1
        if comp_choice == option[1]:#when the computer selects paper 
           if user_choice == option[2]:
               print('YOU LOST.')
               computer_points += 1
           elif user_choice == option[0]:
               print('YOU WON.')
               user_points += 1
        if comp_choice == option[2]:#when the computer selects scissor
           if user_choice == option[0]:
               print('YOU LOST.')
               computer_points += 1
           elif user_choice == option[1]:
               print('YOU WON.')
               user_points += 1
        elif(user_choice != option[0] or user_choice != option[1] or user_choice != option[2]):
           print("\t\t\tYOU ARE A IDIOT WHO DOSEN'T EVEN KNOW HOW TO READ\n\t\t\tYOU LOST A POINT FOR THAT")

   
   if computer_points == user_points:
      print('\n\nTHE GAME IS DRAW')          
   elif computer_points>user_points:
      print('\n\nYOU LOST THE GAME ')
   else:
      print('\n\nYOU WON THE GAME')
   

        

            
            
    




