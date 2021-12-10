from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

from kivy.properties import ObjectProperty, ListProperty, OptionProperty, StringProperty, NumericProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image, AsyncImage
from kivymd.uix.list import OneLineListItem
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color, Line
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView

from kivymd.uix.button import MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.progressbar import MDProgressBar

import datetime
import itertools
import sqlite3
import database
import app_kivy

# Set the screen size to a phone screen size
Window.size = (300, 500)

class SettingsDatabase:
    def __init__(self, path):
        self.path = path

    # Reads data from database
    def ReadDatabase(self):
        return sqlite3.connect(self.path, isolation_level=None)

    # Return all of of the content preferences
    def Read(self, tb):
        conn = self.ReadDatabase()
        cursorObj = conn.cursor()
        cursorObj.execute('SELECT * from "%s" WHERE id=1' %tb)
        return cursorObj.fetchall()

    def WriteNum(self, tb, row, new):
        conn = self.ReadDatabase()
        cursorObj = conn.cursor()
        cursorObj.execute('UPDATE "%s" SET "%s" = %s WHERE id=1' %(tb, row, new))

    def WriteText(self, tb, row, new):
        conn = self.ReadDatabase()
        cursorObj = conn.cursor()
        cursorObj.execute('UPDATE "%s" SET "%s" = "%s" WHERE id=1' %(tb, row, new))

    # Return all content names from a table
    def TableContents(self, table):
        conn = self.ReadDatabase()
        cursor = conn.execute("SELECT * FROM %s" % (table))
        names = list(map(lambda x: x[0], cursor.description))
        return names


pref = SettingsDatabase("liturgy.db")

def make_list(my_dict):
    content_list = []
    for c in my_dict:
        content_list = c
    return content_list


class BookmarksScreen(Screen):

    box = ScrollView()
    text = StringProperty('')
    grid = GridLayout()

    def on_enter(self):
        self.get_bookmarks()
        self.display_bookmarks()

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    def get_bookmarks(self):
        sql = 'SELECT * FROM bookmarks'
        db = self.connect()
        results = db.execute(sql)
        rows = list(results)
        return rows

    def display_bookmarks(self):

        stuff = self.get_bookmarks()
        self.grid = GridLayout(rows=(len(stuff)))

        for i in stuff:
            author = i[2].strip("(')',")
            text = i[3].strip("(')',")
            date = i[4].strip("(')',")
            card = BookmarkCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.grid.add_widget(card)
        self.box.add_widget(self.grid)

    def on_leave(self):
        self.box.clear_widgets()


class HighlightsScreen(Screen):

    hlight = ObjectProperty()

    def on_enter(self):
        self.display_highlights()

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    def get_highlights(self):
        sql = 'SELECT * FROM highlights'
        db = self.connect()
        results = db.execute(sql)
        rows = list(results)
        return rows

    def display_highlights(self):

        stuff = self.get_highlights()

        for i in stuff:
            author = i[2].strip("(')',")
            text = i[3].strip("(')',")
            date = i[4].strip("(')',")
            card = BookmarkCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.hlight.add_widget(card)


class HistoricalScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class InspirationScreen(Screen):
    pass

class PrayersTopicScreen(Screen):
    topic = ObjectProperty()
    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    def on_enter(self):
        self.create_topic_list()

    def create_topic_list(self):
        db = self.connect()
        sql = 'SELECT topic FROM prayers'
        sql2 = 'SELECT Topic FROM ausbund'
        results = db.execute(sql)
        rows = list(results)
        results2 = db.execute(sql2)
        rows2 = list(results2)
        combined = list([item for item in itertools.chain(rows, rows2)])
        combined.sort()

        for i in combined:
            s = str(i)
            tx = s.strip("(')',")
            button = TopicButton(text=tx)
            self.topic.add_widget(button)

    def on_leave(self):
        self.topic.clear_widgets()

