

import random 
number = random.randrange(1,10)
next_trial = 1

print('Try to guess the number between 1 and 10 in three chances')

while True:
  guess1= int(input('\n Enter your guess: '))
  if guess1 == number:
    print(f'You guessed it on your {next_trial} try! Great job🎉🎊✨!')
    break
  elif guess1 > number:
    print ("Oh snap! your guess is higher, try again")
  else:
    print("Better luck next time, your guess is lower")
  next_trial +=1
  print('\n next_trial:',next_trial)


country_list = ["France","Spain","Italy","Austria","Germany"]

random choice module 
to choose user choice 
how to use choose from a list 



