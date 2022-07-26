from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class HomePage(MDScreen):
    'Home Page'


class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        Builder.load_file('neww.kv')
        return HomePage()


MainApp().run()