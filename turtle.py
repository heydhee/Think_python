import turtle
bob= turtle.Turtle()
def Shape(length, angle):
    turtle.fd(length)
    turtle.lt(angle)
    return Shape(length,angle)

Shape(20,10)
