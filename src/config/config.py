import os

from src.config.providers.config_from_env_provider import ConfigFromEnvProvider
from src.config.providers.config_from_json_provider import ConfigFromSimpleJsonProvider


class Config:
    default_env = "dev"

    def __init__(self) -> None:
        self.conf_dict = {}

        target = os.environ.get('TARGET')
        if target is None:
            target = Config.default_env

        json_path = f"src/config/env_configs/{target}.json"

        # Hierarhy of providers
        self.providers = [
            ConfigFromSimpleJsonProvider(json_path),
            ConfigFromEnvProvider(),
            ]

        self.register("BASE_URL_API")
        self.register("BASE_URL_UI")

    def register(self, name):
        """
        Register name of the key which is used 
        in tests
        """

        # Order in self.provider makes difference
        for provider in self.providers:
            val = provider.get(name)

            if val is not None:
                self.conf_dict[name] = val

        # raise error if no value is found across the providers
        val = self.conf_dict.get(name)
        if val is None:    
            raise Exception(f"{name} variable is not set in config")

        print(f"{name} variable is registered in config with value {val}")

    def get(self, name):
        """
        Return existing value
        """
        val = self.conf_dict.get(name)
        if val is None:    
            raise Exception(f"{name} variable is not set in config")

        return self.conf_dict.get(name)


# python way singleton
config = Config()