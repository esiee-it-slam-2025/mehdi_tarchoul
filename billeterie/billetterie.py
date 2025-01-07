import os

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
nb_billets_adulte = 0
nb_billets_reduit = 0
path = ""
travel = 0 
num_zone = ""
price = 0
prix_unit = 0
prix_r_unit = 0

#fonction pour clear console 
def clear():
    os.system('cls')

#fonction de vérification d'entrée utilisateur
def verifydigit():
    while True:
        digit = input("Saisir la valeur : ")
        if digit.isdigit():
            return int(digit)

#fonction qui demande à l'utilisateur son trajet afin de calculer la distance et déterminer la voie à prendre
def ask_distance():
    total_distance = 0
    total_rdistance = 0
    for index, names in enumerate(stations):
        print(f"{index} - {names}")
    print("De quelle station allez-vous partir ?")
    start_station = verifydigit()
    print("Vers quelle station allez-vous ?")
    end_station = verifydigit()

    if start_station < end_station:
        path = "1"
        for index in range(start_station, end_station):
            total_distance += stations_distances[index]
        return total_distance, path
    elif start_station > end_station:
        path = "2"
        inverted_stations = list(stations)
        inverted_stations.reverse()
        start_station = 13 - start_station
        end_station = 13 - end_station
        for index in range(start_station, end_station):
            total_rdistance += stations_distances[index]
        return total_rdistance, path

#fonction qui va déterminer la zone et calculer le tarif total en fonction de la distance et du nb de tickets
def att_zone(total_distance, adult_ticket, reduced_ticket):
    if total_distance <= 3:
        zone = "Zone 1"
        price = adult_ticket * 210 + reduced_ticket * 110
        unit_price = 210
        unit_r_price = 110
        return price, zone, unit_price, unit_r_price
    elif 3 < total_distance <= 7:
        zone = "Zone 2"
        price = adult_ticket * 260 + reduced_ticket * 130
        unit_price = 260
        unit_r_price = 130
        return price, zone, unit_price, unit_r_price
    elif 7 < total_distance <= 11:
        zone = "Zone 3"
        price = adult_ticket * 300 + reduced_ticket * 150
        unit_price = 300
        unit_r_price = 150
        return price, zone, unit_price, unit_r_price
    elif 11 < total_distance <= 15:
        zone = "Zone 4"
        price = adult_ticket * 340 + reduced_ticket * 170
        unit_price = 340
        unit_r_price = 170
        return price, zone, unit_price, unit_r_price

#fonction qui va demander le nombre de billet que l'utilisateur souhaite prendre
def ticket_number():
    print("Combien de billet adulte souhaitez-vous prendre ?")
    adult_ticket = verifydigit()
    print("Combien de billet à tarif réduit souhaitez-vous prendre ?")
    reduced_ticket = verifydigit()
    return adult_ticket, reduced_ticket

# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

# Questions à l'utilisateur
tickets = ticket_number()
nb_billets_adulte = tickets[0]
nb_billets_reduit = tickets[1]
input("Suivant....")
clear()

# Calculs de l'itinéraire
distance = ask_distance()
travel = distance[0]
path = distance[1]
input("Suivant....")
clear()

# Choix de la bonne zone tarifaire et coût total
zone = att_zone(travel, nb_billets_adulte, nb_billets_reduit)
price = zone[0]
num_zone = zone[1]
prix_unit = zone[2]
prix_r_unit = zone[3]
input("Suivant....")
clear()

# Affichage des détails du voyage et du tarif
print("Voici le détail de votre voyage : \n")
print(f"{nb_billets_adulte} billets tarif adulte à {prix_unit} yen par billet, \n{nb_billets_reduit} billet tarif réduit à {prix_r_unit} yen par billet,\n")
print(f"Total : {price} yen\n")
print(f"Zone : {num_zone}\n")
print(f"Voie n°{path}\n")
print("Bon Voyage !!")