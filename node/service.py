import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState, DisplayOptions
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '5eea9e49-9b46-4c68-9934-5801957a541c'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'Adder'
    displayName: str = 'Adder'
    icon: str = '<svg><text x="8" y="50" font-size="50">➕</text></svg>'
    description: str = 'This service sums numbers types Int and Str'
    properties: List[Property] = [
        Property(
            displayName='Текстовое поле',
            name='Текст',
            type=Property.Type.STRING,
            # placeholder='0',
            description='Поле для числа типа string',
            required=True,
            default='0',
        ),
        Property(
            displayName='Числовое поле',
            name='Число',
            type=Property.Type.NUMBER,
            description='Поле для числа типа Int',
            required=True,
            default=0,
        ),
        Property(
            displayName='Вернуть тип Число/Текст',
            name='Переключатель',
            type=Property.Type.BOOLEAN,
            description='Выбор типа возвращаемых данных',
            required=True,
            default=False,
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            result = int(json.node.data.properties['Текст']) + json.node.data.properties['Число']
            if json.node.data.properties['Переключатель']:
                result = str(result)
            await json.save_result({
                "result": result
            })
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView