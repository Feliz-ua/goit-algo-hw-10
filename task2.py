import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2


# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))


# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
under_curve = y_random < f(x_random)

# Відображення точок на графіку
ax.scatter(x_random[under_curve], y_random[under_curve], color='blue', s=1, alpha=0.5, label='Під кривою')
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='red', s=1, alpha=0.5, label='Над кривою')

ax.legend()

# Аналітичний розрахунок
area_analytical = (b**3 - a**3) / 3

# За допомогою quad
area_quad, error_quad = quad(f, a, b)

# Метод Монте-Карло
area_monte_carlo = (b - a) * f(b) * np.mean(under_curve)

# Виведення результатів
print(f"Метод Монте-Карло: {area_monte_carlo:.4f}")
print(f"Аналітичний результат: {area_analytical:.4f}")
print(f"Quad: {area_quad:.4f} (похибка: {error_quad:.2e})")
print(f"Похибка Монте-Карло: {abs(area_monte_carlo - area_analytical):.4f}")

plt.grid()
plt.show()