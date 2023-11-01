from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from .provider import get_authorization_request, get_index_request
import json as my_json

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            prop = json.node.data.properties
            if prop['Действие'] == 'Авторизация':
                domain = prop['Адрес']
                email = prop['Email']
                api_key = prop['API key']
                branch = prop['Id филиала']
                result = await get_authorization_request(domain, api_key, email).execute()
                if not result.is_error:
                    await json.save_result({
                        "branch": branch,
                        "domain": domain,
                        "email": email,
                        "api_key": api_key,
                        "token": eval(result.text)['token'],
                    })
                else:
                    raise Exception('Неверные данные')
            elif prop['Действие'] == 'Сбор данных':
                auth_data = await prop['Data']
                if prop['Resource'] == 'Customer':
                    if prop['Operation'] == 'Index':
                        result = await get_index_request(auth_data["domain"], auth_data["branch"], auth_data["token"], prop['Parameters_index']).execute()
                        if not result.is_error:
                            await json.save_result({
                                "result": my_json.loads(result.text),
                            })
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
