from random import randrange



x=randrange(10)


while x:
    y=int(input("zadej číslo"))
    if (x<y):
        print ("moc velké")
    elif(x>y):
        print("moc malé")
    else:
        print("jjjjj")
        break    

print("nnnnnn")

name="Kvido"
age=58
astr= f"Ahoj {name}, {age} starý"
print(astr)

