#7
def verif():
    try:
        nombre = int(input("Entrez un nombre entier: "))
        
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")

    except ValueError:
        
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        # Appel récursif pour nouvelle entrée si saisie incorrecte
        verif()
verif()