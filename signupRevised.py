from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import psycopg2
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'resizable', False)

class SignupScreen(Screen):
    pass

class SignupApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        screen_manager = ScreenManager()
        screen_manager.add_widget(SignupScreen())
        return screen_manager

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

if __name__ == "__main__":
    SignupApp().run()