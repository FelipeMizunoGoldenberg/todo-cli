import requests

API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-15.78&longitude=-47.93&current_weather=true"
)


def get_weather():
    response = requests.get(API_URL, timeout=10)

    if response.status_code != 200:
        raise Exception("Erro ao buscar dados da API")

    data = response.json()

    current = data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
    }
