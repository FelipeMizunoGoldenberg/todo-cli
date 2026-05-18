from src.weather import get_weather


def test_get_weather():
    weather = get_weather()

    assert "temperature" in weather
    assert "windspeed" in weather
