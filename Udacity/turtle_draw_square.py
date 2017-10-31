import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("white")

    et=turtle.Turtle()
    et.shape('turtle')
    et.color('green')
    et.speed(3)

    n=0
    i=0

    while i<=5:     
        while n<=5:
            et.forward(100)
            et.right(60)
            n+=1
        et.right(30)
        i+=1

    window.exitonclick()


def draw_square_2(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")

    et=turtle.Turtle()
    et.shape('turtle')
    et.color('green')
    et.speed(3)

    for n in range (1,36):
        draw_square_2(et)
        et.right(10)
        
    window.exitonclick()
    
'''
    turtle.Turtle()
    joe.shape('arrow')
    joe.color('blue')
    joe.speed(3)
    joe.circle(150)
'''    


draw_art()
