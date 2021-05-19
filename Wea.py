# API: https://danepubliczne.imgw.pl/api/data/synop/
from requests import get
from json import loads
from terminaltables import AsciiTable, SingleTable

#wczytanie api imgw
url = 'https://danepubliczne.imgw.pl/api/data/synop/'
print(get(url))
resp = get(url)

# print(resp.text)
# print(loads(resp.text))
#interfejs programu i wypisanie danych
print("Weather forecast")
user_city = str(input('Please choose a city: '))
cities = [user_city]
api_row = [
    ['City', 'Temperature', 'Wind Speed', 'Pressure']
]
for weather_row in loads(resp.text):
    # print(r)
    if weather_row['stacja'] in cities:
        # print(r['stacja'], r['temperatura'], r['predkosc_wiatru'], r['cisnienie']) dane z api imgw - odpowiednie listy
        api_row.append([
            weather_row['stacja'], 
            weather_row['temperatura'], 
            weather_row['predkosc_wiatru'], 
            weather_row['cisnienie']
        ])

weather_table = SingleTable(api_row)
print(weather_table.table)
