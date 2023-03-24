import random
import os #* this os module is installed with python automatically, we can use it to control the terminal




score = 0
while score != -1:
  
  os.system("cls")
  number = random.randint(1, 1000)
  next_number = random.randint(1, 1000)
  
  answer = input(f"will the next number be higher or lower than ({str(number)}): ").lower()


  if answer not in ["higher","lower"]:
     print("Please use either higher or lower.")

     input()

     #! Error handling in your code is very important. in this case its not needed and the program can ignore it, but its good for users to know what's wrong.


  if answer == "higher":
      if next_number > number:
        score += 1 #! This should be at the top, so the new score is displayed.
        print(f"Correct!\nThe next number was {next_number}, Your score is {score} \n") # the \n here means new line, better to use this than to make new lines with new print statements

        input() #* an empty input, whenever we press enter it will continue
        os.system("cls") #! this is a command that clears the terminal

        
      else:
          
        print(f"You lost\nthe next number was {next_number}\n\n || Your score was {score}||\n")
        input() 
        os.system("cls")
        score = -1 

  elif answer == "lower":
      
      if next_number < number:
        score += 1
        print(f"Correct!\nThe next number was {next_number}, Your score is {score} \n")
        input()  
        os.system("cls")
      else:
        
        print(f"You lost\nthe next number was {next_number}\n\n || Your score was {score}||\n")
        input() 
        os.system("cls")
        score = -1
        
