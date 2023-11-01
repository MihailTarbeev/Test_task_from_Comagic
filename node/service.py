import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState, DisplayOptions, OptionValue
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
            name='Переключатель типов',
            type=Property.Type.BOOLEAN,
            description='Выбор типа возвращаемых данных',
            required=True,
            default=False,
        ),
        Property(
            displayName='Включить поля',
            name='Переключатель полей',
            type=Property.Type.BOOLEAN,
            description='Отображает два поля с выпадающими списками',
            required=True,
            default=False,
        ),
        Property(
            displayName='Список 1',
            name='Cписок 1',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'Переключатель полей': [
                        True,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Значение 1',
                    value='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value='Значение 2',
                ),
            ],
        ),
        Property(
            displayName='Список 2',
            name='Cписок 2',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'Переключатель полей': [
                        True,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Значение 1',
                    value='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value='Значение 2',
                ),
            ],
        ),
        Property(
            displayName='Почта',
            name='Почта',
            placeholder = 'Поле для ввода почты',
            type=Property.Type.EMAIL,
            displayOptions=DisplayOptions(
                show={
                    'Переключатель полей': [
                        True,
                    ],
                    'Cписок 1':
                    [
                        'Значение 1'
                    ],
                    'Cписок 2':
                    [
                        'Значение 1'
                    ],
                },
            ),
        ),
        Property(
            displayName='Дата и время',
            name='Дата и время',
            placeholder = 'Поле для ввода даты и времени',
            type=Property.Type.DATETIME,
            displayOptions=DisplayOptions(
                show={
                    'Переключатель полей': [
                        True,
                    ],
                    'Cписок 1':
                    [
                        'Значение 2'
                    ],
                    'Cписок 2':
                    [
                        'Значение 2'
                    ],
                },
            ),
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            result = int(json.node.data.properties['Текст']) + json.node.data.properties['Число']
            is_text = json.node.data.properties['Переключатель типов']
            if is_text:
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