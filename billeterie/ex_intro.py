# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py ex_intro.py"


# définition des variables 
nombrea = 6
nombreb = input("Saisir un nombre : ")

# verif si la saisie est bien un entier
try: nombreb=int(nombreb)
except ValueError:
    print("ceci n'est pas un entier")

#fonction qui calcule le résultat demandé
def exo (x1,x2):
    return 2*(x1+x2)

resultat = exo(nombrea, nombreb)

# affichage résultat utilisateur
if(resultat >= 20):
    print(nombrea , " " , nombreb)
    print("Le résultat est Enorme : " , resultat)

else :
    print(nombrea , " " , nombreb)
    print("le resultat est pas ouf : " , resultat)

#finito
    
