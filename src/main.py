from src.data import get_data, sort_data
from src.utils import get_operations, encode_numbers
import os


def print_operation(encode_operation):
    '''
    Создает список для вывода в нужном формате
    :param encode_operation: список словарей с закодированными номерами
    :return: готовый вывод
    '''
    operations = []
    for i in encode_operation:
        operations.append(f"\n{i['date']} {i['description']}\n"
                          f"{i['from_whom']} --> {i['to_whom']}\n"
                          f"{i['amount']} {i['name']}\n")
    return ''.join(operations)


path = os.path.join(os.path.dirname(__file__), 'operations.json')
data = sort_data(get_data(path))
encode_operations = encode_numbers(get_operations(data))

print(print_operation(encode_operations))
