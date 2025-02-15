from datetime import datetime

from src.masks import mask_account, mask_card


def hide_number(data: str) -> str:
    """
    Принимает строку с типом карты/счета и номером, возвращает строку с замаскированным номером.
    """
    parts = data.split()
    if parts[0] in ["Visa", "MasterCard", "Maestro"]:
        digits = "".join([x for x in parts if x.isdigit()])  # Извлекаем цифры номера карты
        masked = mask_card(digits)  # Передаём только цифры номера карты
        return " ".join([x for x in parts if x.isalpha()]) + " " + masked
    elif parts[0] == "Счет":
        account_number = parts[1]  # Извлекаем номер счёта
        masked = mask_account(account_number)  # Передаём только номер счёта
        return "Счет " + masked
    else:
        return data


def format_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате ISO и возвращает в формате DD.MM.YYYY.
    """
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")
