# Hangman Ascii art
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
print ('\n Welcome to the HANGAN word game')
print ('\nPlease follow the game rules. When you guess each word correctly in the missing blanks you win but when you cant enter the right words correctly after 7 times you loose')
print()
words = ['Greed','Fame','Money','Wealth','Envy','Sloth','Gluthon']
guess_word = random.choice(words)
guess_word_list = list(guess_word.lower())
guess_word_length = len(guess_word)
player_letters = '_'*guess_word_length
player_letters_list = list(player_letters)
player_guess_slots = len(HANGMANPICS)
fails = 0
print(player_letters_list)
print()
while player_guess_slots > 0:
  blank = '_'
  if blank not in player_letters_list:
    print("you win!")
    break
  guess = input("key in a letter to try and fill the blank spaces: ")
  l_guess = guess.lower()
  if l_guess in guess_word_list:
    position = guess_word_list.index(l_guess)
    player_letters_list[position] = l_guess
    print()
    print("nice guess!")
    print(player_letters_list)
    print()
  else:
    print(HANGMANPICS[fails])
    print()
    fails+=1
    player_guess_slots-=1
    if player_guess_slots > 0 and player_guess_slots != 1:
      print(str(player_guess_slots) + " more bad guesses and it's over!")
      print()
    elif player_guess_slots == 1:
      print("final guess!")
      print()
    else:
      print()
else:
  print("you failed")
 
# create a list of  words
# make the computer pick a random choice
# turn the random word into a list so I can compare each letter with what the user type
# create another list with just blank lines that i will be replacing when the user gives me the letter
# create a variable that keep counts of user's remaining lives
# start the game in a while loop
# print blank lines for each letter in the random word list
# ask for user input
# check if user input is in random word list 
# if yes replace the blank in the other list and ask the user for another input
# if not reduce out of the lives of the current player and display the hangman pics showing how the user is hanging the man
# if the user has guessed all the word print you win and stop the game


from question_data import questions

# Ascii art for the quiz 
quiz_ascii = '''
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_|  
'''
print(quiz_ascii)

print ('Welcome to the quiz game🙌')
user_name = (input('Please enter your username: '))
print (f'\nWelcome {user_name}👍, please enter either true or false to fill the correct answer in each question.')
print()
score = 0
while True:
  for b in questions:
    print (b['question'])
    player_answer = (input('enter true or false: '))
    if player_answer == 'quit':
      quit()
    elif player_answer.lower() != 'true' and player_answer.lower() != 'false':
      print ('Invalid input🤷‍♀️\n')
    elif b['correct_answer'] == 'True' and player_answer.lower() == 'true':
       print ('correct answer👏\n')
       score += 1
    elif b['correct_answer'] == 'False' and player_answer.lower() == 'false':
      print ('correct answer👏\n')
      score += 1
    else:
      print ('wrong answer🤦‍♀️\n')  
      
  print()
  print ('Total score: ' + str(score) + "/" + str(len(questions)))
      

  # this is the get question
  #cars = {'car':'ford','model':'mustang','year':'1964'}
  #print(cars.get('model'))
      

      

      
      
    
  



MAIN.PY 

from question_data import questions

# Ascii art for the quiz 
quiz_ascii = '''
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___| 
    | |            
    |_|  
'''
print(quiz_ascii)
print('Hello, Let\'s play a quiz game. Enter True or False as your answer to each question\n')

quest_num = 0
correct_answer = 0
for eachquest in questions:
  quest_num += 1
  print(f'Question {quest_num}: {eachquest["question"]}')
  user = input('True or False: ').title()
  if user == eachquest['correct_answer']:
    correct_answer += 1
    print(f'\nYou are right!\nScore: {correct_answer}/{quest_num}\n')
  else:
    print(f'\nWrong, Try again!\nScore: {correct_answer}/{quest_num}\n')

QUESTIONDATA.PY

    questions = [
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The Ceratosaurus, a dinosaur known for having a horn on the top of its nose, is also known to be a decendent of the Tyrannosaurus Rex.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "medium",
      "question": "An octopus can fit through any hole larger than its beak.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Kangaroos keep food in their pouches next to their children.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'Kamea' the Gilbertese Islander word for dog, is derived from the English phrase 'Come here!'",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In 2016, the IUCN reclassified the status of Giant Pandas from endangered to vulnerable.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The Platypus is a mammal.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "A caterpillar has more muscles than humans do.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Finnish Lapphund dogs were used for herding reindeer.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Rabbits can see what's behind themselves without turning their heads.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
]






#pracrice four
print("return values in Functions".upper())
def make_album(artist_name = '(nil)', album_title = "(nil)", song_number = None):
    """create and return a dictionary of artist name and album title"""
    music_portfolio = dict()
    if song_number == None:
        music_portfolio['artist name'] = artist_name
        music_portfolio['album title'] = album_title
        return (music_portfolio)
    else:
        music_portfolio['artist name'] = artist_name
        music_portfolio['album_title'] = album_title
        music_portfolio['number of songs'] = song_number
        return (music_portfolio)
   
# variable declarations
music_list = []
artist1 = "Eminem"
artist1_album = "Recovery"
artist2 = "J cole"
artist2_album = "Forest Hill Drive"
artist3 = "Thousand Foot Krutch"
artist3_album = "The End Is Where We Begin"

# make_album function call
music_list.append(make_album(artist1, artist1_album))
music_list.append(make_album(artist2, artist2_album))
music_list.append(make_album(artist3, artist3_album))

# print(music_list)
for i in music_list:
    print(i, "\n")

new_album = make_album('Rihanna', 'Loud', 4)
print (new_album)
