import csv
import json
import os
import pickle


def path_info(path=os.getcwd()):
	path_list = []
	size_path = {}
	for dir_path, dir_name, file_name in os.walk(path):
		for file in file_name:
			size_path[dir_path] = os.stat(os.path.join(dir_path, file)).st_size + size_path.get(dir_path, 0)
			path_list.append({'name': file,
							  'parent_dir': '' if dir_path == path else os.path.basename(dir_path),
							  'type': 'file',
							  'size': os.stat(os.path.join(dir_path, file)).st_size})
	for dir_path, dir_name, file_name in os.walk(path):
		for folder in dir_name:
			size_path[dir_path] = size_path.get(dir_path, 0) + size_path.get(os.path.join(dir_path, folder), 0)
	for dir_path, dir_name, file_name in os.walk(path):
		for folder in dir_name:
			path_list.append({'name': folder,
							  'parent_dir': '' if dir_path == path else os.path.basename(dir_path),
							  'type': 'folder',
							  'size': size_path[os.path.join(dir_path, folder)]})
	return path_list


def create_csv(path_list):
	with open('result.csv', 'w', encoding='utf-8')as file:
		csv_write = csv.DictWriter(file, dialect='excel', fieldnames=['name', 'parent_dir', 'type', 'size'])
		csv_write.writeheader()
		csv_write.writerows(path_list)


def create_json(path_list):
	with open('result.json', 'w', encoding='utf-8') as file:
		json.dump(path_list, file, indent=4, ensure_ascii=False)


def create_pickle(path_list):
	with open('result.pickle', 'wb')as file:
		pickle.dump(dir_list, file)


dir_list = path_info()
create_json(dir_list)
create_pickle(dir_list)
create_csv(dir_list)
