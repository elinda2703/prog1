from turtle import forward,left,right,penup,pendown,speed,exitonclick,circle,setposition
#speed(1)
def piskvorky(a,b,d):
    for j in range (b):
        for i in range (a):
            for k in range (4):
                forward (d)
                left (90)
            forward(d)
        left(180)
        forward(a*d)
        right(90)
        forward(d)
        right(90)
    for l in range(int(a*b/2)):
        penup()
        x1=int(input("hráči 1, zadej x"))
        y1=int(input("hráči 1, zadej y"))
        setposition((x1-1)*d+d/2,(y1-1)*d+d/6)
        pendown()
        circle(d/3)
        penup()
        x2=int(input("hráči 2, zadej x"))
        y2=int(input("hráči 2, zadej y"))
        setposition((x2-1)*d+d/6,(y2-1)*d+d/6)
        pendown()
        left(45)
        forward(2/3*d*1.41421)
        penup()
        right(135)
        forward(2*d/3)
        pendown()
        right(135)
        forward(2/3*d*1.41421)
        right(135)
    if (a*b%2==1):
        penup()
        x1=int(input("hráči 1, zadej x"))
        y1=int(input("hráči 1, zadej y"))
        setposition((x1-1)*d+d/2,(y1-1)*d+d/6)
        pendown()
        circle(d/3)
        penup()
piskvorky (2,2,50)