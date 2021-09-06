from datetime import date
from participant import Participant
from personne import Personne
from intervenant import Intervenant

def creer_date(p_chaine_date:str, p_carac:str)-> date :
    try:

        element = ""        # tableau de str
                            # contenant les éléments d'une date
        jour = 0            # int
        mois = 0            # int
        annee = 0           # int
                            
        element = p_chaine_date.split(p_carac)
        jour = int(element[0])
        mois = int(element[1])
        annee = int(element[2])

        return date(annee, mois, jour)
    except ValueError:
        print("\n La date n'est pas de type date !")
        
def ajouter_participant(p_choix)-> Participant :

    nom = ""                # str
    prenom = ""             # str
    sexe = ""               # str
    naissance_saisie = ""    # str date de naissance saisie
    naissance = None        # date date de naissance convertie en date
    if p_choix=="p":  
        nom = input("Nom du participant : ")
        prenom = input("Prénom du participant : ")
        sexe = input("Sexe du participant : ")
        naissance_saisie = input("Date de naissance du participant (jour/mois/annee): ")
    else:
        nom = input("Nom de l'intervenant  : ")
        prenom = input("Prénom de l'intervenant : ")
        sexe = input("Sexe de l'intervenant : ")
        naissance_saisie = input("Date de naissance de l'intervenant (jour/mois/annee): ")
    naissance = creer_date(naissance_saisie, "/")
    if p_choix=="p":    
        return Participant(nom, prenom, sexe, naissance)
    else:
        return Intervenant(nom, prenom, sexe, naissance)

def effacer_participant(p_participants:str) :
    code = ""           # str
    participant = None  # participant
    
    code = input("Code de la personne à effacer : ")
    participant = chercher_participant(code, p_participants)

    if participant != None :
        print("\nParticipant : ", participant, " effacé \n")
        p_participants.remove(participant)
    else :
        print("\nLe participant n'existe pas dans le répertoire\n")

def chercher_participant(p_code:str, p_participants) :

    element = ""    # str

    participant = None # Participant
    
    for element in p_participants :

        if element.get_code() == p_code :
            participant = element
            break;

    return participant

def afficher_participant_age(p_participants:Participant) :

    element = ""    # str
    age = 0         # int

    age = int(input("Age minimal pour l'activité : "))
    
    for element in p_participants :
        if element.calculer_age() >= age :
            print("\t:", element)

    print("\n")

def personnes_total(p_participant,p_intervenant):
    personnes=list()
    personnes.extend(p_participant)
    personnes.extend(p_intervenant)
    return personnes