class VerseButton(MDTextButton):
    dialog = None
    text = StringProperty('')
    date = datetime.datetime.today().strftime("%B %d, %Y")

    # function to show bookmark popup
    def bookmark_vs(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Bookmark this verse?",
                buttons=[
                    MDFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color,
                        on_release=self.bookmark
                    ),
                ],
                size_hint=[0.7, 0.6],
            )
        self.dialog.open()

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    # save results of bookmark popup
    def bookmark(self, obj):
        db = self.connect()
        sql = 'INSERT INTO bookmarks (user_id, type, author_ref, text, date) VALUES (1, "Scripture", "Psalm 22:1", "%s", "%s")'%(self.text, self.date)
        db.execute(sql)
        print(self.text)
        self.dialog.dismiss()

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

            self.vs = VerseButton(text=verse,
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
        sound = SoundLoader.load("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/Psalms audio/%s.mp3" % (self.ch))
        if sound:
            sound.play()

    def home(self, x):
        self.manager.current = 'home'

    def leftScreen(self, x):
        self.manager.transition.direction = 'right'
        self.manager.current = 'psalm'

    def rightScreen(self, x):
        self.manager.current = 'prayer'

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

            self.vs = VerseButton(text=verse,
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
        sound = SoundLoader.load("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/Psalms audio/%s.mp3" % (self.ch))
        if sound:
            sound.play()

    def home(self, x):
        self.manager.current = 'home'

    def leftScreen(self, x):
        self.manager.current = 'psalm'

    def rightScreen(self, x):
        self.manager.transition.direction = 'left'
        self.manager.current = 'prayer'


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
        sound = SoundLoader.load("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/Psalms audio/%s.mp3" % (self.ch))
        if sound:
            sound.play()

    def home(self, x):
        self.manager.current = 'home'

    def leftScreen(self, x):
        self.manager.transition.direction = 'right'
        self.manager.current = 'psalm'

    def rightScreen(self, x):
        self.manager.current = 'prayer'


class SettingsScreen(Screen):
    def notifications(self):
        my_popup(NotificationPopup(), "Notification Settings", 0.6)
    def back_button(self):
        MDApp.get_running_app().root.current = "home"


class SortedPrayersScreen(Screen):

    topic_prayers = ObjectProperty()
    topicname = StringProperty('')

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    # display prayers from a certain topic
    def display_prayers(self, topic=""):
        db = self.connect()
        sql = 'SELECT * FROM prayers WHERE topic LIKE "%s"' %(topic)
        sql2 = 'SELECT * FROM ausbund WHERE topic LIKE "%s"' %(topic)
        results = db.execute(sql)
        rows = list(results)
        results2 = db.execute(sql2)
        rows2 = list(results2)
        combined = list([item for item in itertools.chain(rows, rows2)])

        for i in combined:
            text = i[2].strip("(')',")
            author = i[3].strip("(')',")
            date = i[4].strip("(')',")
            card = PrayerCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.topic_prayers.add_widget(card)

    def on_enter(self):
        self.display_prayers(self.topicname)

    def on_leave(self):
        self.topic_prayers.clear_widgets()
    def back_button(self):
        MDApp.get_running_app().root.current = "topic"


class TextFormatting(Screen):
    content = pref.Read("style_preferences")
    content_list = make_list(content)
    def back_button(self):
        MDApp.get_running_app().root.current = "settings"
    def save(self):
        pref.WriteNum("style_preferences", "text_size", self.ids.size.value)
        pref.WriteText("style_preferences", "text_font", self.ids.font.text)
        MDApp.get_running_app().root.current = "settings"

class ThemeOptions(Screen):
    classic = 'normal'
    modern = 'normal'
    content = pref.Read("style_preferences")
    content_list = make_list(content)
    if content_list[1] == "classic":
        classic = 'down'
    else:
        modern = 'down'

    def save(self):
        if self.ids.classic.state == 'down':
            pref.WriteText("style_preferences", "theme", "classic")
        elif self.ids.classic.state == 'down':
            pref.WriteText("style_preferences", "theme", "modern")
        else:
            pref.WriteText("style_preferences", "theme", "classic")

        MDApp.get_running_app().root.current = "settings"

    def back_button(self):
        MDApp.get_running_app().root.current = "settings"

class ContentOptions(Screen):
    content = pref.Read("content_preferences")
    content_list = make_list(content)

    def save(self):
        pref.WriteNum("content_preferences", "prayers", 1 if self.ids.prayers.active else 0)
        pref.WriteNum("content_preferences", "psalms", 1 if self.ids.psalms.active else 0)
        pref.WriteNum("content_preferences", "scripture", 1 if self.ids.scripture.active else 0)
        pref.WriteNum("content_preferences", "hymns", 1 if self.ids.hymns.active else 0)
        pref.WriteNum("content_preferences", "patristics", 1 if self.ids.patristics.active else 0)
        pref.WriteNum("content_preferences", "commentary", 1 if self.ids.commentary.active else 0)
        pref.WriteNum("content_preferences", "anabaptist", 1 if self.ids.anabaptist.active else 0)
        pref.WriteNum("content_preferences", "biblical_languages", 1 if self.ids.languages.active else 0)
        pref.WriteNum("content_preferences", "audio", 1 if self.ids.audio.active else 0)
        MDApp.get_running_app().root.current = "settings"

    def back_button(self):
        MDApp.get_running_app().root.current = "settings"

class NotificationOptions(Screen):
    content = pref.Read("users")
    content_list = make_list(content)

    def save(self):
        pref.WriteNum("users", "notif", 1 if self.ids.checked.active else 0)
        pref.WriteText("users", "notif_type", self.ids.type.text)
        pref.WriteText("users", "notif_schedule", self.ids.schedule.text)
        MDApp.get_running_app().root.current = "settings"

    def back_button(self):
        MDApp.get_running_app().root.current = "settings"

class UserInfo(Screen):
    content = pref.Read("users")
    content_list = make_list(content)
    def back_button(self):
        MDApp.get_running_app().root.current = "settings"
    def save(self):
        pref.WriteText("users", "name", self.ids.name.text)
        pref.WriteText("users", "password", self.ids.password.text)
        pref.WriteText("users", "email", self.ids.email.text)
        MDApp.get_running_app().root.current = "settings"

# custom classes created
class ImageToggleButton(ToggleButtonBehavior,Image):
    """Image toggle button widget for kivy"""
    # toggle_type : what does change when state changes (color, source or both)
    toggle_type = OptionProperty('color',options=['color','source','both'])
    # color_down : color when state is down
    color_down = ListProperty([0.05,0.175,0.225,1])
    # color_normal : color when state is normal
    color_normal = ListProperty([1,1,1,1])
    # source_down : image source when state is down
    source_down = StringProperty('')
    # source_normal : image source when state is normal
    source_normal = StringProperty('')

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # force setting according to normal state
        self.on_state(None,'normal')

    def on_state(self,instance,state):
        if state=='down':
            if self.toggle_type == 'color' or self.toggle_type == 'both':
                self.color=self.color_down
            if self.toggle_type == 'source' or self.toggle_type == 'both':
                self.source=self.source_down
        else: # state=='normal'
            if self.toggle_type == 'source' or self.toggle_type == 'both':
                self.source=self.source_normal
            if self.toggle_type == 'color' or self.toggle_type == 'both':
                self.color=self.color_normal

    def on_source_down(self,instance,src):
        if self.state == 'down' and (self.toggle_type == 'source' or self.toggle_type == 'both'):
            self.source=self.source_down

    def on_source_normal(self,instance,src):
        if self.state == 'normal' and (self.toggle_type == 'source' or self.toggle_type == 'both'):
            self.source=self.source_normal

    def on_color_down(self,instance,clr):
        if self.state == 'down' and (self.toggle_type == 'color' or self.toggle_type == 'both'):
            self.color=self.color_down

    def on_color_normal(self,instance,clr):
        if self.state == 'normal' and (self.toggle_type == 'color' or self.toggle_type == 'both'):
            self.color=self.color_normal

    def on_toggle_type(self, instance, tp):
        if tp == 'source':
            # set color to white when toggle_type = 'source'
            self.color = [1,1,1,1]

def menu_callback(instance_menu, instance_menu_item):
    print(instance_menu, instance_menu_item)

# button that displays topics in database
class TopicButton(MDFlatButton):
    text = StringProperty('')
    topicname = StringProperty('')

    def get_topic(self, val):
        self.text = val
        SortedPrayersScreen.topicname = val
        MDApp.get_running_app().root.current = 'sorted_prayers'

# basic card to display prayers/scripture
class BookmarkCard(MDCard):

    card = ObjectProperty()
    title = StringProperty()
    text = StringProperty()
    date = StringProperty()

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    def remove_bookmark(self, tx):
        # db = self.connect()
        # sql = 'DELETE FROM bookmarks WHERE text=?'
        # db.execute(sql, (tx,))
        for card in self.children:
            if self.text == tx:
                self.parent.remove_widget(self)

class PrayerCard(MDCard):

    prayer_card = ObjectProperty()
    title = StringProperty()
    text = StringProperty()
    date = StringProperty()


class NotificationPopup(FloatLayout):
    content = pref.Read("users")
    content_list = make_list(content)

    def save(self):
        pref.WriteNum("users", "notif", 1 if self.ids.checked.active else 0)
        pref.WriteText("users", "notif_type", self.ids.type.text)
        pref.WriteText("users", "notif_schedule", self.ids.schedule.text)


# Opens the Popup window
def my_popup(popup_class, popup_title, y):
    show = popup_class
    popupWindow = Popup(title=popup_title, content=show, size_hint=(0.8, y))
    popupWindow.open()

class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty


# create screen mananger and add screens
screen_manager = ScreenManager()
screens = [
            HomeScreen(name="home"),
            SettingsScreen(name="settings"),
            BookmarksScreen(name="bookmarks"),
            HighlightsScreen(name="highlights"),
            PrayersTopicScreen(name="topic"),
            HistoricalScreen(name="events"),
            InspirationScreen(name="insp"),
            SortedPrayersScreen(name='sorted_prayers'),
            UserInfo(name="userinfo"),
            PreDevoScreen(name="pre_devo"),
            PsalmDevoScreen(name='psalm'),
            PrayerDevoScreen(name="prayer")
            ]

for screen in screens:
    screen_manager.add_widget(screen)

# Main app
class Liturgy(MDApp):

    # variable set for the notif popup
    dialog = None
    # get date and time
    date = datetime.datetime.today().strftime("%B %d, %Y")

    # run app with kv language and set color theme
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        return Builder.load_string(app_kivy.KV)

    def back_button(self):
        MDApp.get_running_app().root.current = "home"

    # function to show notification popup
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Would you like to allow notifications?",
                buttons=[
                    MDFlatButton(
                        text="No", text_color=self.theme_cls.primary_color,
                        on_release=self.disagreed
                    ),
                    MDFlatButton(
                        text="Yes", text_color=self.theme_cls.primary_color,
                        on_release=self.agreed
                    ),
                ],
                size_hint=[0.7, 0.6],
            )
        self.dialog.open()

    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db", isolation_level=None)
        db = conn.cursor()
        return db

    # store results of notification popup
    def disagreed(self, obj):
        db = self.connect()
        sql = 'UPDATE users SET notif=0 WHERE id=1'
        db.execute(sql)
        self.dialog.dismiss()
    def agreed(self, obj):
        db = self.connect()
        sql = 'UPDATE users SET notif=1 WHERE id=1'
        db.execute(sql)
        self.dialog.dismiss()

    # call notif popup when app opens
    # def on_start(self):
    #     self.show_alert_dialog()


Liturgy().run()
