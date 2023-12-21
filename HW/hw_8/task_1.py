# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import csv
import pickle
from pathlib import Path


def get_directory_info(directory_path):
    directory_path = Path(directory_path)
    directory_info = {}

    def explore_directory(dir_path):
        dir_size = 0
        children = []

        for item in dir_path.iterdir():
            if item.is_dir():
                child_info = explore_directory(item)
                children.append({"name": item.name, "type": "directory", "size": child_info["size"],
                                 "children": child_info["children"]})
                dir_size += child_info["size"]
            elif item.is_file():
                file_size = item.stat().st_size
                children.append({"name": item.name, "type": "file", "size": file_size})
                dir_size += file_size

        return {"size": dir_size, "children": children}

    directory_info = explore_directory(directory_path)

    with open('directory_info.json', 'w') as json_file:
        json.dump(directory_info, json_file)

    with open('directory_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["name", "type", "size"])

        def write_csv_data(data):
            for item in data["children"]:
                csv_writer.writerow([item["name"], item["type"], item["size"]])
                if item["type"] == "directory":
                    write_csv_data(item)

        write_csv_data(directory_info)

    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(directory_info, pickle_file)


get_directory_info("test")
