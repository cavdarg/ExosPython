# 1/ My Python code forever

# 2 / My Python code 
#every day

# 3 / Types de variables
a = 2
b = 2.3
c = 'Hello'
d = True
lst1 = [2,3,8,9]
lst2=['Jean', 'Alice', 'Marc']
tpl1 = ('France','Italie','Allemagne')
tpl2 = (6,8,9)
ens = {5,6,8,9}
dict1 = {'Pays' : 'Allemagne', 'Capitale': 'Berlin'}
rien = None

# 4 / Nombre de caractères
my42count = 'quarante-deux'
print(len (my42count))


# 5 / Existence variable
existe = globals().get('c') or 42
print(existe)

# 6/ Tableau
myArray42 = ['q','u','a','r','a','n','t','e','-','d','e','u','x']

# 7 / Nombre d'index 
myArray42Len = len(myArray42)
print(myArray42Len)


# 8 / Recomposer tableau en String
str1 = "".join(myArray42)
print (f'La grande réponse sur la vie, l’univers et le reste ! {str1}')


# 9 / Aléatoire
from random import randint

rand = randint(1,42)
print(rand)
resultat = rand == 42
print(resultat)


# 10 /
my42Type = type
my42Type(a)


# 11 / Transformer Int en String
compute42= 42*1
Trans = str(compute42)
print(type(Trans))
print(Trans)

# 12 / String 

Suite42 = '42424242'
remplace = Suite42.replace('42','quarante-deux')
print(remplace)

# 13 / Transfert
a=24
b=42
c=a
d=b
a=d
b=c
print(a)
print(b)


