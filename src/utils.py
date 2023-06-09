from datetime import datetime


def get_operations(sorted_data):
    '''
    Выберает 5 первых словарей, преобразует дату и составляет список словарей в удобном формате
    :param sorted_data: список словарей
    :return: список словарей в нужном формате
    '''
    operations = []
    for i in sorted_data[:5]:
        date = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')
        description = i['description']
        if 'from' in i:
            from_whom = i['from']
        else:
            from_whom = ''
        to_whom = i['to']
        amount = i['operationAmount']['amount']
        name = i['operationAmount']['currency']['name']

        one_operation = {'date':date, 'description':description, 'from_whom':from_whom,
                         'to_whom':to_whom, 'amount':amount, 'name':name}
        operations.append(one_operation)

    return operations


def encode_numbers(operations):
    '''
    Кодирует номер отправителя и номер счета, делит номер карты на блоки по 4 цифры
    :param operations: список словарей
    :return: список словарей с закодированными номерами
    '''
    encode_operations = operations
    for i in encode_operations:
        from_whom_count = len(i['from_whom'].split(" ")[-1]) - 10
        from_whom_temp = i['from_whom'].split(" ")[-1][:6] + "*" * from_whom_count + i['from_whom'][-4:]
        i['from_whom'] = i['from_whom'].split(" ")[0] + ' ' + from_whom_temp

        to_whom_temp = "*" * 2 + i['to_whom'].split(" ")[1][-4:]
        i['to_whom'] = i['to_whom'].split(" ")[0] + ' ' + to_whom_temp

    for i in encode_operations:
        s = i['from_whom'].split(" ")
        chunk = [s[-1][i:i+4] for i in range(0, len(s[-1]), 4)]
        i['from_whom'] = ' '.join(s[:-1]), ' '.join(chunk)

    return encode_operations
