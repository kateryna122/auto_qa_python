import os


class Config:
    base_url = os.environ.get("BASE_URL", "https://api.github.com")
    base_url_ui = os.environ.get("BASE_URL_UI", "https://github.com")