t = int(input("please tell the temperature :- "))

if t < 0:
    print("Freezing cold")
elif t >= 0 and t<10:
    print("Very cold")
elif t >= 10 and t<20:
    print("Cold")
elif t >= 20 and t<30:
    print("Plesant")
elif t >= 30 and t<40:
    print("hot")
else:
    print("temperature is very hot")