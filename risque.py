class Risque:
    def __init__(self, description: str, probabilite: float, impact: str):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact
    def afficher_details(self):
        print(f"  Risque: {self.description}")
        print(f"    Probabilité: {self.probabilite}")
        print(f"    Impact: {self.impact}")