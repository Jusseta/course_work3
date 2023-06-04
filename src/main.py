from data import get_data, sort_data
from utils import get_operations, encode_numbers


data = sort_data(get_data('operations.json'))
encode_operations = encode_numbers(get_operations(data))


def print_operation(encode_operation):
    operations = []
    for i in encode_operation:
        operations.append(f"\n{i['date']} {i['description']}\n"
                          f"{i['from_whom']} --> {i['to_whom']}\n"
                          f"{i['amount']} {i['name']}\n")
    return operations


print(''.join(print_operation(encode_operations)))
