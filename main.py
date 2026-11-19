from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Устанавливаем размер окна как у смартфона (для тестов на ПК)
Window.size = (360, 640)
# Основной фон приложения — светло-серый
Window.clearcolor = (0.9, 0.9, 0.9, 1)

# База данных с рецептами для общежития
RECIPES = {
    "Гречка с сосисками": {
        "tools": "• Кастрюля\n• Сковорода (по желанию)\n• Вилка и нож\n• Тарелка",
        "ingredients": "• Гречка — 1 стакан\n• Вода — 2 стакана\n• Сосиски — 2-3 шт.\n• Соль — 0.5 ч. ложки\n• Сливочное или растительное масло",
        "steps": (
            "1. Промой гречку в холодной воде пару раз, чтобы вода стала прозрачной.\n\n"
            "2. Засыпь гречку в кастрюлю, залей 2 стаканами воды и добавь соль.\n\n"
            "3. Поставь на сильный огонь. Когда закипит — убавь огонь на минимум, накрой крышкой и вари 15–20 минут (пока вода не выкипит).\n\n"
            "4. Очисти сосиски от пленки. За 5 минут до готовности гречки положи их прямо сверху в кастрюлю (или обжарь на сковороде с маслом 3-4 минуты).\n\n"
            "5. Добавь в гречку кусочек масла, перемешай. Блюдо готово!"
        )
    },
    "Макароны": {
        "tools": "• Кастрюля\n• Дуршлаг (или крышка от кастрюли)\n• Ложка или вилка",
        "ingredients": "• Макароны — 150-200 г (примерно 1.5 стакана)\n• Вода — 1.5 литра\n• Соль — 0.5 ч. ложки\n• Масло, сыр или кетчуп — по вкусу",
        "steps": (
            "1. Налей в кастрюлю воду (примерно 2/3 объема) и поставь на сильный огонь.\n\n"
            "2. Когда вода закипит, брось туда соль и перемешай.\n\n"
            "3. Засыпь макароны в кипящую воду и сразу перемешай, чтобы они не слиплись.\n\n"
            "4. Вари на среднем огне 7–10 минут (точное время смотри на упаковке), периодически помешивая.\n\n"
            "5. Откинь макароны на дуршлаг (или аккуратно слей воду, придерживая крышку).\n\n"
            "6. Переложи в тарелку, добавь масло, тертый сыр или соус."
        )
    },
    "Жареные пельмени": {
        "tools": "• Сковорода\n• Лопатка для перемешивания\n• Крышка для сковороды",
        "ingredients": "• Замороженные пельмени — 15-20 шт.\n• Растительное масло — 2 ст. ложки\n• Соль, перец, специи — по вкусу\n• Вода — 50 мл (четверть стакана)\n• Сметана или майонез для подачи",
        "steps": (
            "1. Поставь сковороду на средний огонь, налей масло и дай ему разогреться 1 минуту.\n\n"
            "2. Выложи замороженные пельмени в один слой (размораживать их НЕ нужно!).\n\n"
            "3. Обжаривай по 3–4 минуты с каждой стороны до появления золотистой корочки.\n\n"
            "4. Посоли, поперчи, влей в сковороду немного воды и СРАЗУ накрой крышкой (будет сильно шипеть).\n\n"
            "5. Убавь огонь на минимум и туши под крышкой еще 5 минут, чтобы тесто внутри точно пропеклось."
        )
    },
    "Рис с жареной колбасой": {
        "tools": "• Кастрюля\n• Сковорода\n• Нож и разделочная доска\n• Лопатка",
        "ingredients": "• Рис — 1 стакан\n• Вода — 2 стакана\n• Вареная или копченая колбаса — 150 г\n• Растительное масло — 2 ст. ложки\n• Соль — по вкусу",
        "steps": (
            "1. Тщательно промой рис в холодной воде (4-5 раз, пока вода не станет совсем прозрачной).\n\n"
            "2. Залей рис в кастрюле 2 стаканами воды, посоли и поставь на огонь. После закипания убавь огонь, накрой крышкой и вари 15 минут. Не открывай крышку!\n\n"
            "3. Пока варится рис, нарежь колбасу кубиками или соломкой.\n\n"
            "4. Разогрей масло на сковороде и обжарь колбасу 5 минут до румяной корочки.\n\n"
            "5. Высыпь готовый рис в сковороду к колбасе, перемешай и прогрей всё вместе еще 2 минуты."
        )
    },
    "Пюре с котлетами": {
        "tools": "• Кастрюля и сковорода\n• Овощечистка или нож\n• Толкушка для пюре (или обычная вилка/кружка)\n• Лопатка",
        "ingredients": "• Картофель — 4-5 средних клубней\n• Полуфабрикатные котлеты — 2-3 шт.\n• Сливочное масло — 30 г\n• Молоко (или вода от варки) — 50 мл\n• Растительное масло и соль",
        "steps": (
            "1. Почисти картошку, разрежь на 4 части (так быстрее сварится), залей водой в кастрюле, посоли и поставь вариться на 20 минут.\n\n"
            "2. Параллельно разогрей сковороду с растительным маслом. Выложи котлеты и жарь на среднем огне по 5–7 минут с каждой стороны до корочки. Затем убавь огонь, накрой крышкой и подержи еще 5 минут.\n\n"
            "3. Проверь картошку ножом: если легко протыкается — она готова. Слей всю воду.\n\n"
            "4. Добавь в горячую картошку сливочное масло и молоко (или немного бульона), разомни толкушкой до состояния пюре.\n\n"
            "5. Выложи пюре на тарелку, рядом положи горячие котлеты."
        )
    }
}


