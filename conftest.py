import pytest
from playwright.sync_api import Page

from applications.api.api_data_usa import ApiDataUsa
from applications.api.github_api import GitHubApi
from applications.ui.github_ui import GithubUI
from config.config import Config
from config.config_data_usa import ConfigData


@pytest.fixture(scope="session")
def github_api_client():
    github_api_client = GitHubApi(Config.base_url, "v1")

    yield github_api_client
    print("END UP TEST 1")


@pytest.fixture(scope="session")
def data_api_client():
    data_api_client = ApiDataUsa(ConfigData.base_url)

    yield data_api_client
    print("END UP TEST 2")


@pytest.fixture
def github_ui_client(page: Page):
    github_ui_client = GithubUI(Config.base_url_ui, page)
    github_ui_client.goto()

    yield github_ui_client
    print("END UP TEST 3")
