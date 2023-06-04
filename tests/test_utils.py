from src.utils import get_operations, encode_numbers
from src.data import get_data, sort_data


def test_get_operations():
    assert get_operations(sort_data(get_data('test_operations.json'))) == [{'date': '03.03.2019', 'description': 'Перевод с карты на счет',
                                                                            'from_whom': 'Visa Classic 6319351940209800',
                                                                            'to_whom': 'Счет 14073196441261107791',
                                                                            'amount': '44493.45', 'name': 'USD'},
                                                                           {'date': '25.08.2018', 'description': 'Перевод с карты на карту',
                                                                            'from_whom': 'Visa Classic 4040551273087672',
                                                                            'to_whom': 'Visa Platinum 7825450883088021',
                                                                            'amount': '52245.30', 'name': 'USD'}]


def test_encode_numbers():
    assert encode_numbers(get_operations(sort_data(get_data('test_operations.json')))) == [{'amount': '44493.45',
  'date': '03.03.2019',
  'description': 'Перевод с карты на счет',
  'from_whom': 'Visa 631935******9800',
  'name': 'USD',
  'to_whom': 'Счет **7791'},
 {'amount': '52245.30',
  'date': '25.08.2018',
  'description': 'Перевод с карты на карту',
  'from_whom': 'Visa 404055******7672',
  'name': 'USD',
  'to_whom': 'Visa **inum'}]
