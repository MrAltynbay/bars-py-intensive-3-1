from m3_ext.ui.containers import ExtFieldSet, ExtForm, ExtToolBar
from m3_ext.ui.controls import ExtButton
from m3_ext.ui.fields import ExtStringField, ExtHiddenField
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtWindow, ExtEditWindow


class MasterPanel(ExtFieldSet):
    """
    Пример простой панели с кнопками и обработчиками
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Привет, Мир!'
        self.height = 200
        self.items.extend([
            ExtButton(
                text='Нажми меня',
                handler='''
                    function(){
                        const parent = this.ownerCt;
                        const strField = parent.findByType('textfield')[0];
                        sendRequest("/demo/win1", null, {"str_field": strField.getValue()});
                    }''',
            ),
            ExtStringField(
                label='Поле ввода',
                name='str_field',
            ),
            ExtButton(
                text='Grid',
                handler='function(){ sendRequest("/demo/gridwin");}',
            ),
        ])


class MasterWindow(ExtWindow):
    """
    Пример окна
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Вот и я!'
        self.str_field = ExtStringField(
            label='Поле ввода',
            name='str_field',
        )
        self.items.extend([
            self.str_field
        ])


class GridWindow(ExtWindow):
    """
    Пример окна с гридом
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Grid'
        self.layout = 'border'
        self.grid = ExtObjectGrid(
            region='center'
        )
        self.grid.plugins.append('new Ext.ux.grid.GridHeaderFilters()')
        self.grid.add_column(
            data_index='first_name',
            header='Имя',
            sortable=True,
        )
        self.grid.add_column(
            data_index='last_name',
            header='Фамилия',
            sortable=True,
        )
        self.grid.add_column(
            data_index='username',
            header='Ник',
            sortable=True,
        )
        self.grid.add_column(
            data_index='email',
            header='Почта',
            sortable=True,
        )
        self.items.extend([
            self.grid
        ])


class CreateUserWindow(ExtEditWindow):
    """
    Окно создания
    """
    def __init__(self, *args, create_new=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Создание юзера'
        self.id_field = ExtHiddenField(
            name='id',
        )
        self.last_name_field = ExtStringField(
            label='Фамилия',
            name='last_name',
        )
        self.first_name_field = ExtStringField(
            label='Имя',
            name='first_name',
        )
        self.password_field = ExtStringField(
            label='Пароль',
            name='password',
        )
        self.username_field = ExtStringField(
            label='Ник',
            name='username',
        )
        self.email_field = ExtStringField(
            label='Почта',
            name='email',
        )
        self.form = ExtForm()
        self.button_align = self.align_left
        self.save_button = ExtButton(
            text=u'Сохранить',
            handler='submitForm')
        self.cancel_button = ExtButton(
            text=u'Закрыть',
            handler='function(){win.close();}')

        self.footer_bar = ExtToolBar()
        self.footer_bar.items.extend([
            self.save_button,
            self.cancel_button,
        ])

        self.form.items.extend([
            self.id_field,
            self.first_name_field,
            self.last_name_field,
            self.password_field,
            self.username_field,
            self.email_field,
        ])

        self.init_component(*args, **kwargs)


class EditUserWindow(ExtEditWindow):
    """
    Окно редактирования
    """
    def __init__(self, *args, create_new=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Редактирование юзера'
        self.id_field = ExtHiddenField(
            name='id',
        )
        self.last_name_field = ExtStringField(
            label='Фамилия',
            name='last_name',
        )
        self.name_field = ExtStringField(
            label='Имя',
            name='first_name',
        )
        self.password_field = ExtStringField(
            label='Пароль',
            name='password',
        )
        self.username_field = ExtStringField(
            label='Ник',
            name='username',
        )
        self.email_field = ExtStringField(
            label='Почта',
            name='email',
        )
        self.form = ExtForm()
        self.button_align = self.align_left
        self.save_button = ExtButton(
            text=u'Сохранить',
            handler='submitForm')
        self.cancel_button = ExtButton(
            text=u'Закрыть',
            handler='function(){win.close();}')

        self.footer_bar = ExtToolBar()
        self.footer_bar.items.extend([
            self.save_button,
            self.cancel_button,
        ])

        self.form.items.extend([
            self.id_field,
            self.name_field,
            self.last_name_field,
            self.password_field,
            self.username_field,
            self.email_field,
        ])

        self.init_component(*args, **kwargs)
