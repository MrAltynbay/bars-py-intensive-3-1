from django.http import HttpResponse
from django.template import loader
from m3.actions import ActionPack, Action, ACD
from m3_django_compat import get_user_model
from m3_ext.ui.results import ExtUIScriptResult
from recordpack.recordpack import BaseRecordPack
from day_12.providers import ModelProvider
from day_12.ui import MasterPanel, MasterWindow, GridWindow, EditUserWindow, CreateUserWindow

User = get_user_model()


class MasterPack(ActionPack):
    """
    Корневой пак для приложения
    """
    url = ''

    def __init__(self):
        super().__init__()
        self.actions.extend([
            MasterAction(),
            WindowAction(),
            GridAction(),
        ])

        # добавим дочерний пак для элементов грида
        self.grid_pack = MasterRecordPack()
        self.subpacks.extend([
            self.grid_pack
        ])


class MasterAction(Action):
    """
    Корневой экшен - отображение страницы приложения
    """
    url = '/'

    def run(self, request, context):
        # создадим панельку
        panel = MasterPanel()
        # рендерим шаблон страницы и компоненты
        content = loader.render_to_string('master.html', {
            'panel': panel.render(),
        })

        return HttpResponse(content)


class WindowAction(Action):
    """
    Пример экшена окна с декларацией контекста
    """
    url = '/win1'

    def context_declaration(self):
        return [
            ACD(name='str_field', type=str, default='', required=True)
        ]

    def run(self, request, context):
        # создадим окно
        win = MasterWindow()
        # заполним поля из контекста
        win.str_field.value = context.str_field

        # выведем результат - рендер окна
        return ExtUIScriptResult(win, context)


class GridAction(Action):
    """
    Пример окна с гридом
    """
    url = '/gridwin'

    def run(self, request, context):
        # создадим окно с гридом
        win = GridWindow()
        # выполним бинд пака и грида на окне
        self.parent.grid_pack.bind_to_grid(request, context, win.grid)

        return ExtUIScriptResult(win, context)


class MasterRecordPack(BaseRecordPack):
    """
    Пример RecordPack
    """
    url = '/grid'
    provider = ModelProvider(
        data_source=User,
        key_field='id',
    )
    edit_window = EditUserWindow
    new_window = CreateUserWindow

    quick_filters = {
        'first_name': {'control': {'xtype': 'textfield'}},
        'last_name': {'control': {'xtype': 'textfield'}},
        'username': {'control': {'xtype': 'textfield'}},
        'email': {'control': {'xtype': 'textfield'}},
    }
