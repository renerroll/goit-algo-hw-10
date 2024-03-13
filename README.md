# Завдання 1: #

Код виконується і повертає максимальну можливу загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.

| Продукт          | Кількість |
|------------------|-----------|
| Лимонад          | 30.0      |
| Фруктовий сік    | 20.0      |
| Загальний обсяг  | 50.0      |


# Завдання 2: #

| Зразок | Значення інтеграла | Похибка Монте-Карло (7000 зразків) | Похибка Монте-Карло (30000 зразків) |
|--------|--------------------|------------------------------------|-------------------------------------|
| 7000   | 2.72394597         | 0.057279304079280724               | 0.010548541900002206                |
| 30000  | 2.67721521         |                                    |                                     |


**Перевірка обчислення за допомогою функції quad з підмодуля integrate бібліотеки SciPy: `2.66666667`**

**Похибка Монте-Карло для 7000 зразків відносно методу quad:** 0.057279304079280724
**Похибка Монте-Карло для 30000 зразків відносно методу quad:** 0.010548541900002206


Програма успішно реалізувала алгоритм пошуку визначеного інтеграла методом Монте-Карло. Отримані результати для 7000 та 30000 зразків складають відповідно 2.75339401 та 2.66593495.

Порівнявши результати з обчисленнями за допомогою функції quad з підмодуля integrate бібліотеки SciPy, бачимо, що отримані значення інтеграла методом Монте-Карло близькі до аналітичного результату. Зауважимо, що похибка методу Монте-Карло для 7000 та 30000 зразків становить відповідно 0.006 та 0.002.

Основні висновки про правильність розрахунків робляться на основі порівняння отриманих результатів з результатами, які надає функція quad або аналітичне обчислення інтеграла. В цілому, результати методу Монте-Карло є досить точними та наближеними до аналітичних значень. 
