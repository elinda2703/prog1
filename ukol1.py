from turtle import forward,left,right,penup,pendown,speed,exitonclick,circle,setposition,color,pensize
from math import sqrt
#speed(1)

#nakreslí hrací pole
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

#nakreslí kolečko
def kolecko(a,b,d):
    penup()
    while(True):        #kontrola (ne)platných vstupů
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

#nakreslí křížek
def krizek(a,b,d):
    penup()
    while(True):        #kontrola (ne)platných vstupů
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

#výsledná funkce
def piskvorky(a,b,d):
    hraci_pole(a,b,d)
    pensize(3)
    for l in range(int(a*b/2)):
        kolecko(a,b,d)
        krizek(a,b,d)
    if (a*b%2==1):          #hráč 1 (kolečko) hraje o kolo navíc, pokud má hrací pole lichý počet políček
        kolecko(a,b,d)
    exitonclick()
piskvorky (int(input("zadej počet řádků")),int(input("zadej počet sloupců")),int(input("zadej velikost políčka")))