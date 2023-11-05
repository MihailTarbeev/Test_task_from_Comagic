import json as internal_json
from uc_http_requester.requester import Request


async def validate_response(response):
    '''Проверка статус-кода запроса'''
    response = await response.execute()
    if response.status_code == 200:
        data = internal_json.loads(response.text)
    else:
        content = internal_json.loads(response.content)
        if content['error']:
            raise Exception(content['error_description'])
    return data



async def get_access_token(client_id: str, client_secret:str, refresh_token: str):
    '''Извлечение access_token из Request-объекта'''
    response = request_for_access_token(client_id, client_secret, refresh_token)
    data = await validate_response(response)
    return data['access_token']

    
def request_for_access_token(client_id: str, client_secret:str, refresh_token: str):
    '''Создание Request-объекта, содержащего access_token'''
    return Request(
                url = 'https://www.googleapis.com/oauth2/v4/token',
                method=Request.Method.post,
                params= {
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'refresh_token': refresh_token,
                    'grant_type': "refresh_token"
                    })


async def get_list_files(access_token):
    '''Обработка Request-объекта к виду словаря, ключами которого являются порядковые номера файлов, а значениями id и названия файлов'''
    files = {}
    count = 0
    nextPageToken = None
    while True:
        response = request_get_list_files(access_token, nextPageToken)
        data = await validate_response(response)
        for item in data['items']:
            count += 1
            files[count] = { 
                'title': item['title'],
                'id': item['id'],
                }
        if not data.get("nextPageToken"):
            break
        nextPageToken = data['nextPageToken']
    return files


def request_get_list_files(access_token, pageToken:str = None):
    '''Создание Request-объекта, содержащего список файлов, имеющихся на гугл-диске'''
    params = {}
    if pageToken:
        params['pageToken'] = pageToken
    return Request(
                url = 'https://www.googleapis.com/drive/v2/files',
                method=Request.Method.get,
                headers={"Authorization": "Bearer " + access_token},
                params= params
    )

async def upload_file(access_token: str, file: str):
    '''Загрузка файла на гугл диск'''
    file_name = file[0]["name"]
    file_path = file[0]["path"]
    response = await get_content_from_path(file_path).execute()
    content = response.text
    resp_empty_file = create_empty_file(access_token, file_name)
    data = await validate_response(resp_empty_file)
    id = data["id"]
    await validate_response(add_content_into_file(access_token, id, content))
    return f'Ваш файл {file_name} успешно загружен.'


def create_empty_file(access_token: str, file_name: str):
    '''Создание пусого файла на гугл диске'''
    return Request(
        url = "https://www.googleapis.com/drive/v2/files",
        method=Request.Method.post,
        headers={"Authorization": "Bearer " + access_token},
        json= {"title": file_name, "mimeType": "mime/type"}
        )


def add_content_into_file(access_token: str, id: str, content: str):
    '''Запись контента в созданный раннее пустой файл на гугл диске'''
    return Request(
        url = f"https://www.googleapis.com/upload/drive/v2/files/{id}",
        method=Request.Method.put,
        headers={"Authorization": "Bearer " + access_token, "Content-Transfer-Encoding": "base64"},
        params={"uploadType": "media"},
        data=content
        )


def get_content_from_path(path: str):
    '''Создание Request-объекта, содержащего контент файла'''
    return Request(url=path, method=Request.Method.get)