from random import randint
import turtle


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Function checks if point is between two values, even if 1st value is > than 2nd value.
    def falls_in_rectangle(self, rectangle):
        flag_in_rectangle = True
        # Сheck x
        if rectangle.point1.x < rectangle.point2.x:
            if not rectangle.point1.x < self.x < rectangle.point2.x:
                flag_in_rectangle = False
        else:
            if not rectangle.point2.x < self.x < rectangle.point1.x:
                flag_in_rectangle = False
        # Сheck y
        if rectangle.point1.y < rectangle.point2.y:
            if not rectangle.point1.y < self.y < rectangle.point2.y:
                flag_in_rectangle = False
        else:
            if not rectangle.point2.y < self.y < rectangle.point1.y:
                flag_in_rectangle = False
        # Return the result
        return flag_in_rectangle

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + 
            (self.y - point.y)**2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate
        canvas.penup()  # Do not touch the canvas with a pen
        canvas.goto(self.point1.x, self.point1.y)

        canvas.color("orange")
        canvas.pensize(2)
        canvas.shape("turtle")

        canvas.pendown()  # Touch the canvas with a pen
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)  # Turn 90 degrees left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        # Go to a certain coordinate
        canvas.penup()  # Do not touch the canvas with a pen
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
        canvas.hideturtle()
        

# Create rectangle object
rectangle = GuiRectangle(
    Point(randint(0, 200), randint(0, 200)), 
    Point(randint(200, 400), randint(200, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")),
                   float(input("Guess y: ")))

user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle:",
      user_point.falls_in_rectangle(rectangle))

print("Your area was off by:",
      abs(rectangle.area()) - user_area, ".",
      "The actual area is:", abs(rectangle.area()))


myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
