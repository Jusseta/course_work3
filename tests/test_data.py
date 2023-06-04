from src.data import get_data, sort_data


def test_get_data():
    assert get_data('test_operations.json') == [
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


def test_sort_data():
    assert sort_data(get_data('test_operations.json')) == [
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
]