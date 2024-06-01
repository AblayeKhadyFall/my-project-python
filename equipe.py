#from typing import Protocol
from membre import Membre 
class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre: 'Membre'):
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres
    def afficher_details(self):
        print(f"Équipe:")
        for membre in self.membres:
            print(f"  Membre: {membre.nom}, Rôle: {membre.role}")