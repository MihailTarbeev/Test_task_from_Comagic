from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from .provider import create_and_upload_file, write_private_data, authorization, get_list_files


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            prop = json.node.data.properties
            if prop['Действие'] == 'Авторизация':
                private_data = prop['Приватные данные']
                write_private_data(private_data)
                authorization()
                file = await prop['Файл']
                await json.save_result({
                    "file": file
                })
            elif prop['Действие'] == 'Работа с данными':
                if prop["Операция"] == 'Загрузка файла':
                    file = await prop['Data']
                    file_name = file["file"][0]["name"]
                    file_path = file["file"][0]["path"]
                    result = create_and_upload_file(file_name=file_name, path=file_path)
                    await json.save_result({
                        "result": result
                    })
                elif prop["Операция"] == 'Получение списка файлов':
                    result = get_list_files()
                    await json.save_result(result)
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
