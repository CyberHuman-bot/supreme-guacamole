H = float(input("Enter your height in M : "))
W = float(input("Enter your weight in KG : "))
BMI = W/(H ** 2)
print(BMI)
if BMI < 18.5 :
    print("You are a tiny stick")
elif BMI <= 24.9 :
    print("You are a totally normal man (NOW TEACH ME REACT NATIVE TEL :077967663345)")
elif BMI <= 30 :
    print("YOU ARE ONE OF THE FATTEST MAN ALIVE")
else :
    print("YOU ARE THE FATTEST MAN ALIVE")