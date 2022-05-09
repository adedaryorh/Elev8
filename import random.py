import random

rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
# END OF SECTION 👆

rp =[0,1,2]

# WRITE YOUR CODE BELOW THIS LINE 👇
# print(rps[2])

#Welcome to the smash game
robot_choice = random.choice(list(rps))
print(robot_choice)
user_selction = input("player should select their option: ")
# rps=["rock","scissors","paper"]
# robot_choice= random.choice(list(rps))
# print(robot_choice1)

# if user_selction == rps[0]:
#   print("This is a drawn")
# elif user_selction == 

#print(robot_selection)