import turtle

def draw_square_2(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")

    et=turtle.Turtle()
    et.shape('turtle')
    et.color('green')
    et.speed(100)

    for n in range (1,73):
        draw_square_2(et)
        et.right(5)

    et.right(90)
    et.forward(300)
    
    window.exitonclick()
    
'''
    turtle.Turtle()
    joe.shape('arrow')
    joe.color('blue')
    joe.speed(3)
    joe.circle(150)
'''    


draw_art()
