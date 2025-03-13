from operator import itemgetter


def filter_by_state(transaction_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает список словарей по ключу state"""
    new_list = []
    for transaction in transaction_data:
        if transaction["state"] == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(transaction_data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует ключ date по возрастанию"""
    sorted_transaction_data = sorted(transaction_data, key=itemgetter("date"), reverse=reverse)
    return sorted_transaction_data
