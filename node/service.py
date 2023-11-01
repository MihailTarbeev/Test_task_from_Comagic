from typing import List
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue
from node.execute import ExecuteView


class NodeType(flow.NodeType):
    id: str = 'a9d20dc8-9334-4890-98a9-fdc98397fc56'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'MyCRM'
    displayName: str = 'MyCRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">📝</text></svg>'
    description: str = 'This is a Authorization service in MyCRM'
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
                    name='Сбор данных',
                    value='Сбор данных',
                ),
            ]
        ),
        Property(
            displayName='Адрес CRM',
            name='Адрес',
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
            displayName='Id филиала',
            name='Id филиала',
            type=Property.Type.NUMBER,
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
            displayName='Email',
            name='Email',
            type=Property.Type.EMAIL,
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
            displayName='API key',
            name='API key',
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
            displayName='Data',
            name='Data',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Сбор данных',
                    ],
                },
            ),
        ),
        Property(
            displayName='Resource',
            name='Resource',
            type=Property.Type.OPTIONS,
            required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Сбор данных',
                    ],
                },
            ),
            options=[
            OptionValue(
                    name='Customer',
                    value='Customer',
                ),
            ]
        ),
        Property(
            displayName='Operation',
            name='Operation',
            type=Property.Type.OPTIONS,
            required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Сбор данных',
                    ],
                    'Resource': [
                        'Customer',
                    ],
                },
            ),
            options=[
            OptionValue(
                    name='Index',
                    value='Index',
                ),
            OptionValue(
                    name='Create',
                    value='Create',
                ),
            OptionValue(
                    name='Update',
                    value='Update',
                ),
            ]
        ),
        Property(
            displayName='Parameters',
            name='Parameters_index',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Сбор данных',
                    ],
                    'Resource': [
                        'Customer',
                    ],
                    'Operation': [
                        'Index',
                    ]
                },
            ),
            options=[
                Property(
                    displayName='id',
                    name='id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id клиента',
                ),
                Property(
                    displayName='is_study',
                    name='is_study',
                    type=Property.Type.OPTIONS,
                    default='',
                    description='состояние клиента',
                    options=[
                        OptionValue(
                                name='Лид',
                                value='0',
                            ),
                        OptionValue(
                                name='Клиент',
                                value='1',
                            ),
                    ]
                ),
                Property(
                    displayName='study_status_id',
                    name='study_status_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id статус клиента',
                ),
                Property(
                    displayName='name',
                    name='name',
                    type=Property.Type.STRING,
                    default='',
                    description='имя клиента',
                ),
                Property(
                    displayName='gender',
                    name='gender',
                    type=Property.Type.STRING,
                    default='',
                    description='пол клиента',
                ),
                Property(
                    displayName='age_from',
                    name='age_from',
                    type=Property.Type.NUMBER,
                    default='',
                    description='возраст клиента от',
                ),
                Property(
                    displayName='age_to',
                    name='age_to',
                    type=Property.Type.NUMBER,
                    default='',
                    description='возраст клиента до',
                ),
                Property(
                    displayName='phone',
                    name='phone ',
                    type=Property.Type.NUMBER,
                    default='',
                    description='контакты клиента',
                ),
                Property(
                    displayName='legal_type',
                    name='legal_type',
                    type=Property.Type.OPTIONS,
                    default='',
                    description='тип заказчика',
                    options=[
                        OptionValue(
                                name='Физ. лицо',
                                value='1',
                            ),
                        OptionValue(
                                name='Юр. Лицо',
                                value='2',
                            ),
                    ]
                ),
                Property(
                    displayName='legal_name',
                    name='legal_name',
                    type=Property.Type.STRING,
                    default='',
                    description='Имя заказчика',
                ),
                Property(
                    displayName='company_id',
                    name='company_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id юр. лица',
                ),
                Property(
                    displayName='lesson_count_from',
                    name='lesson_count_from',
                    type=Property.Type.NUMBER,
                    default='',
                    description='остаток уроков от',
                ),
                Property(
                    displayName='lesson_count_to',
                    name='lesson_count_to',
                    type=Property.Type.NUMBER,
                    default='',
                    description='остаток уроков до',
                ),
                Property(
                    displayName='balance_contract_from',
                    name='balance_contract_from',
                    type=Property.Type.NUMBER,
                    default='баланс договора от',
                    description='баланс договора от',
                ),
                Property(
                    displayName='balance_contract_to',
                    name='balance_contract_to',
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс договора до',
                ),
                Property(
                    displayName='balance_bonus_from',
                    name='balance_bonus_from',
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс бонусов от',
                ),
                Property(
                    displayName='balance_bonus_to',
                    name='balance_bonus_to',
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс бонусов до',
                ),
                Property(
                    displayName='removed',
                    name='removed',
                    type=Property.Type.OPTIONS,
                    default='',
                    description='флаг архивности',
                    options=[
                        OptionValue(
                                name='только активные',
                                value='0',
                            ),
                        OptionValue(
                                name='активные и архивные',
                                value='1',
                            ),
                        OptionValue(
                                name='только архивные',
                                value='2',
                            ),
                    ]
                ),
                Property(
                    displayName='removed_from',
                    name='removed_from',
                    type=Property.Type.DATE,
                    default='',
                    description='дата отправки в архив от',
                ),
                Property(
                    displayName='removed_to',
                    name='removed_to',
                    type=Property.Type.DATE,
                    default='',
                    description='дата отправки в архив',
                ),
                Property(
                    displayName='level_id',
                    name='level_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id уровня знаний',
                ),
                Property(
                    displayName='assigned_id',
                    name='assigned_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id ответственного менеджера',
                ),
                Property(
                    displayName='employee_id',
                    name='employee_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id ответственного педагога',
                ),
                Property(
                    displayName='lead_source_id ',
                    name='lead_source_id ',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id источника',
                ),
                Property(
                    displayName='color',
                    name='color',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id цвета',
                ),
                Property(
                    displayName='note',
                    name='note',
                    type=Property.Type.STRING,
                    default='',
                    description='примечание',
                ),
                Property(
                    displayName='date_from',
                    name='date_from',
                    type=Property.Type.DATE,
                    default='дата добавления от',
                    description='дата добавления от',
                ),
                Property(
                    displayName='date_to',
                    name='date_to',
                    type=Property.Type.DATE,
                    default='',
                    description='дата добавления до',
                ),
                Property(
                    displayName='next_lesson_date_from',
                    name='next_lesson_date_from',
                    type=Property.Type.DATE,
                    default='',
                    description='дата след.посещения от',
                ),
                Property(
                    displayName='next_lesson_date_to',
                    name='next_lesson_date_to',
                    type=Property.Type.DATE,
                    default='',
                    description='дата след.посещения до',
                ),
                Property(
                    displayName='tariff_till_from',
                    name='tariff_till_from',
                    type=Property.Type.DATE,
                    default='',
                    description='дата действия абонемента от',
                ),
                Property(
                    displayName='tariff_till_to',
                    name='tariff_till_to',
                    type=Property.Type.DATE,
                    default='',
                    description='дата действия абонемента до',
                ),
                Property(
                    displayName='customer_reject_id',
                    name='customer_reject_id',
                    type=Property.Type.NUMBER,
                    default='',
                    description='id причины отказа',
                ),
                Property(
                    displayName='comment',
                    name='comment',
                    type=Property.Type.NUMBER,
                    default='',
                    description='комментарий',
                ),
                Property(
                    displayName='dob_from',
                    name='dob_from',
                    type=Property.Type.DATE,
                    default='',
                    description='дата рождения от',
                ),
                Property(
                    displayName='dob_to',
                    name='dob_to',
                    type=Property.Type.DATE,
                    default='',
                    description='дата рождения до',
                ),
                Property(
                    displayName='withGroups:true',
                    name='withGroups:true',
                    type=Property.Type.NUMBER,
                    default='',
                    description='активные группы клиента',
                ),
            ]
        ),
        Property(
            displayName='Id',
            name='Id_update',
            type=Property.Type.NUMBER,
            required= True,
            default='',
            displayOptions=DisplayOptions(
                show={
                    'Действие': [
                        'Сбор данных',
                    ],
                    'Resource': [
                        'Customer',
                    ],
                    'Operation': [
                        'Update',
                    ],
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