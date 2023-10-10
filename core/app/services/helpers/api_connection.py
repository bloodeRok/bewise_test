import requests


def fetch_questions_from_external_api(count):
    response = requests.get(f'https://jservice.io/api/random?count={count}')
    if response.status_code == 200:
        return response.json()
    return []
