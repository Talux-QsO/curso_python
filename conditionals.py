num =input("Numero:")

if int(num)<30:
    print(f"{num} Este numero es menor que 30")
    if int(num)<20:
        print(f"{num} Este numero es menor que 20")
elif int(num)==30:
    print("Es 30")
else:
    print(f"{num} Este numero es mayor que 30 ")

