from kivymd.app import MDApp 
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

Config.set('graphics', 'resizable', False)


class FinalScreen(Screen):
    Builder.load_file('finalscreen.kv')
    pass

class FinalScreenApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        screen_manager = ScreenManager()
        screen_manager.add_widget(FinalScreen(name='finalscreen'))
        return screen_manager


if __name__ == '__main__':
    FinalScreenApp().run()