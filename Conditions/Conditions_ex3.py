#3
from datetime import datetime

aujourdhui = datetime.today().strftime("%A")
print(aujourdhui)

match aujourdhui: 
    case "Monday" : print("Nous sommes Lundi.")
    case "Tuesday" : print("Nous sommes Mardi.")
    case "Wednesday" : print("Nous sommes Mercredi.")
    case "Thursday" : print("Nous sommes Jeudi.")
    case "Friday" : print("Nous sommes Vendredi.")
    case "Saturday" : print("Nous sommes Samedi.")
    case "Sunday" : print("Nous sommes Dimanche.")
    case _ : print("Jour inconnu.")
