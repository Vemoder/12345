# Определяем функцию
def is_even(n):
    return n % 2 == 0

# Тесты для четных чисел
print(is_even(0))   # Ожидается: True
print(is_even(2))   # Ожидается: True
print(is_even(4))   # Ожидается: True
print(is_even(10))  # Ожидается: True
print(is_even(-2))  # Ожидается: True

# Тесты для нечетных чисел
print(is_even(1))   # Ожидается: False
print(is_even(3))   # Ожидается: False
print(is_even(5))   # Ожидается: False
print(is_even(11))  # Ожидается: False
print(is_even(-3))  # Ожидается: False

# Тесты для некорректных типов (должны вызывать ошибку)
try:
    print(is_even(2.5))  # Ожидается: True, но это может быть неуместно в контексте целых чисел
except TypeError as e:
    print(f"Ошибка для 2.5: {e}")

try:
    print(is_even("string"))  # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка для 'string': {e}")

try:
    print(is_even([]))  # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка для []: {e}")
