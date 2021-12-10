import gesture_box as gesture
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# https://stackoverflow.com/questions/30934445/kivy-swiping-carousel-screenmanager

class Runner(gesture.GestureBox):
    pass

class MainApp(App):
    def build(self):
        return Runner()

if __name__ == '__main__':
    app = MainApp()
    app.run()
