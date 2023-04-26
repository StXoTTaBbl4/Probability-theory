from prettytable import PrettyTable

input_data = [-0.76, -0.55, -0.62, 0.21, -1.13,
              -1.14, 1.07, -0.14, -1.45, 1.45,
              1.07, -1.49, 0.11, 0.35, 1.07,
              1.59, -0.10, - 1.18, -0.73, 0.31]

print(f'Исходный ряд: {input_data}')
print(f'Вариацонный ряд: {sorted(input_data)}')
print("Экстремальные значения:")
print(f'Минимум: {min(input_data)}  Максимум: {max(input_data)}')
print(f'Размах: { max(input_data) - min(input_data)}')

# Статистический ряд
values_and_amounts = {}
for x_i in sorted(input_data):
    if values_and_amounts and x_i == list(values_and_amounts.keys())[-1]:
        values_and_amounts[x_i] += 1
    else:
        values_and_amounts[x_i] = 1
table = PrettyTable()
table.field_names = ["x(i)", *values_and_amounts.keys()]
table.add_row(["n(i)", *values_and_amounts.values()])
print(f'Статистический ряд: \n {table}')

# Математическое ожидание
X = sum(input_data)/len(input_data)
print(f'Математическое ожидание: {round(X,5)}')

# СКО
dispersion = 0
for x_i in input_data:
    dispersion += (x_i - X)**2
print(f'СКО: {round(dispersion**0.5,5)}')

import matplotlib.pyplot as plot
