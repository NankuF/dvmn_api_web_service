import requests

london = 'london'
sheremetievo = 'svo'
cherepovec = 'Череповец'


def get_weather(city: str):
    url = f'http://wttr.in/{city}'
    payload = {'nTqu': '', 'lang': 'ru', 'm': '', }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    get_weather(london)
    get_weather(sheremetievo)
    get_weather(cherepovec)
