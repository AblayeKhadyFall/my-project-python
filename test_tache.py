import unittest
from tache import Tache
from membre import Membre
from datetime import datetime

class TestTache(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets utilisés dans les tests
        self.membre = Membre("Alice", "Chef de projet")
        self.tache = Tache("Tâche 1", "Description de la tâche 1", datetime(2024, 1, 1), datetime(2024, 2, 1), self.membre, "En cours")

    def test_initialisation_tache(self):
        # Teste l'initialisation de la tâche
        self.assertEqual(self.tache.nom, "Tâche 1")
        self.assertEqual(self.tache.description, "Description de la tâche 1")
        self.assertEqual(self.tache.date_debut, datetime(2024, 1, 1))
        self.assertEqual(self.tache.date_fin, datetime(2024, 2, 1))
        self.assertEqual(self.tache.responsable.nom, "Alice")
        self.assertEqual(self.tache.responsable.role, "Chef de projet")
        self.assertEqual(self.tache.statut, "En cours")
        self.assertEqual(self.tache.dependances, [])

    def test_ajouter_dependance(self):
        # Teste l'ajout de dépendances à une tâche
        autre_tache = Tache("Tâche 2", "Description de la tâche 2", datetime(2024, 2, 1), datetime(2024, 3, 1), self.membre, "Non commencée")
        self.tache.ajouter_dependance(autre_tache)
        self.assertIn(autre_tache, self.tache.dependances)

    def test_statut_tache(self):
        # Teste la modification du statut de la tâche
        self.tache.statut = "Terminée"
        self.assertEqual(self.tache.statut, "Terminée")

if __name__ == '__main__':
    unittest.main()
