from math import sqrt

print(1+4)
print(1.2)
print("hello")
print("2+2=",2+2)
a = int(input("zadej koeficient a"))
b = int(input("zadej koeficient b"))
c = int(input("zadej koeficient c"))

d=int(b*b-4*a*c)

if (d<0):
    print("kvadratická rovnice nemá řešení")
elif (d==0):
    print("kořenem rovnice je",-b/(2*a))
else:
    print("kořeny rovnice jsou",(-b+sqrt(d))/(2*a), "a",(-b-sqrt(d))/(2*a))

r=1
print("Kružnice o poloměru",r,"má obvod",2*3.14*r,"a obsah",3.14*r*r)
