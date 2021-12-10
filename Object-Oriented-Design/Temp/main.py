import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button


def my_callback(value, *args):
    print ("Hello, I got an event!", args)

class MyW(Widget):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.register_event_type('on_swipe')

    def on_swipe(self, value):
        self.ids.label1.text = 'Hello1'

    def do_something(self, value):
        if self.ids.button1.text != 'Hello':
            self.dispatch('on_swipe', value)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.ids.button1.text = 'xxx'
        if touch.is_triple_tap:
            self.ids.button1.text = 'Hello'
        self.bind(on_swipe=my_callback)
        self.do_something('test')

kv = """
<MyW>:
  Button:
    id: button1
    text: 'Hello'
  Label:
    id: label1
    pos: 200,200
    text: ''
"""
class e5App(App):
    def build(self):
        b = Builder.load_string(kv)
        return b

if __name__ == '__main__':
    e5App().run()
