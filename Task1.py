from pprint import pprint
import requests


def get_request():
    '''забераем список героев в json формате'''
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json' # URL api
    resp = requests.get(url) # Запрос данных о героях из json
    return resp.json() # Возвращаем json

# pprint(get_request()) # Тестируем функцию get_request


def get_heroes_from_json(Hero1, Hero2, Hero3):
    '''создаем словарь с именами и показателями ума героев'''
    heroes_json = get_request()
    selected_heroes = {} # Словарь куда будем собирать героев
    for info in heroes_json:
        if info['name'] == Hero1.title():
            Hero1_intelligence = info['powerstats']['intelligence']
            selected_heroes[info['name']] = Hero1_intelligence
        elif info['name'] == Hero2.title():
            Hero2_intelligence = info['powerstats']['intelligence']
            selected_heroes[info['name']] = Hero2_intelligence
        elif info['name'] == Hero3.title():
            Hero3_intelligence = info['powerstats']['intelligence']
            selected_heroes[info['name']] = Hero3_intelligence
    return selected_heroes

# pprint(get_heroes_from_json('captain america', 'hulk', 'thanos')) # Тестируем функцию get_heroes_from_json


def who_is_smarter(Hero1, Hero2, Hero3):
    '''выбираем самого умного'''
    heroes = get_heroes_from_json(Hero1, Hero2, Hero3)
    smarter = max(heroes.values())
    for name, values in heroes.items():
        if values == smarter:
            return f'{name} - Самый умный! У него {values} кг. ума!'


if __name__=='__main__':
    result = who_is_smarter('captain america', 'hulk', 'thanos')
    pprint(result)