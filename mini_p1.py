# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0 :
        result = "rock"
    elif number == 1 :
        result = "Spock"
    elif number == 2 :
        result = "paper"
    elif number == 3 :
        result = "lizard"
    elif number == 4 :
        result = "scissors"
    else :
        result = "error"
    return result
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock" :
        result = 0
    elif name == "Spock" :
        result = 1
    elif name == "paper" :
        result = 2
    elif name == "lizard" :
        result = 3
    elif name == "scissors" :
        result = 4
    else :
        result = "error"
    return result

def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    print ("Player chooses " + name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to name using number_to_name
    print ("Computer chooses " + number_to_name(comp_number))
    
    # compute difference of player_number and comp_number modulo five
    diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner    
    # print results
    if diff == 1 or diff == 2: 
        print 'Computer wins!'
    elif diff == 0:
        print 'Player and computer tie!'
    else:
        print 'Player wins!'
    print '' 

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

