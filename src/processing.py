def filter_by_state(transaction_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает список словарей по ключу state"""
    new_list = []
    for i in transaction_data:
        if i["state"] == state:
            new_list.append(i)
    return new_list