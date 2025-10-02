import re

# 1. Валидация username (только буквы, цифры, _ , 3-20 символов)
username_pattern = r'^[a-zA-Z0-9_]{3,20}$'
def is_valid_username(username):
    return bool(re.match(username_pattern, username))

# 2. Поиск всех цен в тексте ("$100", "50 руб", "25.50")
price_pattern = r'\d+\.?\d*'
def extract_prices(text):
    return re.findall(price_pattern, text)

# 3. Валидация HEX цвета (#FFFFFF, #fff, #123abc)
color_pattern = r'^#[a-fA-F0-9]{3,6}$'
def is_valid_color(color):
    return bool(re.match(color_pattern, color))

# Проверка:
print(is_valid_username("vlad_123"))     # Должно быть True
print(is_valid_username("vlad!@#"))      # Должно быть False

print(extract_prices("Price: $100 and 50 руб"))  # Должно найти ['100', '50']
print(is_valid_color("#FFFFFF"))         # Должно быть True

# ТРИ ГЛАВНЫХ ПРАВИЛА:
#1. ^ и $ - ЯКОРИ для полного совпадения
#2. {n,m} - ДИАПАЗОН через ЗАПЯТУЮ
#3. \d \w \s - СПЕЦСИМВОЛЫ через ОБРАТНЫЙ СЛЕШ