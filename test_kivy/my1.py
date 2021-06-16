
import kivy

from kivy.app import App
from kivy.uix.button import Button


class Myapp:
    pass


class Myapp(App):
    def build(self):
        return Button(text = 'Hello World!')
    if__name__ = '__main':
    Myapp().run()
