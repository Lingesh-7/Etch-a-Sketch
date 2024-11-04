
#ETCH A SECTCH PROJECT 1

import turtle as t
print("Welcome to Etch A Seckch!!!\nPress the Following for:\n'a' to turn left\n'w' to move forward\n's' to move backward\n'd' for turning right\n's' for moving back\n'c' for drawing circle\n'k' for clear screen")
aamai=t.Turtle()
aamai.shape('turtle')


def clr():
    aamai.penup()
    aamai.clear()
    aamai.home()
    aamai.pendown()

def a():
    aamai.left(20)

def w():
    aamai.forward(10)

def s():
    aamai.backward(20)

def c():
    aamai.circle(20)
def d():
    aamai.right(20)

myscr=t.Screen()
myscr.listen()
myscr.onkey(a,'a')
myscr.onkey(w,'w')
myscr.onkey(s,'s')
myscr.onkey(d,'d')
myscr.onkey(c,'c')
myscr.onkey(clr,'k')
myscr.exitonclick()





