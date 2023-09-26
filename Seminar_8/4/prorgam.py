"""📌Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌Дополните id до 10 цифр незначащими нулями.
📌В именах первую букву сделайте прописной.
📌Добавьте поле хеш на основе имени и идентификатора.
📌Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
📌Имя исходного и конечного файлов передавайте как аргументы функции."""

import json


def csv_read(csv_file, new_json):
    final_dict = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, itens in enumerate(data):
        data[i] = data[i].strip().split(',')
        data[i][1] = data[i][1].zfill(10)
        final_dict[hash(data[i][0] + data[i][1])] = data[i]
    with open(new_json, 'w', encoding='utf-8')as file:
        json.dump(final_dict, file, indent=4, ensure_ascii=False)


csv_read('../3/my.csv', 'new_db.json')