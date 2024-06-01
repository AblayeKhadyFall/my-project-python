from datetime import datetime
from typing import List
from membre import Membre 
class Tache:
    def __init__(self, nom: str, description: str, date_debut: str, date_fin: str, responsable: 'Membre', statut: str):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut if isinstance(date_debut, datetime) else datetime.strptime(date_debut, '%Y-%m-%d')
        self.date_fin = date_fin if isinstance(date_fin, datetime) else datetime.strptime(date_fin, '%Y-%m-%d')
        self.responsable = responsable
        self.statut = statut
        self.dependances = []
        self.date_debut_tot = None
        self.date_fin_tot = None
        self.date_debut_tard = None
        self.date_fin_tard = None
        
    def ajouter_dependance(self, tache: 'Tache'):
        if tache not in self.dependances:
            self.dependances.append(tache)
            
    def mettre_a_jour_statut(self, statut: str):
        self.statut = statut
        
    def afficher_details(self):
        print(f"  Tâche: {self.nom}")
        print(f"    Description: {self.description}")
        print(f"    Date de début: {self.date_debut}")
        print(f"    Date de fin: {self.date_fin}")
        print(f"    Responsable: {self.responsable.nom}")
        print(f"    Statut: {self.statut}")
        print(f"    Dépendances: {[dep.nom for dep in self.dependances]}")
