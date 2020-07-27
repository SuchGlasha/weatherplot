import pandas as pd
import matplotlib.pyplot as plt

path = 'raw/weather_msk_5y.xls'

data = pd.read_excel(path, skiprows=6)

data['Местное время в Москве (ВДНХ)']

data['date'] = pd.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst=True)

data = data.sort_values('date')

day_first = pd.Timestamp(day=1, month=12, year=2016)
day_last = pd.Timestamp(day=1, month=1, year=2018)

condition = (data['date'] >= day_first) & (data['date'] <= day_last)

data2017 = data[condition]

x = data2017['date']
y = data2017['T']

plt.figure(figsize=(40, 5))
plt.plot(x, y, label='Temperature')
plt.title('Температура в Москве c декабря 2016 по январь 2018')
plt.xlabel('index')
plt.ylabel('T')
plt.legend
plt.show()
