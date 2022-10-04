# A simple hangman game created with Python

#Importing the required modules
#random for random selection of words
#hangman_ascii for game ascii arts
#words contains a list of words that will be used by the Game
import random
import hangman_ascii
import words

#Creating the variables

#ascii art for each stage of the Game
stages = hangman_ascii.stages
#the list of words that will be guessed by the User
word_list = words.word_list
#Randomly selcting a list of word to be guess by the User
chosen_word = random.choice(word_list)
#Storing the lenght of the randomly selcted word for use later
word_length = len(chosen_word)
#Setting the condition for a while loop
end_of_game = False
#The number of lives per Game
lives = 6

#printing hangman logo at the start of the Game
print(hangman_ascii.logo)

#If you want to test the code, this will display the randomly selcted word
#print(f'Pssst, the solution is {chosen_word}.')

#Creating an empty list
display = []
#filling the list with the same number of _ as is in the randomly selcted word
for _ in range(word_length):
    display += "_"

#A while loop for the Game, the game will continue as long as this condition remains false
while not end_of_game:
    #User gueses a letter they think will be in the randomly generated word
    guess = input("Guess a letter: ").lower()

    #This will notify the user if they guess the same word twice
    if guess in display:
      print(f'You have guessed {guess} already')
      print(f"{' '.join(display)}")
    '''
    This will loop through the index of each letter in the chosen_word and check to see if the letter
    at the index is the same as the letter guessed by the user.
    If the condition is fulffiled it replaces a '_' with the same index in the previously created display
    list with the guessed word
    '''
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    '''
    if the word guessed by the user is not in the chosen_word, it willl print out a statement informing the user
    and the the loser will loose a life
    '''
    if guess not in chosen_word:
        print(f'{guess} is not in the chosen word, \nYou lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose !!!")

    #This will join the cotent of the display list, convert it to a string and print.
    print(f"{' '.join(display)}")

    '''
    This will check to see if the user has guessed all the characters in the chosen_word
    if so it will change the end_of_game condition to true thereby exiting the while loop
    '''
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #This will print an ascii art corresponding to the amount of lifes the user has left
    print(stages[lives])
