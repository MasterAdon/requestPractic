import requests
from pprint import pprint

hero_intell = {} # Создаем словарь с интеллектом героев

url = "https://superheroapi.com/api/2619421814940190/332/powerstats"
response = requests.get(url)
hulk = response.json()
a = {'Hulk': hulk['intelligence']}
hero_intell.update(a)

url = "https://superheroapi.com/api/2619421814940190/149/powerstats"
response = requests.get(url)
cap_am = response.json()
b = {'Captain_America' : cap_am['intelligence']}
hero_intell.update(b)

url = "https://superheroapi.com/api/2619421814940190/655/powerstats"
response = requests.get(url)
thanos = response.json()
c = {'Thanos': thanos['intelligence']}
hero_intell.update(c)

# print(hero_intell)
task_list = sorted(hero_intell.keys())
# print(task_list)  #Вывод списка героев отсортьированного по интеллекту

