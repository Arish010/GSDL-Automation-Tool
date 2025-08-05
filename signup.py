from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import psycopg2
<<<<<<< HEAD
from kivy.uix.boxlayout import BoxLayout

=======
from login import LoginScreen
from DataInput import DataInput
import tkinter
from adminpanel import AdminScreen
from resultscreen import ResultScreen
from finalscreen import FinalScreen
from tkinter import filedialog
import geopandas as gpd
>>>>>>> eedc1bc0d6d62714bb7463f5b089d93a1ce570b3
Config.set('graphics', 'resizable', False)

class SignupScreen(Screen):
    pass

class SignupApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager = ScreenManager()
<<<<<<< HEAD
        screen_manager.add_widget(SignupScreen())
        return screen_manager
=======
        screen_manager.add_widget(SignUpScreen())
        screen_manager.add_widget(LoginScreen(name = 'login'))
        screen_manager.add_widget(DataInput(name='datainput'))
        screen_manager.add_widget(AdminScreen(name='adminpanel'))
        screen_manager.add_widget(ResultScreen(name='resultscreen'))
        screen_manager.add_widget(FinalScreen(name='finalscreen'))
        return screen_manager
    
    
    def on_signup(self):
      username = self.root.get_screen("signup_screen").ids.username_field.text
      email = self.root.get_screen("signup_screen").ids.email_field.text
      password = self.root.get_screen("signup_screen").ids.password_field.text
      print(username)
      print(email)
      print(password)
      try:
          conn = psycopg2.connect(database="datamapper",user="postgres",password="root",host="localhost",port="5432")
          print("Connection Established")
          cur = conn.cursor()
          cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
          conn.commit()
          conn.close()
      except:
          print("Exception Occured")
      self.root.current = 'login'
>>>>>>> eedc1bc0d6d62714bb7463f5b089d93a1ce570b3

    def printtoconsole(self):
        username = self.root.get_screen("signup_screen").ids.username_field.text
        password = self.root.get_screen("signup_screen").ids.password_field.text
        repeatpassword = self.root.get_screen("signup_screen").ids.repeat_password_field.text
        print(username)
        print(password)
        print(repeatpassword)
        try:
            conn = psycopg2.connect(database="datamapper", user="postgres", password="root", host="localhost", port="5432")
            print("connection established")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            conn.close()
        
        except:
            print("exception occured")
"""
    def signup(self):
        conn = psycopg2.connect(database="datamapper", user="postgres", password="root", host="localhost", port="5432")
        cur = conn.cursor()
        username = self.root.get_screen("signup_screen").ids.username_field.text
        email = self.root.get_screen("signup_screen").ids.email_field.text
        password = self.root.get_screen("signup_screen").ids.password_field.text
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()
        conn.close()
"""

    def onstart(self):
        self.root.current = 'adminpanel'

    def onadmin(self):
        self.root.current = 'resultscreen'

    def onfinal(self):
        self.root.current = 'finalscreen'

if __name__ == "__main__":
    SignupApp().run()