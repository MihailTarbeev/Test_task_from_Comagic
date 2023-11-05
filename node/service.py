from typing import List
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue
from node.execute import ExecuteView

class NodeType(flow.NodeType):
    id: str = 'c9bedd90-fce9-4bcf-bb31-278c3ad575ef'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'MyApp'
    displayName: str = 'MyApp'
    icon: str = '<svg><text x="8" y="50" font-size="50">💭</text></svg>'
    description: str = 'This is a service for relation with Google Drive Api'
    properties: List[Property] = [
        Property(
            displayName='Действие',
            name='Действие',
            type=Property.Type.OPTIONS,
	        required= True,
            default='',
            options=[
                OptionValue(
                    name='Авторизация',
                    value='Авторизация',
                ),
                OptionValue(
                    name='Работа с данными',
                    value='Работа с данными',
                ),
            ]
        ),
        Property(
            displayName='client_id',
            name='client_id',
            type=Property.Type.STRING,
	        required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Авторизация',
                    ],
                },
            ),
        ),
        Property(
            displayName='client_secret',
            name='client_secret',
            type=Property.Type.STRING,
	        required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Авторизация',
                    ],
                },
            ),
        ),
        Property(
            displayName='refresh_token',
            name='refresh_token',
            type=Property.Type.STRING,
	        required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Авторизация',
                    ],
                },
            ),
        ),
        Property(
            displayName='Файл',
            name='Файл',
            type=Property.Type.JSON,
	        required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Авторизация',
                    ],
                },
            ),
        ),
        Property(
            displayName='Операция',
            name='Операция',
            type=Property.Type.OPTIONS,
            required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Работа с данными',
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Загрузка файла',
                    value='Загрузка файла',
                ),
                OptionValue(
                    name='Получение списка файлов',
                    value='Получение списка файлов',
                ),
            ]
        ),
        Property(
            displayName='data',
            name='data',
            type=Property.Type.JSON,
            required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Работа с данными',
                    ]
                },
            ),
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType

class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView