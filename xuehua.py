import turtle
turtle.setup(700,600)
def draw(s):
    turtle.pendown()
    turtle.fd(s)

def data(L,n):
    if n == 1:
        draw(L)
        return True
    else:
         #data(L/3,n-1)
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            data(L/3,n-1)

def main():
    len = 300
    n = 4
    turtle.penup()
    turtle.goto(-200,150)
    turtle.begin_fill()
    turtle.fillcolor('black')
    for i in range(3):
        
        data(len,n)
        turtle.right(120)

    turtle.end_fill()

    

    turtle.end_fill()
    turtle.hideturtle()
    
main()
