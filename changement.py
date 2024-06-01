from datetime import datetime

class Changement:
    def __init__(self, description: str, version: int, date: datetime):
        self.description = description
        self.version = version
        self.date = date
    def afficher_details(self):
        print(f"  Changement: {self.description}")
        print(f"    Version: {self.version}")
        print(f"    Date: {self.date}")