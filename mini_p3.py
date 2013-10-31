# template for "Stopwatch: The Game"
import simplegui;

canvas_width = 300;
canvas_height = 150;
name_game = 'Stopwatch: The Game';

# define global variables
time = 0;
succes = 0;
total = 0;

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    A = 0;
    if (time > 600):
        A = int(time/600);
        B = int((time - A*600)/100);
        C = int((time - A*600 - B*100)/10);
        D = int( time - A*600 - B*100 - C*10);
    else:
        B = int((time - A*600)/100);
        C = int((time - A*600 - B*100)/10);
        D = int( time - A*600 - B*100 - C*10);
    s = str(A)+':'+str(B)+str(C)+'.'+str(D);
    return s;    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start_handler():
    create_timer();

def button_stop_handler():
    global time, succes, total;
    if (time%10 == 0) and timer.is_running():
        succes = succes + 1;
    if timer.is_running():
        total = total + 1;
    timer.stop();

def button_reset_handler():
    global time, succes, total;
    time = 0;
    succes = 0;
    total = 0;
    timer.stop();

# define event handler for timer with 0.1 sec interval
def create_timer():
    global time;
    timer.start();
    time = time + 1;

# define draw handler
def draw(canvas):
    global succes, total;
    text = str(format(time));
    text_result = str(succes) + "/" + str(total);
    canvas.draw_text(text_result, (220,50), 24, "green");
    canvas.draw_text(text, (100,100), 36, "red");

# create frame
frame = simplegui.create_frame(name_game, canvas_width, canvas_height);

# register event handlers
frame.set_draw_handler(draw);
button_start = frame.add_button('Start', button_start_handler, 200);
button_stop = frame.add_button('Stop', button_stop_handler, 200);
button_restart = frame.add_button('Reset', button_reset_handler, 200);
timer = simplegui.create_timer(100, create_timer);

# start frame
frame.start();

# Please remember to review the grading rubric