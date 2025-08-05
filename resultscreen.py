from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


Config.set('graphics', 'resizable', False)


class ResultScreen(Screen):
    Builder.load_file('resultscreen.kv')
    pass

class ResultScreenApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        screen_manager = ScreenManager()
        screen_manager.add_widget(ResultScreen(name='resultscreen'))
        return screen_manager


if __name__ == '__main__':
    ResultScreenApp().run()