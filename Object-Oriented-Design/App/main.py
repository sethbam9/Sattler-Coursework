import kivy
kivy.require('1.0.6')

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDTextButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.list import OneLineIconListItem

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.input.motionevent import MotionEvent

from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.core.text.markup import MarkupLabel
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Line
from kivy.core.audio import SoundLoader

from borders_click import BorderBehavior
import kv_file
import database
import time

"""
 https://www.youtube.com/channel/UCMMitT9SCbWlEcEkemnsxQg
 """

"""
Try writing a function that inputs the devo content based on the date. 
"""

# About the dimensions of a Google Pixel 2XL
Window.size = (300, 600)

class HomeScreen(Screen):
    def wait(self):
        global first_open
        # Displays the initial popup if this is the first opening of the app.
        if first_open:
            time.sleep(1)
            initial_popup(True)
            first_open = False
        else:
            return None

# Intro Screen before you begin the devo.
class PreDevoScreen(Screen):
    quote = """
           "Prayer is meeting with God. It's checking in, saying I am here, You are here. It is the present moment."
           ~ J.R. Rim
           """

class DevoTop(GridLayout):
    pass

class DevoBottom(GridLayout):
    pass

class DevoBar(MDProgressBar):
    pass

class DevoTitle(MDLabel):
    pass

# Devo screen with content from a Psalm.
class PsalmDevoScreen(Screen):
    def __init__(self, **kwargs):
        super(PsalmDevoScreen, self).__init__(**kwargs)
        # Chapter number
        self.ch = 16
        self.spacing = 30
        self.scroll_height = None

    def getVerses(self, chapter):
        # Creates a Scripture class from the database with book "Psalm"
        psalm = database.Scripture('t_kjv', 'Ps', chapter)
        # Create a list with all the verses in the chapter.
        self.verses = psalm.getVerses()
        # Create the view containers;
        self.scroll = ScrollView(
            do_scroll_y=True,
            size_hint=(0.9, 0.7),
            pos_hint={'center_x': 0.5, 'top': 0.86})
        self.grid = GridLayout(
            rows=len(self.verses),
            size_hint_y=len(self.verses)/self.getHeight(self.verses),
            spacing=(0, self.spacing))

        # Create a label for each verse in the chapter.
        for verse in self.verses:

            self.vs = MDLabel(text=verse,
                pos_hint={'center_x': 0.5})

            self.grid.add_widget(self.vs) # The box inherits the verses.

        # Place the grid of verse rows into the scrollview.
        self.scroll.add_widget(self.grid)
        # Deletes the scrollview from the PsalmScreen when you leave.
        for widget in list(self.children):
            if isinstance(widget, ScrollView): self.remove_widget(widget)
            if isinstance(widget, MDLabel): self.remove_widget(widget)


        self.title = DevoTitle(text= "Psalm %s" % (self.ch))
        self.devo_top = DevoTop()
        self.devo_top.ids.homebtn.bind(on_press=self.home)
        self.devo_top.ids.textbtn.bind(on_press=self.changePsalm)
        self.devo_bottom = DevoBottom()
        self.devo_bottom.ids.leftbtn.bind(on_press=self.leftScreen)
        # self.devo_bottom.ids.bookmarkbtn.bind(on_press=self.playAudio)
        self.devo_bottom.ids.audiobtn.bind(on_press=self.playAudio)
        self.devo_bottom.ids.rightbtn.bind(on_press=self.rightScreen)
        self.bar = DevoBar()
        self.add_widget(self.devo_top)
        self.add_widget(self.scroll)
        self.add_widget(self.title)
        self.add_widget(self.devo_bottom)
        self.add_widget(self.bar)

    def changePsalm(self, x):
        self.ch = 119
        return self.getVerses(self.ch)

    def getHeight(self, verses):
        l = len(verses)
        if l > 6:
            self.scroll_height = 6
        elif l > 1:
            self.scroll_height = l / 1.2
        return self.scroll_height

    def playAudio(self, x):
        sound = SoundLoader.load(r"App\Psalms audio\%s.mp3" % (self.ch))
        if sound:
            sound.play()

    def home(self, x):
        self.manager.current = 'home'

    def leftScreen(self, x):
        self.manager.current = 'psalm'

    def rightScreen(self, x):
        self.manager.transition.direction = 'left'
        self.manager.current = 'prayer'


