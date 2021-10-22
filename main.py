from tobem.tobem import ToBemApp
from kivy.core.window import Window

# Animation to scroll Screen when text is obfscate by android keyboard
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'


ToBemApp().run()
