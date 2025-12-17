from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for messaging providers (Slack, Teams, etc.)
    """
    
    @abstractmethod
    def start(self):
        """
        Start the provider's listener/bot service.
        """
        pass

    @abstractmethod
    def send_message(self, channel: str, text: str):
        """
        Send a message to a specific channel.
        """
        pass

