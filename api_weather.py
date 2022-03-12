import requests


def get_weather(place: str):
    url = f'http://wttr.in/{place}'
    payload = {'nTqm': '', 'lang': 'ru'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['london', 'svo', 'Череповец']
    for place in places:
        print(get_weather(place))
