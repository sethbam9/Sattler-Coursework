from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.graphics import Line, Color

Builder.load_string("""
<DemoRootWidget>:
    BorderLabel:
        text: 'Label1'
    BorderLabel:
        text: 'Label2'
    BorderButton:
        text: 'Button1'

<BorderButton@Button+BorderBehavior>:
    size_hint: None, None
    pos: (100,100)
    width: 200
    height: 100
    borders: 2, 'solid', (1,1,1,1.)

<BorderLabel@Label+BorderBehavior>:
    size_hint: None, None
    pos: (100,100)
    width: 200
    height: 100
    borders: 5, 'solid', (1,0,0,1)
    canvas.before:
        Color:
            rgba: 0,0,1,1.
        Rectangle:
            pos: self.pos
            size: self.size
""")


class BorderBehavior(Widget):
    borders = ObjectProperty(None)
    border_origin_x = NumericProperty(0.)
    border_origin_y = NumericProperty(0.)
    border_origin = ReferenceListProperty(border_origin_x, border_origin_y)

    left_border_points = []
    top_border_points = []
    right_border_points = []
    bottom_border_points = []

    CAP = 'square'
    JOINT = 'none'

    dash_styles = {
        'dashed':
        {
            'dash_length': 10,
            'dash_offset': 5
        },
        'dotted':
        {
            'dash_length': 1,
            'dash_offset': 1
        },
        'solid':
        {
            'dash_length': 1,
            'dash_offset': 0
        }
    }

    def draw_border(self):
        line_kwargs = {
            'points': [],
            'width': self.line_width,
            'cap': self.CAP,
            'joint': self.JOINT,
            'dash_length': self.cur_dash_style['dash_length'],
            'dash_offset': self.cur_dash_style['dash_offset']
        }

        with self.canvas.after:
            self.border_color = Color(*self.line_color)
            # left border
            self.border_left = Line(**line_kwargs)

            # top border
            self.border_top = Line(**line_kwargs)

            # right border
            self.border_right = Line(**line_kwargs)

            # bottom border
            self.border_bottom = Line(**line_kwargs)

    def update_borders(self):
        if hasattr(self, 'border_left'):
            # test for one border is enough so we know that the borders are
            # already drawn
            width = self.line_width
            dbl_width = 2 * width

            self.border_left.points = [
                self.border_origin_x,
                self.border_origin_y,
                self.border_origin_x,
                self.border_origin_y +
                self.size[1] - dbl_width
            ]

            self.border_top.points = [
                self.border_origin_x,
                self.border_origin_y + self.size[1] - dbl_width,
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y + self.size[1] - dbl_width
            ]

            self.border_right.points = [
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y + self.size[1] - dbl_width,
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y
            ]

            self.border_bottom.points = [
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y,
                self.border_origin_x,
                self.border_origin_y
            ]

    def set_border_origin(self):
        self.border_origin_x = self.pos[0] + self.line_width
        self.border_origin_y = self.pos[1] + self.line_width

    def on_border_origin(self, instance, value):
        print (self.border_origin, "border origin")
        self.update_borders()

    def on_size(self, instance, value):
        # not sure if it's really needed, but if size is changed
        # programatically the border have to be updated
        # --> needs further testing
        if hasattr(self, 'line_width'):
            self.set_border_origin()
            self.pos = self.border_origin

    def on_pos(self, instance, value):
        # print instance, value, "pos changed"
        if hasattr(self, 'line_width'):
            self.set_border_origin()

    def on_borders(self, instance, value):
        self.line_width, self.line_style, self.line_color = value
        self.cur_dash_style = self.dash_styles[self.line_style]
        # print self.cur_dash_style, "dash_style selected"
        self.set_border_origin()
        self.draw_border()

    # touch events for testing
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
                touch.grab(self)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            # I received my grabbed touch
            print (touch)
            self.pos = (touch.x, touch.y)
        # else:
        #     print "only touched"
        #     # it's a normal touch

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # I receive my grabbed touch, I must ungrab it!
            touch.ungrab(self)
        # else:
        #     # it's a normal touch
        #     print "normal touch up"
        #     pass


class DemoRootWidget(BoxLayout):
    pass


if __name__ == '__main__':
    class DemoBorderApp(App):
        def build(self):
            return DemoRootWidget()


    DemoBorderApp().run()
