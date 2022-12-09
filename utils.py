import requests


def get_html(source: str) -> str:
    response = requests.get(source)
    return response.text
