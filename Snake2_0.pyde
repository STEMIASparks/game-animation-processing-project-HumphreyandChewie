#Main circle Variables
x = 375
y = 375

#Body Circle variables
a = 375
b = 375

#Movement key bind variables
up = 0
down = 0
left = 0
right = 0

#Speed
v = 5
#Lose condition variable
gg = 0
ggs = "Game Over!"
textx = 900
texty = 900

#Apple Location Variables
R1 = random(25,725)
R2 = random(25,725)
r1 = 0
r2 = 0

#Score
score = 0
sx = 500
sy = 50
hs = 0

def setup():
#Play area setup
    size(750,750)
    background(0)

def draw():
    global x, y, a, b, up, down, left, right, gg, textx, texty, R1, R2, r1, r2, score, sx, sy, v, hs
    
#Setting Apple Location variables
    r1 = R1
    r2 = R2

    
#Snake body drawing function
    pass
    noStroke()
    background(0)
    fill(200,0,0)
    rect(r1, r2, 20, 20, 7)
    fill(0,200,0)
    circle(x,y,50)

#Scoreboard
    fill(255,0,0)
    textSize(50)
    text("Score is " + str(score), sx, sy)
    if score >= hs:
        hs = score
    text("High Score is " + str(hs), sx-105, sy+70)

#Movement Variables
    if up >= 1 and gg < 1:
        a = x
        y = y-v
        delay(50)
    
    elif down >= 1 and gg < 1:
        a = x
        y += v
        delay(50)
    
    elif left >= 1 and gg < 1:
        b = y
        x = x-v
        delay(50)
    
    elif right >= 1 and gg < 1:
        b = y
        x += v
        delay(50)
    
#Lose Condition
    if x >= 725 or x <= 25:
        gg = 1
        textx = 260
        texty = 300
        
    elif y >= 725 or y <= 25:
        gg = 1
        textx = 200
        texty = 300


    if gg > 0:
        fill(255, 0, 0)
        textSize(50)
        text(ggs, textx, texty)
        
        
#Apple Sensing system
    if x <= r1+35 and x >= r1-35 and y <= r2+35 and y >= r2-35:
        score += 1
        v += 1
        delay(10)
        R1 = random(50, 700)
        R2 = random(50, 700)

#Key binds for Snake Movement
def keyPressed():
    global a, b, x, y, up, down, left, right, gg, textx, texty, v, score
    if key == 'w' or key == 'W':
        up = 1
        down = 0
        left = 0
        right = 0
        
    elif key == 'a' or key == 'A':
        up = 0
        down = 0
        left = 1
        right = 0
        
    elif key == 's' or key == 'S':
        up = 0
        down = 1
        left = 0
        right = 0
        
    elif key == 'd' or key == 'D':
        up = 0
        down = 0
        left = 0
        right = 1
    
    #Reset Function
    
    elif key == 'r' or key == 'R':
        x = 375
        y = 375
        textx = 900
        texty = 900
        gg = 0
        v = 5
        score = 0
        up = 0
        down = 0
        left = 0
        right = 0
    

        
