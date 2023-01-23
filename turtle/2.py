import turtle

T_1 = turtle.Turtle()

# for i in range(4):
#     T_1.forward(100)
#     T_1.left(90)

# for i in range(4):
#     T_1.forward(100)
#     T_1.right(90)

# for i in range(5):
#     T_1.forward(100)
#     T_1.right()

# T_1.right(90)


# T_1.forward(100)

# T_1.left(30)
# T_1.forward(100)

# for i in range(5):
#     T_1.forward(100)
#     T_1.right(144)
# 3- n-2 * 180
# def angle(x):
#     return((x-2)*180)


# for i in range(6):
#     T_1.forward(100)
#     T_1.right(360/18)


# import turtle   #Outside_In
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.color("blue")
 
# def sqrfunc(size):
#     for i in range(4):
#         skk.fd(size)
#         skk.left(90)
#         size = size-5
 
# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)

# wn = turtle.Screen()

# wn.bgcolor("BLUE")

# T_1.color("RED")
# T_1.speed(10)

# x = 200
# cnt = 0
# while(x >= 5):
#     T_1.forward(x)
#     T_1.left(90)
#     if(cnt == 2):
#         x -= 5
#         cnt = 0
#     cnt += 1

# Python program to user input pattern
# using Turtle Programming


# import time
# import random

# print ("This program draws shapes based on the number you enter in a uniform pattern.")
# squares = int(input("Enter the side number of the shape you want to draw: "))
# # if num_str.isdigit():
# # 	squares = int(num_str)

# angle = 180 - 180*(squares-2)/squares

# turtle.up

# x = 0
# y = 0
# turtle.setpos(x, y)


# numshapes = 8
# for x in range(numshapes):
# 	turtle.color(random.random(), random.random(), random.random())
# 	x += 5
# 	y += 5
# 	turtle.forward(x)
# 	turtle.left(y)
# 	for i in range(squares):
# 		turtle.begin_fill()
# 		turtle.down()
# 		turtle.forward(40)
# 		turtle.left(angle)
# 		turtle.forward(40)
# 		print (turtle.pos())
# 		turtle.up()
# 		turtle.end_fill()

# time.sleep(11)
# turtle.bye()


# import turtle #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size + 5

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)

# wn = turtle.Screen()

# wn.bgcolor("GREEN")

# T_1.color("LIGHT BLUE")

# x = int(input("WRITE THE SIZE OF SPIRAL: "))

# start_x = 5
# cnt = 0
# while(start_x <= x):
#     cnt += 1
#     T_1.forward(start_x)
#     T_1.left(90)
#     if(cnt == 2):
#         start_x += 5
#         cnt = 0

# T_1.hideturtle()
    





    










turtle.done()


