# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100

# helper function to start and restart the game
def new_game():
    global guess_count, secret_number, num_range, guess_number
    
    if num_range == 100 :
        guess_count = 7
        guess_number = 0
        secret_number = random.randrange(0,num_range)
    else:    	
        guess_count = 9
        guess_number = 0
        secret_number = random.randrange(0,num_range)

    f.start
    print "\nNew game! Range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(guess_count) + "\n"

# define event handlers for control panel
def range100():
    global num_range, guess_count, last_count, guess_number
    num_range = 100
    new_game()
    
def range1000():
    global num_range, guess_count, last_count, guess_number
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global guess_number, guess_count
    guess_number = int(guess);
    
    print "\nGuess was " + guess;
    print "Number of remaining guesses is  " + str(guess_count)
    
    if guess_number > secret_number:
        print "Lower!"
    elif guess_number < secret_number:
        print "Higher!"
    else:
        print "Correct!\n"
        new_game();
        
    guess_count = guess_count - 1
    if guess_count == 0:
        print "You LOST!!!\n"
        new_game()
        
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is (0,100)", range100, 200)
f.add_button("Range is (0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

#start
new_game()