import random
global status
def setup():
    global status
    status = 2
    size(500, 500)
    background(250, 88, 88)
    
def draw():
    noStroke()
    squares()
    if status == 2:
        number()
    

def squares():
    textSize(20)
    fill(255)
    # show numbers
    rect(200, 20, 90, 60)
    # change numbers
    fill(0)
    text('C', 400, 50)
    fill(255)
    rect(400, 50, 20, 20)
    # reset
    fill(0)
    text('R', 350, 50)
    fill(255)
    rect(350, 50, 20, 20)
    y = 100
    for i in range (5):
        x = 50
        for t in range (5):
            rect(x, y, 70, 70)
            x = x + 80
        y = y + 80
        
def mouseClicked():
    global status
    status = 0
    if (mouseX > 400) and (mouseX < 420) and (mouseY < 70) and (mouseY > 50):
        if status == 0:
            r = random.randint(1,99)
            fill(0)
            textSize(20)
            text(r, 250, 50)
            noLoop()
            
    if (mouseX > 350) and (mouseX < 370) and (mouseY < 70) and (mouseY > 50):
        number()
            
        
def mouseReleased():
    loop()
    
def number():
    global status
    fill(0)
    textSize(20)
    y = 100
    # if keyPressed:
    #     if key == 'r':
    for w in range (1000):
        for i in range (5):
            x = 50
            for t in range (5):
                text(random.randint(1, 99),x + 20, y + 40)
                x = x + 80
            y = y + 80
    noLoop()
    
            

    
            
        