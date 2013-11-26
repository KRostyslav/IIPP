# Mini-project #6 - Blackjack
import simplegui
import random
import math

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("https://www.dropbox.com/s/mar4m0hm0mfcfho/cards.png?dl=1")
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("https://www.dropbox.com/s/c7p2fn0zern1faq/card_back.png?dl=1")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
you_win = False
in_stand = True

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#=============================================================
# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
#=============================================================        
# define hand class
class Hand:
    def __init__(self,player_name):
        self.cards=[];
        self.value=0;
        self.aces=0;
        self.name=player_name;

    def add_card(self, card):
        self.cards.append(card)	
        self.value += VALUES[card.get_rank()]
        if(card.get_rank()=="A"):
            self.aces+=1
        if(self.value+10 <= 21 and self.aces >0):
            self.value=self.value+10
        if(self.value>21):
            in_play=False
            evaluate()
        
    def get_value(self):
        return self.value	
    
    def busted(self):
        print self.name+ " lose!"

    def draw(self, canvas, pos):
        sp=list(pos);
        padding = CARD_SIZE[0] + 25;
        for cd in self.cards:
            if(self.name=="Dealer" and in_play and sp[0]==pos[0]):
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE);
            else:
                cd.draw(canvas,sp);
            sp[0]+=padding;
 
#=============================================================        
# define deck class 
class Deck:
    def __init__(self):
        self.decklist=range(0,52)
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        self.decklist=range(0,52)
        random.shuffle(self.decklist)
        # use random.shuffle()

    def deal_card(self):
        num=self.decklist.pop(0)
        c=Card(SUITS[math.floor(num/13)],RANKS[num%13])	
        return c	# deal a card object from the deck
#=============================================================
#define event handlers for buttons
def evaluate():
    global score,in_play, you_win, in_stand
    in_stand = False
    in_play=False;
    if(dealer.get_value()>21):
        dealer.busted();
        you_win = True
        score+=1;
    elif player.get_value()>21:
        player.busted();
        you_win = False
        score-=1;
    elif(dealer.get_value()<player.get_value()):
        you_win = True
        score+=1;        
    else:
        you_win = False
        score-=1;
    
def deal():
    global outcome, in_play, in_stand, score,player,dealer
    deck.shuffle()
    player=Hand("You")
    dealer=Hand("Dealer")
    in_stand = True
    dealer.add_card(deck.deal_card())
    hit()
    dealer.add_card(deck.deal_card())
    hit()  
    if(in_play):
        score=-1
    in_play = True    

def hit():
    global in_play, in_stand
    if in_stand:
        player.add_card(deck.deal_card());
    # if the hand is in play, hit the player   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_stand
    in_stand = False
    while(dealer.get_value() < 17):
        dealer.add_card(deck.deal_card());   
    if(in_play):
        evaluate();   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global you_win
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("GAME: Blackjack",[150,50],40,"Black");
    canvas.draw_text("Score "+str(score),[250,100],30,"Red");
    dealer.draw(canvas,[30,200]);
    if in_play:
        message="Hit or Stand?";
    elif (you_win == True):
        message="You win. New Deal?"
    elif (you_win != True):
        message="You lose. New Deal?"
    canvas.draw_text(message,[150,350],30,"Red");
    player.draw(canvas,[30,400])    
    canvas.draw_text("You:",[30,550],30,"Black");
    canvas.draw_text("Dealer:",[30,180],30,"Blasck");

#=============================================================
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

deck=Deck();
player=Hand("You");
dealer=Hand("Dealer");
deal();
# remember to review the gradic rubric