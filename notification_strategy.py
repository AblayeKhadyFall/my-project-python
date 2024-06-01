from abc import ABC, abstractmethod
from typing import Protocol
from membre import Membre 
class NotificationStrategy(ABC):
    @abstractmethod
    def envoyer(self, message: str, destinataire: 'Membre'):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: 'Membre'):
        print(f"Email envoyé à {destinataire.nom}: {message}")

class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: 'Membre'):
        print(f"SMS envoyé à {destinataire.nom}: {message}")

class PushNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: 'Membre'):
        print(f"Push notification envoyé à {destinataire.nom}: {message}")
