def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Ціна'] * details['Залишок']
        print(f"Вартість залишку для {product}: {stock_value:.2f} грн")


def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Залишок'] < 10:
            # Формула розрахунку знижки (5%)
            discount = details['Ціна'] * 0.05
            new_price = details['Ціна'] - discount

            # ✅ Оновлюємо ціну в словнику, щоб зберегти нову ціну
            details['Ціна'] = new_price

            print(f"Знижка для {product}: {discount:.2f} грн (нова ціна: {new_price:.2f} грн)")
        else:
            print(f"Для {product} знижка не застосовується, залишок — {details['Залишок']} одиниць.")
