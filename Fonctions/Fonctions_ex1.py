#Ex1 :
def myPutStr(mot):
    if isinstance(mot, (int, float)):
        return "Et pourquoi pas 42?"
    return str(mot)

resultat = myPutStr("a")
resultat1 = myPutStr(10)
print (resultat)
print (resultat1)