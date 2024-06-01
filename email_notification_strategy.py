from membre import Membre
from notification_strategy import NotificationStrategy

class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre) -> None:
        print(f"Envoi d'un email à {destinataire.nom}: {message}")
