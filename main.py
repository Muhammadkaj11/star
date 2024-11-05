import turtle


screen = turtle.Screen()
screen.bgcolor("white")  


star = turtle.Turtle()
star.shape("turtle")  
star.color("blue")    
star.speed(3)         


def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)  


draw_star(100)  


star.hideturtle()


screen.exitonclick()
