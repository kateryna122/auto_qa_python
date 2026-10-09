import os


class ConfigData:
    base_url = os.environ.get("BASE_URL", "https://api.datausa.io")