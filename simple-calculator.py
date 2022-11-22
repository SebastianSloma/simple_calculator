wybór = input("dodawanie, odejmowanie. mnożenie, dzielenie: ")

a = int(input("pierwsza liczba: "))
b = int(input("druga liczba: "))

if (wybór == "dodawanie"):
    print(a + b)
elif(wybór == 'odejmowanie'):
    print(a - b)
elif(wybór == 'mnożenie'):
    print(a * b)
elif(wybór == 'dzielenie'):
    print(a / b)
else:
    print("zły wybór")