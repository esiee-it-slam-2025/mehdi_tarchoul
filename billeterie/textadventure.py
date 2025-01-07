import os

personnage = {
    "PV": 70
}

epee = {
    "Epee simple": 5,
    "Kiba": 10,
    "Kabutowari": 15,
    "Shibuki": 20,
    "Nuibari": 25,
    "Hiramekarei": 35,
    "Kubikiribosh": 45,
    "Samehada": 70,
}

hall = [
    "Observer"
    "Quitter"
    "Classe 1-A"
    "Couloir 1"
]

Classe1a = [
    "Observer"
    "Parler"
    "Hall"
    "Couloir 1"
]

Couloir1 = [
    "Observer"
    "Inspecter"
    "Classe 1-A"
    "Hall"
    "Monter (RDC+1)"
]

swords_power = list(epee.values())
swords_name = list(epee.keys())
personnage_key = list(epee.keys())
personnage_value = list(epee.values())

plats = "Ramen,Onigiri,Udon,Curry"  # À transformer en liste

plats_stock = {}  # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************


def proposer_lieux(mots_cles):
    message = "│[Lieux] "
    # A remplir ici
    print(message)
    print(mots_cles)


def proposer_actions(actions):
    message = "│[Actions] "
    # A remplir ici
    print(message)
    print(actions)

def verif_digit(digit):
    if digit.isdigit():
        digit = int(digit)
        return True
    else :
        print("Tu as du mal comprendre ... Je répète : ")
        return False
        
def quit():
    return exit()

def choices(place ,counter):
    while True:
        if place == 1 :
            print("┌────────────────────────────────────────")
            proposer_actions(f"| - {hall[0]}") 
            print(f"| - {hall[1]}")
            proposer_lieux(f"| - {hall[2]}")  
            print(f"| - {hall[3]}")
            print("└────────────────────────────────────────")
            reponse = input("├─> ")
            return reponse.lower()
        if place == 2 :
            print("┌────────────────────────────────────────")
            proposer_actions(f"| - {Couloir1[0]}") 
            if counter == 1:
                print(f"| - {Couloir1[1]}")
            proposer_lieux(f"| - {Couloir1[2]}")  
            print(f"| - {Couloir1[3]}")
            print(f"| - {Couloir1[4]}")
            print("└────────────────────────────────────────")
            reponse = input("├─> ")
            return reponse.lower()
        if place == 3 :
            print("┌────────────────────────────────────────")
            proposer_actions(f"| - {Classe1a[0]}") 
            print(f"| - {Classe1a[1]}")
            proposer_lieux(f"| - {Classe1a[2]}")  
            print(f"| - {Classe1a[3]}")
            print("└────────────────────────────────────────")
            reponse = input("├─> ")
            return reponse.lower()
        if place == 4 : 
            print("┌────────────────────────────────────────")
            proposer_actions(f"| - {hall[0]}") 
            print(f"| - {hall[1]}")
            proposer_lieux(f"| - {hall[2]}")  
            print(f"| - {hall[3]}")
            print(f"| - {hall[4]}")
            print("└────────────────────────────────────────")
            reponse = input("├─> ")
            return reponse.lower()
# ********************************************************************************
# INTRODUCTION
# ********************************************************************************
def clear():
    os.system('cls')

def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")
    while True :
        
        while True:
            print("\nQuel âge as-tu ?")
            age = input("├─> ")
            if verif_digit(age) == True :
                break
            

        print("Très bien ! Et maintenant, comment t'appelles-tu ?")
        name = input("├─> ").lower()
        while True :    
            print("Parfait. Est-tu un garçon ou une fille ? ")
            gender = input("├─> ").lower()
            if gender == "garcon" or gender == "garçon" or gender == "fille":
                personnage["Sexe"] = gender
                break
            else:
                print("Tu as du mal comprendre ... Je répète : ")
        while True : 
            print(f"Formidable {name} ! Une dernière question, souhaites-tu jouer en mode facile ou difficile ?")
            difficulty = input("├─> ").lower()
            #breakpoint()
            if difficulty == "facile" or difficulty == "facil" or difficulty == "façile" or difficulty == "difficile" or difficulty == "dificile" or difficulty == "difficille" or difficulty == "difficil" : 
                break
            else : 
                print("Tu as du mal comprendre ... Je répète : ")

        if gender == "garcon" or gender == "garçon" : 
            print(f"Je résume donc la situation : Tu t'appelles {name} \nTu es un garçon de {age} ans et tu souhaites commencer en {difficulty} c'est bien cela ? \n")
        elif gender == "fille" :
            print(f"Je résume donc la situation : Tu t'appelles {name} \nTu es une fille de {age} ans et tu souhaites commencer en {difficulty} c'est bien cela ? \n")
        else:
            print()
        print("| oui <> non")
        choice = input("├─> ").lower()
        if choice == "oui" :
            personnage["Pseudo"] = name
            personnage["Age"] = age
            if difficulty == "facile" :
                personnage[swords_name[0]] = swords_power[0]
                
            else :
                personnage[swords_name[1]] = swords_power[1]   
                
            print(" : ",personnage)
            input()
            break
        else : 
            print("Bon reprenons depuis le début veux-tu ?")

        
            
        

    
    # Demander un âge et écrire cette information dans le dictionnaire "personnage"

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"

    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"

    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************


def lieu_hall():
    clear()
    place = 1
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    reponse = choices(place, counter).lower()
    counter = 0

    if reponse == "quitter" or reponse == "quiter" or reponse == "quieter":
        quit()
    elif reponse == "couloir1" or reponse == "coulior1" or reponse == "couloir 1" or reponse == "coulior 1":
        lieu_couloir_rdc()
    elif reponse == "classe 1-a" or reponse == "classe 1" or reponse == "classe 1a" or reponse == "classe1a" or reponse == "calsse 1-a" or reponse == "calsse 1a" or reponse == "calsse1a":
        lieu_classe1a_rdc()
    elif reponse == "observer" or reponse == "osberver" or reponse == "obverser" or reponse == "observe":
        print(f"{personnage_value[2]} tu n'y verras que de banales casiers ainsi qu'un groupe d'étudiants entrain de bavarder")
    # Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non


def lieu_couloir_rdc():
    clear()
    place = 2
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du rez de chaussé.")
    print("On y trouve entre autres la couloir.")
    reponse = choices(place,counter).lower()

    if reponse == "hall" or reponse == "hlal" or reponse == "hal" or reponse == "halll":
        lieu_hall()
    elif reponse == "classe 1-a" or reponse == "classe 1" or reponse == "classe 1a" or reponse == "classe1a" or reponse == "calsse 1-a" or reponse == "calsse 1a" or reponse == "calsse1a":
        lieu_classe1a_rdc()
    elif reponse == "observer" or reponse == "osberver" or reponse == "obverser" or reponse == "observe":
        print(f"{personnage_value[2]} Le couloir est humide et froid. Il y a cependant plusieurs fissures dans le mur à ta gauche.") 
        counter = 1
    elif reponse == "inspecter" or reponse == "inspecte" or reponse == "insepcter" or reponse == "inspetcer":
        if "parchemin maudit" not in objets_cles:
            print("Tu décides de regarder à l'intérieur d'une des fissures et tu trouves un parchemin maudit !\n Tu le range dans ton sac à objets clés. ")
        else:
            print("Il n'y a plus rien à trouver ici")


def lieu_classe1a_rdc():
    clear()
    place = 3
    counter = 0
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la salle de classe 1-A.")
    print("Un professeur, assis devant son bureau entrain de bouquiner, vous fixe du coin du regard.")
    reponse = choices(place, counter)


# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
