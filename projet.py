from datetime import datetime
from typing import List
from notification_context import NotificationContext
from notification_strategy import NotificationStrategy 
from tache import Tache
from equipe import Equipe
from risque import Risque
from jalon import Jalon
from changement import Changement
from fpdf import FPDF
from membre import Membre 
class Projet:
    def __init__(self, nom: str, description: str, date_debut: str, date_fin: str):
        self.nom = nom
        self.description = description
        self.date_debut = datetime.strptime(date_debut, '%Y-%m-%d')
        self.date_fin = datetime.strptime(date_fin, '%Y-%m-%d')
        self.taches = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques = []
        self.jalons = []
        self.version = 0
        self.changements = []
        self.chemin_critique = []
        self.notification_context = None

    def set_notification_strategy(self, strategy: NotificationStrategy):
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: 'Membre'):
        self.equipe.ajouter_membre(membre)

    def definir_budget(self, budget: float):
        self.budget = budget

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)

    def enregistrer_changement(self, description: str):
        self.version += 1
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)

    def generer_rapport_performance(self):
        pass

    def calculer_chemin_critique(self):
        pass

    def notifier(self, message: str, destinataires: List['Membre']):
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
    def afficher_details(self):
        print(f"Projet: {self.nom}")
        print(f"Description: {self.description}")
        print(f"Date de début: {self.date_debut}")
        print(f"Date de fin: {self.date_fin}")
        print(f"Budget: {self.budget}")
        print(f"Version: {self.version}")
        print(f"Tâches:")
        for tache in self.taches:
            tache.afficher_details()
        print(f"Risques:")
        for risque in self.risques:
            risque.afficher_details()
        print(f"Jalons:")
        for jalon in self.jalons:
            jalon.afficher_details()
        print(f"Changements:")
        for changement in self.changements:
            changement.afficher_details()
        print(f"Équipe:")
        self.equipe.afficher_details()
        
    def calculer_chemin_critique(self):
        # Initialiser les dates au plus tôt et au plus tard
        for tache in self.taches:
            tache.date_debut_tot = self.date_debut
            tache.date_fin_tot = tache.date_debut_tot + (tache.date_fin - tache.date_debut)
            tache.date_debut_tard = self.date_fin
            tache.date_fin_tard = tache.date_debut_tard - (tache.date_fin - tache.date_debut)

        # Calculer les dates au plus tôt
        for tache in self.taches:
            for dependance in tache.dependances:
                if dependance.date_fin_tot > tache.date_debut_tot:
                    tache.date_debut_tot = dependance.date_fin_tot
                    tache.date_fin_tot = tache.date_debut_tot + (tache.date_fin - tache.date_debut)
            print(f"Débogage: Tâche {tache.nom}, Date de début tôt: {tache.date_debut_tot}, Date de fin tôt: {tache.date_fin_tot}")

       
        # Calculer les dates au plus tard
        for tache in reversed(self.taches):
            for dependance in tache.dependances:
                if dependance.date_debut_tard < tache.date_fin_tard:
                    tache.date_fin_tard = dependance.date_debut_tard
                    tache.date_debut_tard = tache.date_fin_tard - (tache.date_fin - tache.date_debut)
            print(f"Débogage: Tâche {tache.nom}, Date de début tard: {tache.date_debut_tard}, Date de fin tard: {tache.date_fin_tard}")

        # Identifier les tâches critiques
        chemin_critique = []
        for tache in self.taches:
            if tache.date_debut_tot == tache.date_debut_tard:
                chemin_critique.append(tache)

        return chemin_critique
    
    def afficher_chemin_critique(self):
        chemin_critique = self.calculer_chemin_critique()
        print("Chemin critique:")
        for tache in chemin_critique:
            print(f"  Tâche: {tache.nom}, Date de début: {tache.date_debut_tot}, Date de fin: {tache.date_fin_tot}")
            
    def evaluer_risques(self):
        for risque in self.risques:
            risque['impact_total'] = risque['probabilite'] * (1 if risque['impact'] == 'Élevé' else 0.5 if risque['impact'] == 'Moyen' else 0.1)
            self.risques.sort(key=lambda x: x['impact_total'], reverse=True)

    def afficher_risques(self):
        self.evaluer_risques()
        print("Risques (priorisés) :")
        for risque in self.risques:
            print(f"  Risque: {risque['nom']}, Probabilité: {risque['probabilite']}, Impact: {risque['impact']}, Impact Total: {risque['impact_total']}")
            
      #Generer un rapport      
    def generer_rapport_pdf(self, filename):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Rapport du Projet", ln=True, align="C")
        
        pdf.cell(200, 10, txt=f"Projet: {self.nom}", ln=True)
        pdf.cell(200, 10, txt=f"Description: {self.description}", ln=True)
        pdf.cell(200, 10, txt=f"Date de début: {self.date_debut}", ln=True)
        pdf.cell(200, 10, txt=f"Date de fin: {self.date_fin}", ln=True)
        
        pdf.cell(200, 10, txt="Tâches:", ln=True)
        for tache in self.taches:
            pdf.cell(200, 10, txt=f"  - {tache.nom}: {tache.date_debut} à {tache.date_fin} ({tache.responsable.nom})", ln=True)
        
        pdf.output(filename)


# Exemple d'utilisation
projet = Projet("Projet X", "Description du projet X", "2024-01-01", "2024-12-31")
projet.ajouter_tache(Tache("Tâche 1", "Description de la tâche 1", "2024-01-01", "2024-02-01", Membre("Alice", "Chef de projet"), "En cours"))
projet.ajouter_tache(Tache("Tâche 2", "Description de la tâche 2", "2024-02-01", "2024-03-01", Membre("Bob", "Développeur"), "Non commencée"))
projet.generer_rapport_pdf("rapport_projet.pdf")