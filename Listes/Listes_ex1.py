
#Ex1 :
liste = [1,2,3,4,5,8]
suite= list(range(11))
print(suite)

for elmt in liste :
    table = [elmt * i for i in suite]
    print(f"Table de {elmt}: {table}")

    
#Ex1/ meth avec map :
liste3 = [1,2,3,4,5,8]
def myfunc(a) :
    return[a*i for i in range(11)]
print(list(map(myfunc,liste3)))

#ex1 map avec fonction lambda
liste4 = [1,2,3,4,6]
print(list(map(lambda x : [x*i for i in range(11)],liste4)))