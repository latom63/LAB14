import numpy as np
import matplotlib.pyplot as plt

# Задаємо функцію
x = np.linspace(0.1, 5, 500)  # Обираємо x від 0.1 до 5, щоб уникнути ділення на 0
y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$Y(x)=\frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$', color='blue', linewidth=2, linestyle='-')

# Налаштування осей
plt.xlabel('x', fontsize=14)
plt.ylabel('Y(x)', fontsize=14)

# Назва графіка
plt.title('Графік функції $Y(x)$', fontsize=16)

# Додавання легенди
plt.legend(fontsize=12)

# Відображення графіка
plt.grid(True)
plt.show()
