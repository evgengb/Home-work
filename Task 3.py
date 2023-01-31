"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n_str = input("Введите целое положительное число - ")
n = int(n_str)

nn_str = n_str + n_str
nn = int(nn_str)
nnn_str = n_str + n_str + n_str
nnn = int(nnn_str)
num = n + nn + nnn

print(f"n + nn + nnn = {num}") # Ответ как в примере
print(f"{n} + {nn_str} + {nnn_str} = {num}")
