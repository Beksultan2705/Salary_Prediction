import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': ['2020', '2021', '2022', '2023', '2024', '2025'],
    'Kyrgyz Republic': [18940, 19330, 26540, 31604, 36047, 44419],
    'Bishkek': [22677, 23085, 30757, 37454.7, 44074, 51266],
    'Issyk-Kul': [26860, 30172, 34669, 38743, 41084, 46261],
    'Batken': [13017, 13010, 20439, 25554, 26662, 31461],
    'Jalala-Abad': [17580, 17478, 24869, 28764, 31229, 34633],
    'Naryn':[18071, 17931, 26031, 33011, 35205, 39934],
    'Osh_Region':[12712, 12557, 19762, 23134, 25200, 26914],
    'Osh_City':[15726, 15674, 23459, 26961, 30039, 34662],
    'Chuy': [16051, 15958, 21641, 25562, 27819, 33837],
    'Talas': [16156, 16400, 25092, 30689, 34068, 38725]
}

df = pd.DataFrame(data).set_index('Year')

plt.style.use('seaborn-v0_8-muted')

fig, ax = plt.subplots(figsize=(12, 7))

# Рисуем линии. Выделим общую по стране жирной линией
for column in df.columns:
    linewidth = 4 if column == 'Кыргызстан (в целом)' else 2
    alpha = 1 if column == 'Кыргызстан (в целом)' else 0.7
    ax.plot(df.index, df[column], marker='o', label=column, linewidth=linewidth, alpha=alpha)

# Настройки
plt.title('Динамика роста средних зарплат в КР по регионам (2020-2024)', fontsize=16, pad=20)
plt.ylabel('Сом', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Выносим легенду вбок, чтобы не мешала
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Регионы")

# Подписываем только финальные значения 2024 года для ясности
for column in df.columns:
    plt.text(4.1, df[column].iloc[-1], f'{int(df[column].iloc[-1])}', va='center', fontsize=9)

plt.tight_layout()
plt.show()
