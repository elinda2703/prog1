
"""
d = int (input("stupně"))
m = int (input("minuty"))
s = float (input("vteřiny"))
deg = d + m/60 + s/3600

if (d<-180 or d>180):
    print("stupně musí být v intervalu -180;180")
elif (m<0 or m>60):
    print ("minuty musí být v intervalu 0;60")
elif (s<0 or s>60):
    print ("vteřiny musí být v intervalu 0;60")
else:
    print(deg)

def deg():
    x = float(input("stupně jako desetinné číslo"))
    a = int(x)
    b_float = float(x-a)
    b = int((b_float)*60)
    c = float((b_float-int(b_float))*60)
    print(a,"°",b,"'",c,"''")

deg()
"""