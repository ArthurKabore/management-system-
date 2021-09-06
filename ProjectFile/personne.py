##############################################################
# Classe      : Personne
# Descritpion : voir dans la classe
# Par         : Patrik Artur Kabore 
##############################################################

#============= Importations =====================
##
##import locale
##locale.setlocale(locale.LC_ALL, "fr_CA")
import operator
import datetime
from datetime import date
import sys


#--fonction pour valider les constructeurs
def contient_Nombres(p_string):
    return any(char.isdigit() for char in p_string)

def set_user_sex(p_sex_user):
    if p_sex_user == "m" or p_sex_user == "M":
        return p_sex_user == "M"
    elif p_sex_user == "f" or p_sex_user == "F":
        return p_sex_user == "F"

#============= Classe ===========================
import abc
class Personne(metaclass=abc.ABCMeta) :
    #-----------  Constructeur -----------------------------
    
    
    @abc.abstractmethod
    def __init__(self, p_nom, p_prenom:str, p_sexe:str,
                       p_naissance:date) :
        """
        Constructeur qui initialise les donnés membres.
           p_nom : est le nom du participant
           p_prenom : est le prénom du participant
           p_sexe : est le sexe du participant
           p_naissance : est la date de naissance du participant
        """
        #...... Déclaration des données membres ......
        self.__code = ""           # str (code d'identification du participant)
        self.__nom = ""            # str
        self.__prenom = ""         # str
        self.__sexe = ""           # str (H/F)
        self.__naissance = None    # date (date de naissance du participant)

        #-----Validations-----
        #appel a la fonction qui verifie les constructeurs
        if contient_Nombres(p_nom)==True: 
            raise TypeError("Le nom (et le prenom) ne peut contenir de numero(s)")
        
        if contient_Nombres(p_prenom)==True:
            raise TypeError("Le prenom ne peut contenir de numero(s)")

        if contient_Nombres(p_sexe)==True:
            raise TypeError("Parametre sexe invalide")

        try:    
            assert((isinstance(p_naissance, date)==True))
        except:
            raise ValueError("Erreur la naissance n'est pas de type date")
        try:
            set_user_sex(p_sexe)
        except:
            raise ValueError("Parametre sexe invalide")
        
        date_ajd=date.today()
        try:
            assert(p_naissance<date_ajd)
        except:
            raise ValueError("La date du participant ne doit pas etre dans le futur")
        #fin des tests
        
        #...... Affectation des valeurs ......
        self.__nom=p_nom
        self.__prenom = p_prenom
        self.__naissance = p_naissance
        self.__sexe = p_sexe
        self.creer_code()
        
        

    #----------- Opérations --------------------------------
    def formater_fichier(self):
        with open("personnes.txt") as f:
            donnee = f.read().splitlines()
        return donnee
   
    def creer_code(self)-> str:
        auj = None      # date d'aujourd'hui
        str_date = ""   # date du jour formatée
        str_nom = ""    # str 3 caractères majuscules du nom
        str_prenom = "" # str 1 caractère majuscule du prénom
        str_annee = ""  # str 2 derniers chiffres de l'année de naissance
        
        auj = date.today()
        str_date = auj.strftime("%d%m%y")

        str_nom = self.__nom[:3].upper()
        str_prenom = self.__prenom[0].upper()

        str_annee = self.__naissance.strftime("%y")
        
        self.__code = str_date + str_nom + str_prenom + str_annee

    def calculer_age(self, p_date:date = date.today()) -> int :
        """
        Calcul l'age du participant en année à la date passée
        en paramètre. Si aucune date n'est passée, la date par défaut
        est la date du jour.
        L'age n'est pas arrondi. L'age du participant
        augmente d'un an seulement à partir du jour de son anniversaire
        """

        age = 0 # int age en années

        age = p_date.year - self.__naissance.year

        if ((p_date.month < self.__naissance.month)
           or (p_date.month == self.__naissance.month
               and p_date.day < self.__naissance.day)) :
                age = age - 1 

        return age
   
    #-----------  Accesseur/mutateur  -----------------------

    def get_nom(self)-> str:
        """
        Retourne le nom du participant
        """
        return self.__nom

    def get_prenom(self)-> str:
        """
        Retourne le prenom du participant
        """
        return self.__prenom

    def get_sexe(self)-> str:
        """
        Retourne le sexe du participant
        """
        return self.__sexe

    def get_code(self)-> str:
        """
        Retourne le code du participant
        """
        return self.__code

    def get_naissance(self)-> date:
        """
        Retourne la date de naissance du participant
        """
        return self.__naissance

    def __eq__(self, autre:object)->bool :
        return self.__prenom == self.__prenom

    def __ne__(self, autre:object)->bool :
        return self.__prenom != self.__prenom

    def __lt__(self, autre:object)->bool :
        return self.__prenom < self.__prenom

    def __le__(self, autre:object)->bool :
        return self.__prenom <= self.__prenom

    def __gt__(self, autre:object)->bool :
        return self.__prenom > self.__prenom
    
    def __ge__(self, autre:object)->bool :
        return self.__prenom >= self.__prenom
    #-----------  Affichage  -------------------------------
    def __str__(self):
        """
        Formatte l'affichage selon le format:
           [#code] Prénom NOM (H/F) dateNaissance
        Exemple :
           [#bla] Paul Lemieux (H) 1978-01-02
        """
        s = " [#" + self.__code + "] " + self.__prenom + " " + \
            self.__nom + " (" + self.__sexe + ") " +  \
            self.__naissance.strftime("%d-%m-%Y")
        return s
    
    def __repr__(self):
        """
        Formatte l'affichage quand utilisé dans une liste
        """
        return self.__str__()+"\n"



