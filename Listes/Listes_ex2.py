#Ex2 :
suite1= list(range(11))
nombre = []

for i in suite1 :
    rslt = i*5
    nombre.append(f"5 x {i} = {rslt}")

for elmt in nombre:
    print(elmt)