def get_mask_card_number(card_number: int) -> str:
    """Функция, которая принимает номер карты и маскирует его"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция, которая принимает номер счета и маскирует его"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"
