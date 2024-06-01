from notification_strategy import EmailNotificationStrategy, SMSNotificationStrategy, PushNotificationStrategy
from email_notification_strategy import EmailNotificationStrategy
from projet import Projet
from membre import Membre
from tache import Tache
from risque import Risque
from jalon import Jalon
import os
from datetime import datetime
from fpdf import FPDF


def main():
    # Créer des membres
    membre1 = Membre("Alice", "Chef de projet")
    membre2 = Membre("Bob", "Développeur")

    # Créer un projet
    projet = Projet("Projet X", "Description du projet X", "2024-01-01", "2024-12-31")

    # Ajouter des membres à l'équipe
    projet.ajouter_membre_equipe(membre1)
    projet.ajouter_membre_equipe(membre2)

    # Définir une stratégie de notification
    projet.set_notification_strategy(EmailNotificationStrategy())

    # Créer et ajouter des tâches
    tache1 = Tache("Tâche 1", "Description de la tâche 1", "2024-01-01", "2024-02-01", membre1, "En cours")
    tache2 = Tache("Tâche 2", "Description de la tâche 2", "2024-02-01", "2024-03-01", membre2, "Non commencée")
    #tache1.ajouter_dependance(tache1)
    tache2.ajouter_dependance(tache1)
    projet.ajouter_tache(tache1)
    projet.ajouter_tache(tache2) 
       
    # Appel de la méthode pour générer le rapport PDF
    #projet.generer_rapport_pdf("rapport_projet.pdf")

    # Affichage du projet (facultatif, pour débogage)
    print(projet)
    
    # Créer et ajouter des risques
    risque1 = Risque("Risque 1", 0.7, "Élevé")
    risque2 = Risque("Risque 2", 0.8, "Élevé")
    projet.ajouter_risque(risque1)
    projet.ajouter_risque(risque2)

    # Créer et ajouter des jalons
    jalon1 = Jalon("Jalon 1", "2024-06-01")
    jalon2 = Jalon("Jalon 2", "2024-05-02")
    projet.ajouter_jalon(jalon1)
    projet.ajouter_jalon(jalon2)

    # Enregistrer un changement
    projet.enregistrer_changement("Changement de version 1")
    projet.enregistrer_changement("Changement de version 2")

    # Notifier les membres
    projet.notifier("Message de test", [membre1, membre2])
    
    # Afficher les détails du projet
    projet.afficher_details()
    
    # Afficher le chemin critique
    projet.afficher_chemin_critique()

    # Générer le rapport PDF
    projet.generer_rapport_pdf("rapport_projet.pdf")

    # Vérification de l'existence du fichier PDF
    if os.path.exists("rapport_projet.pdf"):
        print("Le rapport PDF a été généré avec succès : rapport_projet.pdf")
    else:
         print("Erreur lors de la génération du rapport PDF.")
         
if __name__ == "__main__":
    main()
    