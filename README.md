Операции по счетам

Программа выводит на экран список из 5 последних выполненных клиентом операций из файла operations.json в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

Номер карты и номер счета замаскированы и не отображаются целиком



В файле operations.json хронятся следующие данные:

- `id` — id транзакциии
- `date` — информация о дате совершения операции
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутстовать)
- `to` — куда


Для файлов json прописан абсолютный путь
