import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20,30,400, 500, 60, 560))
            Color(1,0,0,.5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            # Color(1,1,0,.5, mode='rgba')
            # self.rect = Rectangle(pos=(100,200), size=(50,50))

    def on_touch_down(self, touch): #override of the original function
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
    # def on_touch_up(self, touch):
    #     print("MU", touch)
        # self.btn.opacity = 1


class MyApp4(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp4().run()
