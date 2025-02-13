from src.masks import hide_account_number, hide_card_number

"""
# Проверка функции mask_card() с аннотациями типов
"""


def test_mask_card() -> None:
    assert hide_card_number("1488148814881488") == "1488 14** **** 1488"
    assert hide_card_number("464646464646") == "Некорректный номер карты"


"""
# Проверка функции hide_account_number() с аннотациями типов
"""


def test_mask_account() -> None:
    assert hide_account_number("73654108430135871488") == "**1488"
    assert hide_account_number("1488") == "Некорректный номер счета"
