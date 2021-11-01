from turtle import forward,left,right,penup,pendown,speed,exitonclick
def ctverec():
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(30)
    exitonclick()
#ctverec ()

def hexa():
    forward(30)
    left(60)
    forward(30)
    left(60)
    forward(30)
    left(60)
    forward(30)
    left(60)
    forward(30)
    left(60)
    forward(30)
    exitonclick()
#hexa()

#for i in range(10):
#        print(i)

def kytka():
    for i in range(6):
        forward (50)
        left(60)
        for j in range(6):
            forward(50)
            right(60)
#kytka()

def mrizka(a,b):
    for j in range (b):
        for i in range (a):
            for k in range (4):
                forward (60)
                left (90)
            forward(60)
        left(180)
        forward(a*60)
        right(90)
        forward(60)
        right(90)    
#mrizka (3,4)              
#speed(1)
def sestimrizka(a,b,d):
    for _ in range (b):
        for _ in range (a):
            for _ in range(7):
                forward(d)
                left(60)
            forward(d)
            right(60)
        right(120)
        for l in range (a):
            forward(d)
            right(60)
            forward(d)
            left (60)
        forward(d)
        left(60)
        forward(d)
        left(60)                        
sestimrizka(4,3,60)