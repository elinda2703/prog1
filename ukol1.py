from turtle import forward,left,right,penup,pendown,speed,exitonclick,circle,setposition,color,pensize
from math import sqrt
#speed(1)
def hraci_pole(a,b,d):
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

def kolecko(a,b,d):
    penup()
    while(True):
        x1=int(input("hráči 1, zadej x"))
        y1=int(input("hráči 1, zadej y"))
        if (x1>a or y1>b or x1<=0 or y1<=0):
            print ("neplatný vstup")
        else:
            break
    setposition((x1-1)*d+d/2,(y1-1)*d+d/6)
    pendown()
    color('blue')
    circle(d/3)

def krizek(a,b,d):
        penup()
        while(True):
            x2=int(input("hráči 2, zadej x"))
            y2=int(input("hráči 2, zadej y"))
            if (x2>a or y2>b or x2<=0 or y2<=0):
                print ("neplatný vstup")
            else:
                break
        setposition((x2-1)*d+d/6,(y2-1)*d+d/6)
        pendown()
        color('red')
        left(45)
        forward(2/3*d*sqrt(2))
        penup()
        right(135)
        forward(2*d/3)
        pendown()
        right(135)
        forward(2/3*d*sqrt(2))
        right(135)

def piskvorky(a,b,d):
    hraci_pole(a,b,d)
    pensize(3)
    for l in range(int(a*b/2)):
        kolecko(a,b,d)
        krizek(a,b,d)
    if (a*b%2==1):
        kolecko(a,b,d)
piskvorky (int(input("zadej počet řádků")),int(input("zadej počet sloupců")),int(input("zadej velikost pole")))