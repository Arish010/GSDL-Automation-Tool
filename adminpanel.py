from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

Config.set('graphics', 'resizable', False)


class AdminScreen(Screen):
    Builder.load_file('adminpanel.kv')
    pass

class AdminPanelApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager = ScreenManager()
        screen_manager.add_widget(AdminScreen(name='adminpanel'))
        return screen_manager
    

if __name__ == "__main__":
    AdminPanelApp().run()