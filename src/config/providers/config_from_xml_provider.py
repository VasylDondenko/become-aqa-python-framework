import xml.etree.ElementTree as ET
from src.config.providers.base_config import BaseConfigKeyProvider


# BaseConfigKeyProvider usage is optional
class ConfigFromXmlProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the XML file
    """
    def __init__(self, config_path):
        """
        :param config_path: path to the XML with configuration
        """
        tree = ET.parse(config_path)
        self._config_data = tree.getroot()

    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        element = self._config_data.find(key)
        if element is not None:
            return element.text
        else:
            return None