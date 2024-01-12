
import random
print("WELCOME TO HANGMAN GAME ")
print("\n👇 GUESS THIS MOVIE 👇")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["barfi",
    "krrish",
    "golmaal",
    "fashion",
    "jabariya",
    "fidaa",
    "raazi",
    "stree",
    "raees",
    "october",
    "kedarnath",
    "mausam",
    "kalank",
    "kaminey",
    "barfi",
    "badlapur",
    "krrish",
    "piku",
    "dhadak",]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
vowel=["a","e","i","o","u"]

display = []

for _ in range(word_length):
  flag=False   
  for n in vowel:
        if chosen_word[_]==n:
          display+=n
          flag=True
          break 

  display+="_"   
  if flag:
    display.pop()
        
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
          display[position] = letter

  
    if guess not in chosen_word:
          lives-=1
          print(f"Left Lives :{lives}")
          print(stages[lives])

          if lives==0:
            end_of_game=True
            print("YOU LOOSED!!!!!")
            print(f"The movie is : {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

   