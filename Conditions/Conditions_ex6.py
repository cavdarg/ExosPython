#6
prixInitial = float(input("Quel est le prix ?"))
pourcentage = float(input("Quel est le pourcentage de remise?"))
remise = (pourcentage/100)*prixInitial
prixRemisé= prixInitial - remise
print(prixRemisé)
if prixRemisé > prixInitial / 2:
    print(f"Montant de la remise : {pourcentage:.2f} €")
    print(f"Prix après remise: {prixRemisé:.2f} €")
else:
    # Affichage du message d'erreur
    print("La remise est trop élevée. Veuillez choisir un pourcentage de remise plus bas.")
