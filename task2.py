import matplotlib.pyplot as plt
import numpy as np

# Реалістичні фіктивні дані
years = np.arange(2003, 2023)  # Період 2003-2022
ukraine_data = [12000, 11500, 11200, 10800, 10500, 10200, 10000, 9700, 9500, 9300, 9100, 8900, 8700, 8500, 8300, 8100, 8000, 7800, 7600, 7400]
usa_data = [15000, 14800, 14700, 14500, 14300, 14100, 13900, 13700, 13600, 13400, 13300, 13100, 13000, 12900, 12800, 12700, 12600, 12500, 12400, 12300]

# 2.1 Лінійний графік динаміки показника для України та США
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_data, marker='o', label='Україна')
plt.plot(years, usa_data, marker='s', label='США')
plt.title('Children out of school, primary (2003-2022)')
plt.xlabel('Рік')
plt.ylabel('Кількість дітей, які не відвідують школу')
plt.grid(alpha=0.3)
plt.legend()
plt.show()

# 2.2 Стовпчаста діаграма для обраної країни
# Вибір країни: "Україна" або "США"
country = "Україна"  # Замініть на "США" для іншої країни

if country == "Україна":
    data = ukraine_data
elif country == "США":
    data = usa_data
else:
    print("Країна не знайдена. Використовую Україну за замовчуванням.")
    data = ukraine_data

# Побудова стовпчастої діаграми
plt.figure(figsize=(10, 6))
plt.bar(years, data, color='skyblue' if country == "Україна" else 'salmon', edgecolor='black')
plt.title(f'Children out of school, primary for {country} (2003-2022)')
plt.xlabel('Рік')
plt.ylabel('Кількість дітей, які не відвідують школу')
plt.xticks(years, rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()
