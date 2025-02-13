def hide_card_number() -> str:
    """Функция запрашивает номер карты и возвращает его в замаскированном формате."""
    card_num = input("Введите номер карты: ")
    # Убираем пробелы и проверяем, что введены только цифры
    cleaned_num = "".join(card_num.split())
    if not cleaned_num.isdigit() or len(cleaned_num) != 16:
        return "Ошибка: номер карты должен состоять из 16 цифр."
    # Маскируем номер карты
    masked_num = f"{cleaned_num[:4]} {cleaned_num[4:6]}** **** {cleaned_num[-4:]}"
    return masked_num


def hide_account_number() -> str:
    """Функция запрашивает номер счета и возвращает его в замаскированном формате."""
    account_num = input("Введите номер счета: ")
    # Убираем пробелы и проверяем, что введены только цифры
    cleaned_num = "".join(account_num.split())
    if not cleaned_num.isdigit() or len(cleaned_num) < 4:
        return "Ошибка: номер счета должен содержать минимум 4 цифры."
    # Маскируем номер счета
    masked_num = f"**{cleaned_num[-4:]}"
    return masked_num


# Пример использования
if __name__ == "__main__":
    print(hide_card_number())
    print(hide_account_number())
