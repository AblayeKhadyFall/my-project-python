from datetime import datetime

class Jalon:
    def __init__(self, nom: str, date: str):
        self.nom = nom
        self.date = datetime.strptime(date, '%Y-%m-%d')
    def afficher_details(self):
        print(f"  Jalon: {self.nom}")
        print(f"    Date: {self.date}")