from datetime import datetime
from src.masks import hide_account_number, hide_card_number

def hide_number(data: str) -> str:
    """
    Принимает строку с типом карты/счета и номером, возвращает строку с замаскированным номером.
    """
    parts = data.split()
    if parts[0] in ["Visa", "MasterCard", "Maestro"]:
        digits = "".join([x for x in parts if x.isdigit()])
        masked = hide_card_number(digits)
        return " ".join([x for x in parts if x.isalpha()]) + " " + masked
    elif parts[0] == "Счет":
        return "Счет " + hide_account_number(parts[1])
    else:
        return data


def format_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате ISO и возвращает в формате DD.MM.YYYY.
    """
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")