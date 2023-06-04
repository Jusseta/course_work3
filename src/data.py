import json


def get_data(json_file):
    '''
    Функция читает файл json и преобразует в объект python
    :param json_file: файл формата json
    :return: список словарей
    '''
    with open(json_file, encoding='utf-8') as file:
        all_data = json.loads(file.read())
        return all_data


def sort_data(data):
    '''
    Сортирует словари по статусу и оставляет только выполненные ("EXECUTED")
    :param data: данные для сортировки
    :return: список словарей от нового к старому
    '''
    full_data = []
    for i in data:
        if 'state' in i:
            if i['state'] == "EXECUTED":
                full_data.append(i)
    return sorted(full_data, key=lambda k: k['date'].split('.'), reverse=True)
