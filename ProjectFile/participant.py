##############################################################
# Classe      : Participant
# Descritpion : voir dans la classe
# Par         : Patrik Artur Kabore 
##############################################################

#============= Importations =====================
import operator
import datetime
from datetime import datetime
from datetime import date
import sys
from personne import Personne

class Participant(Personne):
    def __init__(self, p_nom, p_prenom:str, p_sexe:str,p_naissance:date):
        super().__init__(p_nom, p_prenom, p_sexe,p_naissance)

    def formater_fichier(self):
        super().formater_fichier()
      
    
    
