import kivy

kivy.require('1.0.6')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class RootScreen(ScreenManager):
    pass

class TitleScreen(Screen):
    pass

class CharacterCreationScreen(Screen):
    pass


class GameApp(App):

    def build(self):
        return RootScreen()


if __name__ == '__main__':
    GameApp().run()
