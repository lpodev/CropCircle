import turtle

turtle.title("Crop Circle")

turtle.penup()  # Lift the pen up
turtle.goto(0, -100)  # Move the turtle to the center of the screen
turtle.pendown()  # Put the pen down

turtle.circle(100)  # Draw a circle with a radius of 100 pixels


# It keeps the window open until the user closes it.
turtle.done()
