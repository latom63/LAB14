import matplotlib.pyplot as plt

# Дані з лабораторної роботи
data = [
    {"name": "Іван", "gender": "ч", "height": 190},
    {"name": "Артем", "gender": "ч", "height": 185},
    {"name": "Максим", "gender": "ч", "height": 180},
    {"name": "Дмитро", "gender": "ч", "height": 175},
    {"name": "Сергій", "gender": "ч", "height": 170},
    {"name": "Марія", "gender": "ж", "height": 165},
    {"name": "Ольга", "gender": "ж", "height": 160},
    {"name": "Наталя", "gender": "ж", "height": 155},
    {"name": "Ірина", "gender": "ж", "height": 150},
    {"name": "Катерина", "gender": "ж", "height": 145},
]

# Обчислення кількості хлопців і дівчат
gender_counts = {"ч": 0, "ж": 0}
for person in data:
    gender_counts[person["gender"]] += 1

# Підготовка даних для кругової діаграми
labels = ["Хлопці", "Дівчата"]
sizes = [gender_counts["ч"], gender_counts["ж"]]
colors = ["lightblue", "pink"]
explode = (0.1, 0)  # Відокремимо сектор "Хлопці"

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
)
plt.title("Розподіл хлопців і дівчат")
plt.show()
