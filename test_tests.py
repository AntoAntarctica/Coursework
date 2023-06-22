from main import change_date_format, masking_card, output_money, sort_by_date


def test_change_date_format():
    """
    Функия читает дату и время
    :return: Переворачивает и выводит дату и отсекает время
    """

    assert change_date_format("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert change_date_format("2022-12-31T23:59:59.345232") == "31.12.2022"


def test_masking_card():
    """
    Функция читает формат счета или номер карты
    :return: В каждом из двух случаев скрывает символы определенным количеством звездочек
    """

    assert masking_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98 **** 7658"
    assert masking_card("Счет 78808375133947439319") == "Счет ********* 9319"


def test_output_money():
    """
    Функция считывает количество и валюту
    :return: выводит в нужном формате
    """
    operation_amount = {
        "amount": 100.0,
        "currency": {
            "name": "USD"
        }
    }
    assert output_money(operation_amount) == "100.0 USD"

    operation_amount = {
        "amount": 50.0,
        "currency": {
            "name": "EUR"
        }
    }
    assert output_money(operation_amount) == "50.0 EUR"


def test_sort_by_date():
    """
    Считываем операции
    :return: список выполненных операций, отсортированных по дате
    """
    data = [
        {"state": "EXECUTED", "date": "2023-06-20"},
        {"state": "PENDING", "date": "2023-06-22"},
        {"state": "EXECUTED", "date": "2023-06-21"},
        {"state": "EXECUTED", "date": "2023-06-23"},
    ]

    sorted_operations = sort_by_date(data)

    assert sorted_operations[0]["date"] == "2023-06-23"
    assert sorted_operations[1]["date"] == "2023-06-21"
    assert sorted_operations[2]["date"] == "2023-06-20"

    for operation in sorted_operations:
        assert operation["state"] == "EXECUTED"
