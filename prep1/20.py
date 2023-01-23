# #python program for printing "GFG" 
# #importing turtle modules 
# import turtle 

# #setting up workscreen 
# ws=turtle.Screen() 

# #defining turtle instance 
# t=turtle.Turtle() 

# #turtle pen will be of "GREEN" color 
# t.color("Green") 

# #setting width of pen 
# t.width(3) 


# #for printing letter "G" 
# for x in range(180): 
# 	t.backward(1) 
# 	t.left(1) 
# t.right(90) 
# t.forward(50) 
# t.right(90) 
# t.forward(30) 
# t.right(90) 
# t.forward(50) 


# #for printing letter "F" 
# t.penup() 
# t.goto(40,0) 
# t.pendown() 
# t.forward(110) 
# t.goto(40,0) 
# t.left(90) 
# t.forward(50) 
# t.penup() 
# t.goto(40,-50) 
# t.pendown() 
# t.forward(40) 


# #for printing letter "G" 
# t.penup() 
# t.goto(150,0) 
# t.pendown() 
# for x in range(180): 
# 	t.backward(1) 
# 	t.left(1) 
# t.right(90) 
# t.forward(50) 
# t.right(90) 
# t.forward(30) 
# t.right(90) 
# t.forward(50)


import turtle

# def circle(x):


        
        


T_1 = turtle.Turtle()

# T_1.penup()
# T_1.forward(100)
# T_1.left(90)
# T_1.pendown()
# T_1.forward(100)

for i in range(4):
    T_1.forward(100)
    T_1.right(90)

T_1.left(60)
T_1.forward(100)
T_1.right(120)
T_1.forward(100)


def roma(x, ):
    cnt = 1
    while(cnt <= 360):
        T_1.forward(1)
        T_1.right(0.05)
        cnt += 1
    



T_1.hideturtle() 
turtle.done()

