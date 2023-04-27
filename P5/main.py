from prettytable import PrettyTable
import matplotlib.pyplot as mpl
from math import log

input_data = [-0.76, -0.55, -0.62, 0.21, -1.13,
              -1.14, 1.07, -0.14, -1.45, 1.45,
              1.07, -1.49, 0.11, 0.35, 1.07,
              1.59, -0.10, - 1.18, -0.73, 0.31]

sorted_input_data = sorted(input_data)

print(f'Исходный ряд: {input_data}')
print(f'Вариацонный ряд: {sorted_input_data}')
print("Экстремальные значения:")
print(f'Минимум: {min(input_data)}  Максимум: {max(input_data)}')
print(f'Размах: {max(input_data) - min(input_data)}')

# Статистический ряд
values_and_amounts = {}
for x_i in sorted_input_data:
    if values_and_amounts and x_i == list(values_and_amounts.keys())[-1]:
        values_and_amounts[x_i] += 1
    else:
        values_and_amounts[x_i] = 1
table = PrettyTable()
table.field_names = ["x(i)", *values_and_amounts.keys()]
table.add_row(["n(i)", *values_and_amounts.values()])
print(f'Статистический ряд: \n {table}')

# Математическое ожидание
X = sum(input_data) / len(input_data)
print(f'Математическое ожидание: {round(X, 5)}')

# СКО
dispersion = 0
for x_i in input_data:
    dispersion += (x_i - X) ** 2
print(f'СКО: {round(dispersion ** 0.5, 5)}')

# Эмпирическая функция
x = mpl.subplot(5, 1, 1)
mpl.title("График эмпирической функции распределения")
mpl.grid()
mpl.ylim(0, 1)
mpl.xlim(-2, 2)
mpl.xlabel("x")
mpl.ylabel("F(x)")

n = len(values_and_amounts)
keys = list(values_and_amounts.keys())
y = 0
print("Эмпирическая функция:")
print(f'\t\t/ {round(y, 2)}, x <= {keys[0]}')
for i in range(n - 1):
    if i < n:
        y += values_and_amounts[keys[i]] / n
    else:
        y = 0

    if i == n / 2:
        left = "F*(x) = "
    else:
        left = "\t\t"

    print(f'{left}| {round(y, 2)}, {keys[i]} < x <= {keys[i + 1]}')
    mpl.plot([keys[i], keys[i + 1]], [y, y], c='black')
print(f'\t\t\\ {round(y, 2)}, {keys[-1]} < x')

# Группированная выборка
h = (max(input_data) - min(input_data)) / (1 + log(len(input_data), 2))
# left_border = sorted_input_data[0] -h/2
left_border = round(sorted_input_data[0],2)
next_left_border = round(left_border + h,2)
grouped_selection = {left_border: 0}
for i in sorted_input_data:
    if left_border <= i < next_left_border:
        grouped_selection[left_border] += 1 / n
    else:
        grouped_selection[next_left_border] = 1/n
        left_border = round(next_left_border,2)
        next_left_border = round(left_border + h,2)

table = PrettyTable()
table.field_names = (f'[{round(key,2)}; {round(key+h,2)})' for key in grouped_selection.keys())
table.add_row(list(round(x, 2) for x in grouped_selection.values()))
print("Интервальное статистическое распределение:")
print(table)

# Полигон приведенных частот
mpl.subplot(5, 1, 3)
mpl.title("Полигон приведенных частот")
mpl.grid()
mpl.xlim(-2, 2)
mpl.xlabel("x")
mpl.ylabel("p")
mpl.plot(list(grouped_selection.keys()), list(grouped_selection.values()), c='black')

# Гистограмма
mpl.subplot(5, 1, 5)
mpl.grid(c='black')
mpl.title("Гистограмма частот")
mpl.bar(list(map(lambda z: z + h/2, grouped_selection.keys())), list(grouped_selection.values()), width=h)
x_ticks = list(grouped_selection.keys()) + [round(list(grouped_selection.keys())[-1] + h, 2)]
mpl.xticks(x_ticks, x_ticks)
mpl.show()

print(grouped_selection)
