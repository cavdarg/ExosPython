#ex3 :

def detectMyAgeByNight (age) :
    age = int(age)
    if age<18 :
        r=  f'Vous ne pouvez pas entrer, vous avez {age} ans'
    elif age > 41 :
        r= 'Vous êtes patron'
    else :
        r= f'Vous pouvez entrer, vous avez {age} ans'
    return r

age = int(input("Quel est votre âge ?"))
age1 = detectMyAgeByNight(age)
print(age1)




 
















































































