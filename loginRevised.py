from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from DataInput import DataInput
import tkinter
from tkinter import filedialog
import geopandas as gpd

Config.set('graphics', 'resizable', False)

class LoginScreen(Screen):
    Builder.load_file('login.kv')
    pass

class LogInApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(DataInput(name='datainput'))
        return screen_manager
    
    def on_login(self):
        self.root.current = 'datainput'

    def btnfunc(self):
        tkinter.Tk().withdraw()
        user_input = filedialog.askopenfilename(filetypes=[("Shapefile", "*.shp"), ("All Files", "*.*")],)
        if user_input:
            df = gpd.read_file(user_input)
            print(df.head())


    

if __name__ == "__main__":
    LogInApp().run()