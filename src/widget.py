from src import masks


def mask_account_card(card_or_account_details: str) -> str:
    """Функция, которая возвращает название карты или счета и маску номера"""
    list_card_or_account_details = card_or_account_details.split()
    numbers = list_card_or_account_details[-1]
    account_or_card_name = list_card_or_account_details[:-1]
    if list_card_or_account_details[0] == "Счет":
        masked_numbers = masks.get_mask_account(int(numbers))
    else:
        masked_numbers = masks.get_mask_card_number(int(numbers))
    return " ".join(account_or_card_name) + " " + str(masked_numbers)


def get_date(data: str) -> str:
    """Функция, которая показывает дату"""
    year = data[:4]
    month = data[5:7]
    day = data[8:10]
    return day + "." + month + "." + year
