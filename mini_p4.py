# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
direction = RIGHT

# initialize ball_pos and ball_vel for new bal in middle of table

paddle1_vel = paddle2_vel = 0;
paddle1_pos =([0, HEIGHT /2 - HALF_PAD_HEIGHT], [0, HEIGHT /2 + HALF_PAD_HEIGHT] )
paddle2_pos =([WIDTH, HEIGHT /2 - HALF_PAD_HEIGHT], [WIDTH, HEIGHT /2 + HALF_PAD_HEIGHT])
# ========================================================================
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2];
    if(direction == RIGHT):
        ball_vel = [random.randrange(1, 6), random.randrange(1, 6)];
    else:
        ball_vel = [- random.randrange(1, 6), random.randrange(1, 6)];        
# ========================================================================
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, direction # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(direction) 
# ========================================================================
def draw(c):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global direction, score1, score2
    if(direction == RIGHT):
        direction = LEFT
    else:
        direction = RIGHT 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0];
    ball_pos[1] += ball_vel[1];
# red area   
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and ((paddle1_pos[0][1] <= ball_pos[1]) and (paddle1_pos[1][1] >= ball_pos[1])):
        ball_vel[0] = -ball_vel[0]
    elif (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and ((paddle1_pos[0][1] >= ball_pos[1]) or (paddle1_pos[1][1] <= ball_pos[1])): 
        score2 += 1
        spawn_ball(direction)
        
# green area  
    if (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH) and ((paddle2_pos[0][1] <= ball_pos[1]) and (paddle2_pos[1][1] >= ball_pos[1])):
        ball_vel[0] = -ball_vel[0]
    elif (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH) and ((paddle2_pos[0][1] >= ball_pos[1]) or (paddle2_pos[1][1] <= ball_pos[1])): 
        score1 += 1
        spawn_ball(direction)
        
# horizont and vertical      
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball    
    c.draw_circle(ball_pos, BALL_RADIUS, 5, 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] += paddle1_vel;
    paddle1_pos[1][1] += paddle1_vel;
    if paddle1_pos[0][1] <= 0:
        paddle1_pos[0][1] = 0;
        paddle1_pos[1][1] = PAD_HEIGHT;
    if paddle1_pos[1][1] >= HEIGHT:
        paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT;
        paddle1_pos[1][1] = HEIGHT

    paddle2_pos[0][1] += paddle2_vel;
    paddle2_pos[1][1] += paddle2_vel;
    if paddle2_pos[0][1] <= 0:
        paddle2_pos[0][1] = 0;
        paddle2_pos[1][1] = PAD_HEIGHT;
    if paddle2_pos[1][1] >= HEIGHT:
        paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT;
        paddle2_pos[1][1] = HEIGHT

    # draw paddles
    c.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, 'Red')
    c.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, 'Green')
    
    # draw scores
    c.draw_text('Player 1', (190, 50), 24, 'Red') 
    c.draw_text('Player 2', (320, 50), 24, 'Green') 
    c.draw_text(str(score1), (220, 100), 48, 'Red') 
    c.draw_text(str(score2), (350, 100), 48, 'Green') 
# ========================================================================    
def keydown(key):
    global paddle1_vel, paddle2_vel
    temp = 5
    
    #player 1
    if(key == simplegui.KEY_MAP["W"]):
        paddle1_vel =  - temp;
    if(key == simplegui.KEY_MAP["S"]):
        paddle1_vel = temp;
        
    #player 2
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel =  - temp;
    if(key == simplegui.KEY_MAP["down"]):
        paddle2_vel = temp;
# ========================================================================        
def keyup(key):
    global paddle1_vel, paddle2_vel
    #player 1
    if(key == simplegui.KEY_MAP["W"]):
        paddle1_vel = 0;
    if(key == simplegui.KEY_MAP["S"]):
        paddle1_vel = 0;
    #player 2
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel = 0;
    if(key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0;
# ========================================================================
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button_restart = frame.add_button('Restart!', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
