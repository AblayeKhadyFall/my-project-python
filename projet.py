from datetime import datetime, timedelta

class Tache:
    def __init__(self, nom, description, date_debut, date_fin, responsable, statut, dependances=None):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances = dependances if dependances else []

    def __str__(self):
        return f"Tâche: {self.nom}, Description: {self.description}, Date de début: {self.date_debut}, Date de fin: {self.date_fin}, Responsable: {self.responsable}, Statut: {self.statut}, Dépendances: {self.dependances}"


class Projet:
    def __init__(self, nom, description, date_debut, date_fin):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.risques = []
        self.jalons = []
        self.changements = []
        self.equipe = []

    def ajouter_tache(self, nom, description, date_debut, date_fin, responsable, statut, dependances=None):
        tache = Tache(nom, description, date_debut, date_fin, responsable, statut, dependances)
        self.taches.append(tache)

    def ajouter_risque(self, nom, probabilite, impact):
        self.risques.append({'nom': nom, 'probabilite': probabilite, 'impact': impact})

    def ajouter_jalon(self, nom, date):
        self.jalons.append({'nom': nom, 'date': date})

    def ajouter_changement(self, version, date):
        self.changements.append({'version': version, 'date': date})

    def ajouter_membre(self, nom, role):
        self.equipe.append({'nom': nom, 'role': role})

    def calculer_chemin_critique(self):
        def find_task_by_name(name):
            for task in self.taches:
                if task.nom == name:
                    return task
            return None

        # Calculer les dates de début et de fin au plus tôt
        for tache in self.taches:
            if not tache.dependances:
                tache.date_debut_tot = tache.date_debut
            else:
                tache.date_debut_tot = max(find_task_by_name(dep).date_fin_tot for dep in tache.dependances)
            tache.date_fin_tot = tache.date_debut_tot + (tache.date_fin - tache.date_debut)

        # Calculer les dates de début et de fin au plus tard
        for tache in reversed(self.taches):
            if tache == self.taches[-1]:
                tache.date_fin_tard = tache.date_fin_tot
            else:
                tache.date_fin_tard = min(
                    (find_task_by_name(dep).date_debut_tard for dep in tache.dependances if find_task_by_name(dep)),
                    default=tache.date_fin_tot
                )
            tache.date_debut_tard = tache.date_fin_tard - (tache.date_fin - tache.date_debut)

        # Déterminer le chemin critique
        chemin_critique = []
        for tache in self.taches:
            if tache.date_debut_tot == tache.date_debut_tard:
                chemin_critique.append(tache.nom)

        return chemin_critique

    def envoyer_email(self, destinataire, message):
        print(f"Envoi d'un email à {destinataire}: {message}")

    def __str__(self):
        result = []
        result.append(f"Projet: {self.nom}")
        result.append(f"Description: {self.description}")
        result.append(f"Date de début: {self.date_debut}")
        result.append(f"Date de fin: {self.date_fin}")
        result.append(f"Budget: 0.0")  # Ajouter des détails de budget si nécessaire
        result.append(f"Version: 2")   # Ajouter des détails de version si nécessaire
        result.append("Tâches:")
        for tache in self.taches:
            result.append(f"  {tache}")
        result.append("Risques:")
        for risque in self.risques:
            result.append(f"  Risque: {risque['nom']}, Probabilité: {risque['probabilite']}, Impact: {risque['impact']}")
        result.append("Jalons:")
        for jalon in self.jalons:
            result.append(f"  Jalon: {jalon['nom']}, Date: {jalon['date']}")
        result.append("Changements:")
        for changement in self.changements:
            result.append(f"  Changement: Changement de version {changement['version']}, Date: {changement['date']}")
        result.append("Équipe:")
        for membre in self.equipe:
            result.append(f"  Membre: {membre['nom']}, Rôle: {membre['role']}")
        return "\n".join(result)