# Класс для создания черных прямоугольных кнопок со скругленными углами
class RoundedBlackButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (0.85, 0.85, 0.85, 1)  # Светло-серый цвет текста на кнопке
        self.bold = True
        self.font_size = '15sp'
        self.halign = 'center'
        self.valign = 'middle'
        self.bind(size=self._update_text_size)

        # Рисуем черный прямоугольник со скругленными углами
        with self.canvas.before:
            Color(0.15, 0.15, 0.15, 1)  # Темно-серый / черный цвет кнопки
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[18])

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_text_size(self, instance, value):
        self.text_size = (instance.width - 20, None)


# Главный экран (Меню выбора блюд)
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title = Label(
            text="ОБЩАГА-ШЕФ\nВыбери блюдо:",
            font_size='24sp',
            bold=True,
            color=(0.15, 0.15, 0.15, 1),
            halign='center',
            size_hint_y=0.22
        )
        main_layout.add_widget(title)

        center_wrapper = BoxLayout(orientation='vertical', size_hint_y=0.78)
        
        grid = GridLayout(
            cols=2,
            spacing=15,
            size_hint=(1, None),
            height=380
        )

        for dish_name in RECIPES.keys():
            btn = RoundedBlackButton(text=dish_name)
            btn.bind(on_release=self.open_recipe)
            grid.add_widget(btn)

        center_wrapper.add_widget(Label(size_hint_y=0.1))
        center_wrapper.add_widget(grid)
        center_wrapper.add_widget(Label(size_hint_y=0.2))

        main_layout.add_widget(center_wrapper)
        self.add_widget(main_layout)

    def open_recipe(self, instance):
        recipe_screen = self.manager.get_screen('recipe')
        recipe_screen.load_dish(instance.text)
        self.manager.current = 'recipe'


# Второй экран (Подробный рецепт)
class RecipeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.dish_title = Label(
            text="",
            font_size='22sp',
            bold=True,
            color=(0.15, 0.15, 0.15, 1),
            size_hint_y=None,
            height=50,
            halign='center'
        )
        self.layout.add_widget(self.dish_title)

        scroll = ScrollView(size_hint=(1, 1))
        
        self.recipe_content = Label(
            text="",
            font_size='16sp',
            color=(0.15, 0.15, 0.15, 1),
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.recipe_content.bind(
            width=lambda *x: setattr(self.recipe_content, 'text_size', (self.recipe_content.width, None)),
            texture_size=lambda *x: setattr(self.recipe_content, 'height', self.recipe_content.texture_size[1])
        )

        scroll.add_widget(self.recipe_content)
        self.layout.add_widget(scroll)

        back_btn = RoundedBlackButton(
            text="← Назад к выбору блюд",
            size_hint=(1, None),
            height=55
        )
        back_btn.bind(on_release=self.go_back)
        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def load_dish(self, dish_name):
        data = RECIPES[dish_name]
        self.dish_title.text = dish_name.upper()
        
        full_text = (
            f"[b]ЧТО ПОНАДОБИТСЯ (ИНСТРУМЕНТЫ):[/b]\n{data['tools']}\n\n"
            f"[b]ПРОДУКТЫ (МАТЕРИАЛЫ):[/b]\n{data['ingredients']}\n\n"
            f"[b]ПОШАГОВОЕ ПРИГОТОВЛЕНИЕ:[/b]\n{data['steps']}"
        )
        self.recipe_content.text = full_text

    def go_back(self, instance):
        self.manager.current = 'menu'


# Главный класс запуска приложения
class DormCookApp(App):
    def build(self):
        self.title = "Общага-Шеф"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(RecipeScreen(name='recipe'))
        return sm


if __name__ == '__main__':
    DormCookApp().run()
