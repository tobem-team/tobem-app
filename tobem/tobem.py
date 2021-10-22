from kivy.lang import Builder
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd_extensions.sweetalert import SweetAlert


class Mood(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform != 'android':
            self.user_font_size = 100
        else:
            self.user_font_size = 150


class ToBem(MDFloatLayout):
    def message(self, mood):
        print(mood)
        SweetAlert().fire(
            text='Gostaria de dizer por que se sente assim?',
            input='Sinto que...',
        )


class ToBemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '700'

        return Builder.load_file('tobem/tobem.kv')
