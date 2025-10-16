from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name


# 1. Введення товарів
products = input_product()

# 2. Розрахунок вартості залишку
print("\n--- Вартість залишку ---")
calculate_stock_value(products)

# 3. Розрахунок знижки
print("\n--- Розрахунок знижки ---")
calculate_discount(products)

# 4. Виведення назв товарів
print("\n--- Список товарів ---")
product_names = list(products.keys())
print_product_names(product_names)

# 5. Пошук товару
print("\n--- Пошук товару ---")
search_name = input("Введіть назву товару для пошуку: ")
find_product_by_name(products, search_name)
