deom =[1 ,3 ,4, True ,[2,5] ]
color=["rojo","azul","verde"]
print(color)

numbersList=list((1,2,4))
print(numbersList)
print(type(numbersList))

rangList=list(range(1,10))
print(rangList)

print(type(color))
print(dir(color))

print(len(color))
print(deom[3])

print([2,5] in deom)
print("Blanco" in color)

# 
color[1]="amarillo"
# 

# 
color.append("violeta")               #meter un elemento
color.extend(("negro","naranja"))     #meter varios elementos

color.insert(len(color) ,"maron")


color.pop()

color.remove("verde")

color.clear()

print(color.index("rojo"))
print(color)

