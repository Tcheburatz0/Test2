from statistics import mean

import requests
import json

s_city = "Petersburg,RU"
appid = "ee5d55c03e00461d6c01b4e1b991bc40"


# Прогноз
def request_forecast(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        sum = 0
        count = 0
        morns_six = []
        morns_nine = []
        for i in data['list']:
            if i['dt_txt'].find('18:00:00') != -1:
                morns_six.append(i['main']['temp'])
            if i['dt_txt'].find('21:00:00') != -1:
                morns_nine.append(i['main']['temp'])
            sum += i['main']['temp']
            count += 1
    except Exception as e:
        print("Exception (forecast):", e)
        pass

    print("Средняя температура = ", format(round(sum/count, 2)))
    print('Средняя прогнозная вечерняя (6-и вечера) температура = ', mean(morns_six))
    print('Средняя прогнозная вечерняя (9-и вечера) температура = ', mean(morns_nine))

    text = json.loads(res.text)
    info = text['list']
    pres = []
    for i in info:
        main = i['main']
        pres.append(main['pressure'])
    print('Минимальное давление: ' + str(min(pres)))


# city_id for SPb
city_id = 498817

request_forecast(city_id)
