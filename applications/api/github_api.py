import requests


class GitHubApi:
    def __init__(self, base_url, version):
        self.base_url = base_url
        self.version = version


    def get_user(self, username):
        r = requests.get(f"{self.base_url}/users/{username}")
        r.raise_for_status()
        return r.json()


    def get_repos(self, repo_search_param: str):
        r = requests.get(
            f"{self.base_url}/search/repositories",
                params={'q': repo_search_param}
                )
        r.raise_for_status()
        return r.json()

