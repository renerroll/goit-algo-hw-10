import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import quad


def integral_plot(f, a, b):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()


def monte_carlo_integral(a, b, num_samples=1000):
    sum_values = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        sum_values += f(x)

    average = sum_values / num_samples
    integral_approximation = (b - a) * average

    return integral_approximation

# Обчислення похибки методу Монте-Карло
def monte_carlo_error(values):
    mean = np.mean(values)
    std_deviation = np.std(values)
    n = len(values)
    error = 1.96 * (std_deviation / np.sqrt(n))  
    return error


if __name__ == "__main__":
    def f(x):
        return x**2

    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Розв'язок методом Монте-Карло
    mc_result_1 = monte_carlo_integral(a, b, 7000)
    mc_result_2 = monte_carlo_integral(a, b, 30000)
    mc_results = [mc_result_1, mc_result_2]
    mc_error = monte_carlo_error(mc_results)

    print(f"**Знаходження значення інтеграла методом Монте-Карло:**\n"
          f"7000 зразків - `{mc_result_1:.8f}`\n"
          f"30000 зразків - `{mc_result_2:.8f}`\n")

    quad_result, error = quad(f, a, b)
    print(f"**Перевірка обчислення за допомогою функції quad з підмодуля integrate бібліотеки SciPy:** `{quad_result:.8f}`\n")
    
    print(f"**Похибка Монте-Карло для 7000 зразків відносно методу quad:** {abs(mc_result_1 - quad_result)}")
    print(f"**Похибка Монте-Карло для 30000 зразків відносно методу quad:** {abs(mc_result_2 - quad_result)}")


    integral_plot(f, a, b)
