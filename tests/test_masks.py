from src.masks import mask_account, mask_card

"""
# Проверка функции mask_card() с аннотациями типов
"""


def test_mask_card() -> None:
    assert mask_card("1488148814881488") == "1488 14** **** 1488"
    assert mask_card("4646464") == "Некорректный номер карты"


"""
# Проверка функции hide_account_number() с аннотациями типов
"""


def test_mask_account() -> None:
    assert mask_account("73654108430135871488") == "**1488"
    assert mask_account("1488") == "Некорректный номер счета"
