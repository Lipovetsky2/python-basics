
# Калькулятор покупок

# Константи
DISCOUNT: float = 0.10

# Введення даних
name: str = str(input("Назва товару: "))
price: float = float(input("Ціна: "))
quantity: int = int(input("Кількість: "))

# Перевірка
valid: bool = price > 0 and quantity > 0

if not valid or name == "":
    print("Помилка введення!")

else:
    total = price * quantity

    # Розрахунок знижки
    if total >= 1000:
        discount = DISCOUNT
        if quantity >= 10:
            discount += 0.05
    elif total >= 500:
        discount = 0.05
    else:
        discount = 0.0

    final = total - total * discount
    result = "Є знижка" if discount > 0 else "Без знижки"

    # Спосіб оплати
    payment = int(input("Оплата (1-готівка, 2-картка): "))

    match payment:
        case 1:
            method = "Готівка"
        case 2:
            method = "Картка"
        case _:
            method = "Не вибрано"

    # Результат
    print("\n--- ЧЕК ---")
    print(f"Товар: {name}")
    print(f"Сума: {total:.2f} грн")
    print(f"Знижка: {discount * 100:.0f}%")
    print(f"До оплати: {final:.2f} грн")
    print(f"{result}")
    print(f"Оплата: {method}")
