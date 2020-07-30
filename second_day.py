import pandas as pd
import matplotlib.pyplot as plt

path = 'raw/weather_msk_5y.xls'

data = pd.read_excel(path, skiprows=6)

data['Местное время в Москве (ВДНХ)']

data['date'] = pd.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst=True)

data = data.sort_values('date')

data = data.reset_index(drop=True)

print(data)

print(data['T'].min())
print(data['T'].max())

data['min_T'] = data['T'].min()
data['max_T'] = data['T'].max()

data['quantile_95'] = data['T'].quantile(0.95)
data['quantile_05'] = data['T'].quantile(0.05)

# скользящее среднее позволяет следить за динамикой процесса путём сглаживания
print(data['T'].rolling(10).mean())

# гистограмма показывает частоту с которой встречаются значения
data['T'].hist()

# корреляция
data.corr()

data_daily = data[data['date'].dt.hour == 12]
plt.figure(figsize=(20, 5))
pd.plotting.autocorrelation_plot(data_daily['T'])

x = data['date']
y = data['T']
plt.figure(figsize=(20, 5))
plt.plot(x, y, label='T')
plt.plot(x, data['min_T'], label='min')
plt.plot(x, data['max_T'], label='max')
plt.plot(x, data['quantile_95'], label='quantile 95')
plt.plot(x, data['quantile_05'], label='quantile 05')
plt.plot(x, data['T'].rolling(100).mean(), label='Скользящее среднее 100 дней')
plt.plot(x, data['T'].rolling(1000).mean(), label='Скользящее среднее 1000 дней')
plt.legend()
plt.show()

