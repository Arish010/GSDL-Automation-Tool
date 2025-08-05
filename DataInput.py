from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import tkinter
from tkinter import filedialog
import geopandas as gpd
from kivy.config import Config

Config.set('graphics', 'resizable', True)

class DataInput(Screen):
    Builder.load_file('DataInput.kv')
    pass

class DataInputApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return DataInput(name='datainput')
    

    def btnfunc(self):
        tkinter.Tk().withdraw()
        user_input = filedialog.askopenfilename(filetypes=[("Shapefile", "*.shp"), ("All Files", "*.*")],)
        if user_input:
            df = gpd.read_file(user_input)
            print(df.head())

    def onstart(self):
        self.root.current = 'adminpanel'


if __name__ == "__main__":
    DataInputApp().run()