class PrayerDevoScreen(Screen):
    def __init__(self, **kwargs):
        super(PrayerDevoScreen, self).__init__(**kwargs)
        # Chapter number
        self.ch = 22
        self.spacing = 30
        self.scroll_height = None

    def getVerses(self, chapter):
        # Creates a Scripture class from the database with book "Psalm"
        psalm = database.Scripture('t_kjv', 'Ps', chapter)
        # Create a list with all the verses in the chapter.
        self.verses = psalm.getVerses()
        # Create the view containers;
        self.scroll = ScrollView(
            do_scroll_y=True,
            size_hint=(0.9, 0.7),
            pos_hint={'center_x': 0.5, 'top': 0.86})
        self.grid = GridLayout(
            rows=len(self.verses),
            size_hint_y=len(self.verses)/self.getHeight(self.verses),
            spacing=(0, self.spacing))

        # Create a label for each verse in the chapter.
        for verse in self.verses:

            self.vs = MDLabel(text=verse,
                pos_hint={'center_x': 0.5})

            self.grid.add_widget(self.vs) # The box inherits the verses.

        # Place the grid of verse rows into the scrollview.
        self.scroll.add_widget(self.grid)
        # Deletes the scrollview from the PsalmScreen when you leave.
        for widget in list(self.children):
            if isinstance(widget, ScrollView): self.remove_widget(widget)
            if isinstance(widget, MDLabel): self.remove_widget(widget)


        self.title = DevoTitle(text= "Psalm %s" % (self.ch))
        self.devo_top = DevoTop()
        self.devo_top.ids.homebtn.bind(on_press=self.home)
        self.devo_top.ids.textbtn.bind(on_press=self.changePsalm)
        self.devo_bottom = DevoBottom()
        self.devo_bottom.ids.leftbtn.bind(on_press=self.leftScreen)
        # self.devo_bottom.ids.bookmarkbtn.bind(on_press=self.playAudio)
        self.devo_bottom.ids.audiobtn.bind(on_press=self.playAudio)
        self.devo_bottom.ids.rightbtn.bind(on_press=self.rightScreen)
        self.bar = DevoBar()
        self.add_widget(self.devo_top)
        self.add_widget(self.scroll)
        self.add_widget(self.title)
        self.add_widget(self.devo_bottom)
        self.add_widget(self.bar)

    def changePsalm(self, x):
        self.ch = 119
        return self.getVerses(self.ch)

    def getHeight(self, verses):
        l = len(verses)
        if l > 6:
            self.scroll_height = 6
        elif l > 1:
            self.scroll_height = l / 1.2
        return self.scroll_height

    def playAudio(self, x):
        sound = SoundLoader.load(r"App\Psalms audio\%s.mp3" % (self.ch))
        if sound:
            sound.play()

    def home(self, x):
        self.manager.current = 'home'

    def leftScreen(self, x):
        self.manager.transition.direction = 'right'
        self.manager.current = 'psalm'

    def rightScreen(self, x):
        self.manager.current = 'prayer'

class ScriptureScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

sm = ScreenManager()

screens = [
            HomeScreen(name="home"),
            PreDevoScreen(name="pre_devo"),
            PsalmDevoScreen(name='psalm'),
            PrayerDevoScreen(name="prayer"),
            MenuScreen(name="menu")
            ]

for screen in screens:
    sm.add_widget(screen)

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(kv_file.screen_helper)
        return screen

DemoApp().run()


















""" EXTRA

COUNT children
    self.add_widget(MDRectangleFlatButton(
        on_press=self.widg))
    def widg(self, x):
        for child in list(self.children):
            print(child)
            for c in child.children:
                print("    ", c)
                for a in c.children:
                    print("          ", a)

# Popup window with sign up and notification options.
class InitialPopup(FloatLayout):
    pass

# Opens the Popup window
def initial_popup(bool):
    show = InitialPopup()
    popupWindow = Popup(title="Welcome to Liturgy", content=show, size_hint=(0.8, 0.8))
    # Checks if the App has been opened before.
    if bool == True:
        popupWindow.open()
    if bool == False:
        popupWindow.dismiss()

# Screen to give the feel of a phone background when you first open the app.
class PhoneScreen(Screen):
    pass

# The boolean used for the initial popup.
first_open = False

"""
