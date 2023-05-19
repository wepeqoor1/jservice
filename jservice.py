import requests


def get_questions(count: int) -> dict:
    url = f'https://jservice.io/api/random?count={count}'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()
