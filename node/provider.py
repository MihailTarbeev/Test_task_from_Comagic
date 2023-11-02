from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json
import requests

gauth = GoogleAuth()


def write_private_data(data):
    with open("client_secrets.json", "w") as jsonFile:
        json.dump(data, jsonFile)


def authorization():
    gauth.LocalWebserverAuth()


def create_and_upload_file(file_name='text.txt', path=None):
    try:
        drive = GoogleDrive(gauth)
        my_file = drive.CreateFile({"title": f'{file_name}'})
        if path:
            content = requests.get(path).text
            my_file.SetContentString(content)
            my_file.Upload()
            return f'Файл {file_name} успешно загружен!'
    except Exception as e:
        return e


def get_list_files():
    try:
        drive = GoogleDrive(gauth)
        my_files = drive.ListFile().GetList()
        data = {}
        id = 0
        for file in my_files:
            id += 1
            data[id] = file['title']
        return data
    except Exception as e:
        return e