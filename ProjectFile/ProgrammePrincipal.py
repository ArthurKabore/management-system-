# Fichier : gestionParticipant.py
# Description : programme qui permet la gestion d'un répertoire de
#               participant
# Auteur : Patrik Artur Kabore

#======== Importation de librairies =======
import utilitaires
import sys
import datetime
from datetime import date
from personne import Personne
from participant import Participant
from intervenant import Intervenant

#sys.tracebacklimit = 0

#=============== Initiations =========
self=None

participant = list()   
intervenant = list()
personnes=list()
nouvelles_personnes=list()

q=0
p=0
u=5
ligne = ""              # str
x=0
i = 0                   # int compteur
choix = ""              # str choix du menu
code = ""               # str
indice = ""             # int position du participant dans la liste

menu = "Quelle opération voulez-vous effectuer ? \n \
        A - ajouter un participant \n \
        E - effacer un participant \n \
        L - afficher tous les particpants en age de participer \n \
        Q - Quitter \n"

#====== Formatage du fichier ==================
donnee=Personne.formater_fichier(self)

for y in donnee:
    ligne=donnee[x].split()
    if ligne[0]=="Participant:":
        ligne=ligne[1].split(';')
        element = ligne[3].split("/")

        jour = int(element[0])
        mois = int(element[1])
        annee = int(element[2])

        naissance=date(annee, mois, jour)
        participant.append(Participant(ligne[0],ligne[1],ligne[2],naissance))
    else:
        ligne=ligne[1].split(';')
        element = ligne[3].split("/")

        jour = int(element[0])
        mois = int(element[1])
        annee = int(element[2])
        
        naissance=date(annee, mois, jour)
        intervenant.append(Intervenant(ligne[0],ligne[1],ligne[2],naissance))
    x+=1

#==========Imprimerie des Personnes===================
personnes=utilitaires.personnes_total(participant,intervenant) #calcule le total de personnes

for ligne in donnee:
    print("Après création du participant ",i+1)
    print("   ", personnes[i])
    i += 1

    
print("\nAprès création de la liste :")
print(personnes, "\n")

#========= Menu ==========
while choix.title() != "Q" :
    choix = input(menu)
    if choix.title() == "A" :
        choix_personne=input("Inscrire un intervenant ou un participant (I/P) ?")
        while choix_personne!="p" and choix_personne!="i":
            choix_personne=input("Inscrire un intervenant ou un participant (I/P) ?")

        if choix_personne.lower()=="p":
            participant.append(utilitaires.ajouter_participant(choix_personne))
            print("\nAprès création de la personne",u,":")
            print("   ", participant[len(participant) - 1], "\n")
            u+=1
        elif choix_personne.lower()=="i":
            intervenant.append(utilitaires.ajouter_participant(choix_personne))        
            print("\nAprès création de la personne",u,":")
            print("   ", intervenant[len(intervenant) - 1], "\n")
            u+=1

    elif choix.title() == "E" :

        codeChoisis = ""
        complete = False
        while not complete:
            codeChoisis = input("\nCode de la personne à effacer: ")
            for i in range(0, len(personnes)-1):
                if personnes[i].get_code() == codeChoisis:
                    personne = personnes[i]
                    personnes.remove(i)
                    print("Personne:  ", personne, "\teffacé\n")
                    complete = True
        answer = ""
            
    elif choix.title() == "L" :
        utilitaires.afficher_participant_age(participant)
    elif choix.title() == "I":
        print(intervenant)
    elif choix.title() != "Q" :
        print("\nChoix invalide\n")

#===========Sortie du code==============
nouvelles_personnes=utilitaires.personnes_total(participant,intervenant)

#nouvelle liste de personnes dans un fichier
fichier_personnes=open("personnes_Nouvelles.txt", "w")
t=0
for lel in nouvelles_personnes:
    fichier_personnes.write(str(donnee[t]))
    fichier_personnes.write("\n")
    t+=1
fichier_personnes.close()

# Print a la sortie
print("\nListe à la sortie du menu :")
print(nouvelles_personnes, "\n")
       
        
    
    
