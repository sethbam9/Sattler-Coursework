# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import Screen
# from kivy.uix.label import Label
#
#
# def convert_data(data):
#     l = []
#     for item in data:
#         for key, value in item.items():
#             l.append({'text': key, 'value': value})
#     return l
#
# class test():
#
#     def demo(self):
#         print('Demo')
#
# class MyLabel(Label):
#     double_tap_time = 1
#     def on_touch_down(self, touch):
#         if touch.is_double_tap:
#             demo()
#
# class Invoice(Screen):
#     def abc(self):
#         arr = ({'Item1': ''},{'Item2': 1000})
#
#         self.rv.data = convert_data(arr)
#
# class MyApp(App):
#     def build(self):
#         return Builder.load_file('test.kv')
#
# if __name__ == '__main__':
#     MyApp().run()


from kivy.app import App

from kivy.uix.label import Label


class DoubleClickableLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.register_event_type('on_double_press')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return Label.on_touch_down(self, touch)

    def on_double_press(self, *args):
        pass


class MyApp(App):
    def build(self):
        label = DoubleClickableLabel(text='Hello world', on_double_press=self.callback)
        return label

    def callback(self, *args):
        print("double clicked", args[0])


if __name__ == '__main__':
    MyApp().run()
