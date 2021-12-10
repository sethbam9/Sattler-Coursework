import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel, MDIcon
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivy.animation import Animation

from kivy.event import EventDispatcher


class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)
    def do_something(self, value):
        # when do_something is called, the 'on_test' event will be
        # dispatched with the value
        self.dispatch('on_test', value)
    def on_test(self, *args):
        print ("I am dispatched", args)

def my_callback(dt):
    print ('My callback is called', dt)

class MyGrid(FloatLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.event = None
        self.p = False
        self.ev = MyEventDispatcher()
        self.ev.bind(on_test=self.my_callback)
        self.ev.do_something('test')
        self.anim = (Animation(pos_hint={'x':.2,'y':.3})
            + Animation(size_hint=(.3, .2), t='in_quad'))
        self.add_widget(Button(text="Callback",
            size_hint=(.1,.1), pos=(400,100), on_press=self.pressed))
        self.add_widget(Button(text="MyEvent",
            size_hint=(.1,.1), pos=(50,50), on_press=self.my_callback))
        self.add_widget(Button(text="ANIMATE",
            size_hint=(.1,.1), pos_hint={'x':.5,'y':.5}, on_press=self.animate))


    def go(self):
        if not self.p:
            self.event = Clock.schedule_interval(my_callback, 1)
            self.p=True
        else:
            self.event.cancel()
            self.p=False

    def pressed(self, instance):
        self.go()

    def my_callback(self, value, *args):
        print ("Hello, I got an event!", args)

    def animate(self, widget):
        self.anim.start(widget)

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):
    pressed = ListProperty([0, 0])
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))

class MyApp(MDApp):

    def build(self):
        return RootWidget()
        # return MyGrid()

if __name__ == '__main__':
    MyApp().run()

"""
Often times you will want to restrict the area on the screen that a widget
watches for touches You can use a widget’s collide_point() method to achieve
this. You simply  pass it the touch’s position and it returns True if the
touch is within the ‘watched area’ or False otherwise
"""
