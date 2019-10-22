#Anthony Gandini

from graphics import *
import math

def inCircle(pt1, circ):
    dx = pt1.getX() - circ.getCenter().getX()
    dy = pt1.getY() - circ.getCenter().getY()
    dist = math.sqrt(dx * dx + dy * dy)

    return dist <= circ.getRadius()
    
def main():
    win = GraphWin("Archery Board" , 1000 , 1000)
    white = Circle(Point(500 , 500) , 375)
    black = Circle(Point(500 , 500) , 300)
    blue = Circle(Point(500 , 500) , 225)
    red = Circle(Point(500 , 500) , 150)
    yellow = Circle(Point(500 , 500) , 75)
    
    white.setFill("white")
    black.setFill("black")
    blue.setFill("blue")
    red.setFill("red")
    yellow.setFill("yellow")
    
    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)
    
    score = 0
    total = 0

    for i in range(5):
        mouse = win.getMouse()
        if inCircle(mouse , yellow):
            score = 9
        elif inCircle(mouse , red):
            score = 7
        elif inCircle(mouse , blue):
            score = 5
        elif inCircle(mouse , black):
            score = 3
        elif inCircle(mouse , white):
            score = 1
        print("That click was worth" , score , "points")
        total += score
        
    print("Your total score was" , total)

main()