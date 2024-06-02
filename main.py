import io
import sys
from fpdf import FPDF
from datetime import datetime
from projet import Projet  # Assurez-vous d'importer votre module correctement
from email.mime.text import MIMEText
import smtplib

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Rapport de Projet', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

class Tee(io.StringIO):
    def __init__(self, *files):
        super().__init__()
        self.files = files

    def write(self, data):
        super().write(data)
        for f in self.files:
            f.write(data)

class Main:
    def run(self):
        # Créer un flux de sortie pour capturer la sortie standard
        captured_output = io.StringIO()
        tee = Tee(sys.stdout, captured_output)
        
        # Rediriger la sortie standard vers le tee
        old_stdout = sys.stdout
        sys.stdout = tee

        try:
            # Initialisation du projet
            projet = Projet("Projet X", "Description du projet X", datetime(2024, 1, 1), datetime(2024, 12, 31))

            # Ajout de membres d'équipe
            projet.ajouter_membre("Alice", "Chef de projet")
            projet.ajouter_membre("Bob", "Développeur")

            # Ajout de tâches
            projet.ajouter_tache("Tâche 1", "Description de la tâche 1", datetime(2024, 1, 1), datetime(2024, 2, 1), "Alice", "En cours")
            projet.ajouter_tache("Tâche 2", "Description de la tâche 2", datetime(2024, 2, 1), datetime(2024, 3, 1), "Bob", "Non commencée", ["Tâche 1"])

            # Ajout de risques
            projet.ajouter_risque("Risque 1", 0.7, "Élevé")
            projet.ajouter_risque("Risque 2", 0.8, "Élevé")

            # Ajout de jalons
            projet.ajouter_jalon("Jalon 1", datetime(2024, 6, 1))
            projet.ajouter_jalon("Jalon 2", datetime(2024, 5, 2))

            # Ajout de changements
            projet.ajouter_changement(1, datetime.now())
            projet.ajouter_changement(2, datetime.now())

            # Calcul du chemin critique
            chemin_critique = projet.calculer_chemin_critique()
            print("Chemin critique:", chemin_critique)

            # Envoi des emails
            projet.envoyer_email("alice@example.com", "Message de test")
            projet.envoyer_email("bob@example.com", "Message de test")

            # Affichage des informations du projet
            print(projet)
        finally:
            # Restaurer la sortie standard
            sys.stdout = old_stdout

        # Récupérer le contenu capturé
        output = captured_output.getvalue()

        # Générer le rapport PDF
        pdf = PDF()
        pdf.add_page()

        # Ajouter le contenu capturé au PDF
        pdf.chapter_title("Rapport de Projet")
        pdf.chapter_body(output)

        # Enregistrer le PDF
        pdf_output_path = "rapport_projet.pdf"
        pdf.output(pdf_output_path)

        print(f"Le rapport PDF a été généré avec succès : {pdf_output_path}")

if __name__ == "__main__":
    main = Main()
    main.run()
