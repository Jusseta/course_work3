import pytest


@pytest.fixture
def result_test_get_data():
    return [
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
              "amount": "44493.45",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
          },
          {
            "id": 51314762,
            "state": "EXECUTED",
            "date": "2018-08-25T02:58:18.764678",
            "operationAmount": {
              "amount": "52245.30",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 4040551273087672",
            "to": "Visa Platinum 7825450883088021"
          },
          {
            "id": 464419177,
            "state": "CANCELED",
            "date": "2018-07-15T18:44:13.346362",
            "operationAmount": {
              "amount": "71024.64",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 9657499677062945",
            "to": "Счет 19213886662094884261"
          }
        ]


@pytest.fixture
def data_for_sort():
    return [
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
              "amount": "44493.45",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
          },
        {
            "id": 464419177,
            "state": "CANCELED",
            "date": "2018-07-15T18:44:13.346362",
            "operationAmount": {
                "amount": "71024.64",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 9657499677062945",
            "to": "Счет 19213886662094884261"
        }
    ]


@pytest.fixture
def result_test_sort_data():
    return [
          {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
              "amount": "44493.45",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
          }]


@pytest.fixture
def result_test_get_operations():
    return [{
          'amount': '44493.45',
          'date': '03.03.2019',
          'description': 'Перевод с карты на счет',
          'from_whom': 'Visa Classic 6319351940209800',
          'name': 'USD',
          'to_whom': 'Счет 14073196441261107791'}]


@pytest.fixture
def result_test_encode_numbers():
    return [{'amount': '44493.45',
              'date': '03.03.2019',
              'description': 'Перевод с карты на счет',
              'from_whom': 'Visa 631935******9800',
              'name': 'USD',
              'to_whom': 'Счет **7791'}]


@pytest.fixture
def result_test_print_operation():
    return ('\n'
             '03.03.2019 Перевод с карты на счет\n'
             'Visa 631935******9800 --> Счет **7791\n'
             '44493.45 USD\n')
