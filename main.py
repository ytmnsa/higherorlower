import random
score = 0
while score != -1:
  
  number = random.randint(1, 1000)
  next_number = random.randint(1, 1000)
  
  answer = input(str(number) + ".  will the next number be higher or lower: ").lower()

  if answer == "higher":
      if next_number > number:
          print("Correct!")
          print(f"the next number was {next_number}")
          print(" ")
          score += 1
      else:
          print("You Lost")
          print(f"the next number was {next_number}")
          print(f"Your score was {score}")
          score = -1

  elif answer == "lower":
      if next_number < number:
          print("Correct!")
          print(f"the next number was {next_number}")
          print(" ")
          score += 1
      else:
          print("You Lost")
          print(f"the next number was {next_number}")
          print(f"Your score was {score}")
          score = -1
