import os
import random

# Définition des données du jeu

personnage = {
    "Nom": "",
    "Age": 0,
    "Sexe": "",
    "PV": 70,
    "Objets clés": ["smartphone"],
    "Inventaire": {}
}

lieux = {
    "hall": {
        "description": "Tu te trouves dans le hall d'entrée de l'école.",
        "actions": ["observer", "quitter", "classe 1-a", "couloir 1"]
    },
    "classe 1-a": {
        "description": "C'est la salle de classe 1-A.",
        "actions": ["observer", "parler", "hall", "couloir 1"]
    },
    "couloir 1": {
        "description": "C'est le couloir du rez de chaussée.",
        "actions": ["observer", "inspecter", "classe 1-a", "hall", "monter"]
    },
    "couloir 1er étage": {
        "description": "Tu te trouves dans le couloir du premier étage.",
        "actions": ["observer", "descendre", "salle d'entrainement", "cafétéria", "toit"]
    },
    "salle d'entrainement": {
        "description": "C'est la salle d'entrainement.",
        "actions": ["observer", "combattre", "couloir 1er étage"]
    },
    "cafétéria": {
        "description": "C'est la cafétéria du premier étage.",
        "actions": ["observer", "prendre repas", "couloir 1er étage"]
    },
    "toit" : {
    "description": "Tu te trouves sur le toit de l'école. Il y a une vue magnifique depuis ici.",
    "actions": ["observer", "descendre", "parchemin"]
    }
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

plats = {
    "Ramen": 10,
    "Onigiri": 15,
    "Udon": 20,
    "Curry": 25
}

swords_power = list(epee.values())
swords_name = list(epee.keys())
parchemin_remis = False  
carte_remis = False

# Fonctions utilitaires

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_actions(actions):
    print("Actions disponibles :")
    for action in actions:
        print(f"- {action.capitalize()}")

def quitter_jeu():
    print("Merci d'avoir joué !")
    exit()

def lancer_combat():
    points_de_vie = random.randint(3, 15)
    print(f"Tu combats le mannequin d'entrainement et lui infliges {points_de_vie} points de dégâts.")
    personnage["PV"] -= points_de_vie

def verif_digit(digit):
    if digit.isdigit():
        digit = int(digit)
        return True
    else:
        print("Tu as du mal comprendre ... Je répète : ")
        return False

# Fonctions de jeu pour chaque lieu
def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")
    while True:
        while True:
            print("\nQuel âge as-tu ?")
            age = input("├─> ")
            if verif_digit(age) == True:
                break

        print("Très bien ! Et maintenant, comment t'appelles-tu ?")
        name = input("├─> ").lower()
        while True:
            print("Parfait. Es-tu un garçon ou une fille ? ")
            gender = input("├─> ").lower()
            if gender == "garcon" or gender == "fille":
                personnage["Sexe"] = gender
                break
            else:
                print("Tu as du mal comprendre ... Je répète : ")
        while True:
            print(f"Formidable {name} ! Une dernière question, souhaites-tu jouer en mode facile ou difficile ?")
            difficulty = input("├─> ").lower()
            if difficulty == "facile" or difficulty == "difficile":  # Correction ici
                break
            else:
                print("Tu as du mal comprendre ... Je répète : ")

        if gender == "garcon" or gender == "garçon":
            print(f"Je résume donc la situation : Tu t'appelles {name} \nTu es un garçon de {age} ans et tu souhaites commencer en {difficulty} c'est bien cela ? \n")
        elif gender == "fille":
            print(f"Je résume donc la situation : Tu t'appelles {name} \nTu es une fille de {age} ans et tu souhaites commencer en {difficulty} c'est bien cela ? \n")
        else:
            print()
        print("| oui <> non")
        choice = input("├─> ").lower()
        if choice == "oui":
            personnage["Pseudo"] = name
            personnage["Age"] = age
            if difficulty == "facile":
                personnage[swords_name[1]] = swords_power[1]

            else:
                personnage[swords_name[0]] = swords_power[0]
            print(" : ", personnage)
            input()
            break
        else:
            print("Bon reprenons depuis le début veux-tu ?")
    while True:
        lieu_hall()
    


def lieu_hall():
    while True:
        clear_screen()
        print(lieux["hall"]["description"])
        afficher_actions(lieux["hall"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu regardes autour de toi mais rien d'intéressant à signaler.")
            input()
        elif action == "quitter":
            quitter_jeu()
        elif action == "classe 1-a":
            lieu_classe1a()
        elif action == "couloir 1":
            lieu_couloir1()
        else:
            print("Action invalide.")

def lieu_classe1a():
    global parchemin_remis
    global carte_remis

    while True:
        clear_screen()
        print(lieux["classe 1-a"]["description"])
        afficher_actions(lieux["classe 1-a"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("La salle de classe est calme, le professeur semble concentré sur son cours.")
            input()
        elif action == "parler":
            if carte_remis == False:
                print("Tu entames une conversation avec le professeur.")
                print("Après une discussion enrichissante, le professeur te remet une carte d'entraînement !")
                personnage["Objets clés"].append("Carte d'entraînement")
                carte_remis = True
                input()
            else:
                print("Tu discutes un moment avec le professeur, mais il ne semble rien avoir de nouveau à te donner.")
                input()
        elif action == "hall":
            if parchemin_remis == False:
                print("Alors que tu te diriges vers la sortie, le professeur t'interpelle :")
                print("Ah, j'ai presque oublié ! Prends ce parchemin, il pourrait t'être utile.")
                personnage["Objets clés"].append("Parchemin")
                parchemin_remis = True
                input()
            lieu_hall()
        elif action == "couloir 1":
            lieu_couloir1()
        else:
            print("Action invalide.")


def lieu_couloir1():
    while True:
        clear_screen()
        print(lieux["couloir 1"]["description"])
        afficher_actions(lieux["couloir 1"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu vois des casiers alignés le long du couloir.")
            input()
        elif action == "inspecter":
            print("Tu inspectes les casiers mais tu ne trouves rien d'intéressant.")
        elif action == "classe 1-a":
            lieu_classe1a()
        elif action == "hall":
            lieu_hall()
        elif action == "monter":
            lieu_couloir1erEtage()
        else:
            print("Action invalide.")

def lieu_couloir1erEtage():
    while True:
        clear_screen()
        print(lieux["couloir 1er étage"]["description"])
        afficher_actions(lieux["couloir 1er étage"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu observes attentivement le couloir.")
            input()
        elif action == "descendre":
            lieu_couloir1()
        elif action == "salle d'entrainement" or action == "salle":
            lieu_salle_entrainement()
        elif action == "cafétéria" or action == "cafeteria":
            lieu_cafeteria()
        elif action == "toit":
            lieu_toit()  # Accéder au toit depuis le couloir du premier étage
        else:
            print("Action invalide.")

def lieu_salle_entrainement():
    while True:
        clear_screen()
        print(lieux["salle d'entrainement"]["description"])
        afficher_actions(lieux["salle d'entrainement"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu observes attentivement la salle d'entrainement.")
            input()
        elif action == "combattre":
            lancer_combat()
        elif action == "couloir":
            lieu_couloir1erEtage()
        else:
            print("Action invalide.")

def lieu_cafeteria():
    while True:
        clear_screen()
        print(lieux["cafétéria"]["description"])
        afficher_actions(lieux["cafétéria"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu observes attentivement la cafétéria.")
            input()
        elif action == "prendre repas":
            prendre_repas()
        elif action == "couloir":
            lieu_couloir1erEtage()
        else:
            print("Action invalide.")
            
def lieu_toit():
    while True:
        clear_screen()
        print(lieux["toit"]["description"])
        afficher_actions(lieux["toit"]["actions"])

        action = input("Que veux-tu faire ? ").lower()
        if action == "observer":
            print("Tu observes la vue depuis le toit.")
            input()
        elif action == "descendre":
            lieu_couloir1erEtage()
        elif action == "parchemin" and parchemin_remis:
            ouvrir_parchemin()  
        else:
            print("Action invalide.")

def prendre_repas():
    max_repas = 2
    nb_repas = len(personnage["Inventaire"])

    if nb_repas < max_repas:
        plat = random.choice(list(plats.keys()))
        personnage["Inventaire"][plat] = plats[plat]
        print(f"Tu as pris un {plat} dans la cafétéria.")
        input()
    else:
        print("Tu ne peux pas prendre plus de repas.")
        input()

def lancer_combat():
    mannequin_pv = 70
    degats_min = 3
    degats_max = 10
    epée_equipée = ""
    
    if "Badge d'entraînement" in personnage["Objets clés"]:
        mannequin_pv = 120
        degats_min = 6
        degats_max = 15
    elif "Deuxième badge d'entraînement" in personnage["Objets clés"]:
        mannequin_pv = 200
        degats_min = 10
        degats_max = 20
    
    for epée in swords_name:
        if epée in personnage:
            epée_equipée = epée
            break
    
    print("Tu entres en combat contre le mannequin d'entraînement !")

    while mannequin_pv > 0 and personnage["PV"] > 0:
        print(f"Points de vie du mannequin : {mannequin_pv}")
        print(f"Tes points de vie : {personnage['PV']}")

        choix = input("Que veux-tu faire ? (taper/fuir/manger) ").lower()

        if choix == "taper":
            degats = random.randint(epee[epée_equipée], epee[epée_equipée] * 2)  # Utilisation de la valeur de l'épée
            print(f"Tu attaques le mannequin et lui infliges {degats} points de dégâts !")
            mannequin_pv -= degats
        elif choix == "fuir":
            print("Tu décides de fuir le combat et de retourner dans la salle d'entraînement.")
            print("Le mannequin te regarde partir, déçu de ton manque de courage.")
            input()
            lieu_salle_entrainement()  # Retour à la salle d'entraînement
        elif choix == "manger":
                if len(personnage["Inventaire"]) > 0:
                    print("Tu prends une pause pour manger quelque chose.")
                    print("Voici ce que tu as dans ton inventaire :")
                    for item, value in personnage["Inventaire"].items():
                        print(f"- {item} ({value} PV)")
                    choix_nourriture = input("Que veux-tu manger ? ").capitalize()
                    if choix_nourriture in personnage["Inventaire"]:
                        pv_plus = personnage[plats.values(choix_nourriture)]
                        pv_regenere = personnage["PV"] + pv_plus  # Régénère jusqu'au maximum de 70 PV
                        print(f"Tu manges {choix_nourriture} et récupères {pv_regenere} points de vie.")
                        personnage["PV"] += pv_regenere
                        del personnage["Inventaire"][choix_nourriture]
                    else:
                        print("Tu n'as pas cette nourriture dans ton inventaire.")
                else:
                    print("Tu n'as pas de nourriture dans ton inventaire.")
        else:
            print("Action invalide. Choisis entre taper, fuir ou manger.")
            continue

        if mannequin_pv > 0:
            print("Le mannequin riposte !")
            degats = random.randint(degats_min, degats_max)
            print(f"Le mannequin t'inflige {degats} points de dégâts !")
            personnage["PV"] -= degats

        input()

    if personnage["PV"] <= 0:
        print("Tu es vaincu... Game Over.")
        quitter_jeu()
    else:
        print("Félicitations ! Tu as vaincu le mannequin d'entraînement.")
        if "Badge d'entraînement" not in personnage["Objets clés"]:
            print("En récompense, tu obtiens un badge d'entraînement !")
            personnage["Objets clés"].append("Badge d'entraînement")
        elif "Deuxième badge d'entraînement" not in personnage["Objets clés"]:
            print("En récompense, tu obtiens un deuxième badge d'entraînement !")
            personnage["Objets clés"].append("Deuxième badge d'entraînement")
        else:
            print("Tu as déjà remporté tous les badges d'entraînement !")
        
        # Ajout de 20 points de vie supplémentaires
        personnage["PV"] += 20 

        if epée_equipée:
            # Ajout de 5 points de dégâts supplémentaires à l'épée
            epee[epée_equipée] += 5  

        input()

def ouvrir_parchemin():
    if "Parchemin" in personnage["Objets clés"]:
        print("Tu ouvres le parchemin...")
        print("Sur le parchemin, il est écrit : 'Pour obtenir une puissante épée, choisis judicieusement.'")
        print("Une liste d'épées est dessinée en dessous.")
        print("Tu peux choisir parmi les épées suivantes :")
        for i, epée in enumerate(swords_name, 1):
            print(f"{i}. {epée}")
        
        choix_epée = input("Quelle épée choisis-tu ? (entrez le numéro correspondant) ")
        if choix_epée.isdigit():
            choix_epée = int(choix_epée)
            if 1 <= choix_epée <= len(swords_name):
                epée_choisie = swords_name[choix_epée - 1]
                print(f"Tu as choisi l'épée {epée_choisie}.")
                personnage[epée_choisie] = epee[epée_choisie]  # Équiper le personnage avec l'épée choisie
                input
            else:
                print("Choix invalide.")
                input()
        else:
            print("Choix invalide.")
            input()
    else:
        print("Tu ne possèdes pas de parchemin pour ouvrir.")


# Boucle principale du jeu

def jeu():
    intro()
    

if __name__ == "__main__":
    jeu()
