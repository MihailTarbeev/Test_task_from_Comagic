from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from .provider import get_list_files, get_access_token, upload_file

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            prop = json.node.data.properties
            if prop['Действие'] == 'Авторизация':
                client_id = prop['client_id']
                client_secret = prop['client_secret']
                refresh_token = prop['refresh_token']
                client_id = prop['client_id']
                file = await prop['Файл']
                access_token = await get_access_token(client_id, client_secret, refresh_token)
                await json.save_result({
                        "access_token": access_token,
                        "file": file,
                    })
            elif prop['Действие'] == 'Работа с данными':
                if prop["Операция"] == 'Загрузка файла':
                    data = await prop['data']
                    access_token = data['access_token']
                    file = data['file']
                    result = await upload_file(access_token, file)
                    await json.save_result({
                        "result": result
                    })
                elif prop["Операция"] == 'Получение списка файлов':
                    access_token = (await prop['data'])['access_token']
                    files = await get_list_files(access_token)
                    await json.save_result({
                        "file_list": files,
                    })
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
