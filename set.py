color={"rojo","asul"}

print(color)
print("morado" in color)
color.add("verde")
print(color)

color.remove("asul") #fallo deseguridad inportante
print(color)

del color

color.clear()
print(color)

