import requests


class ApiDataUsa:
    def __init__(self, base_url):
        self.base_url = base_url


    def get_data_tesseract(self):
        r = requests.get(f"{self.base_url}/tesseract/")
        r.raise_for_status()
        return r.json()


    def get_data_members(self):
        r = requests.get(
            f"{self.base_url}/tesseract/members",
            params={'cube': "acs_yg_total_population_5",
                    'level': "State"},
        )
        r.raise_for_status()
        return r.json()