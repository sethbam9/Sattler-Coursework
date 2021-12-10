from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.image import Image, AsyncImage
from kivymd.uix.button import MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
import datetime
import sqlite3

import app_kivy

# Set the screen size to a phone screen size
Window.size = (300, 500)

class Scripture:
    # get kjv with book number and chapter number and format to list
    def get_scripture(b="",c=""):
        
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db")
        db = conn.cursor()
        sql = 'SELECT * FROM t_kjv WHERE b="%s" AND c="%s"' %(b,c)
        results = db.execute(sql)    
        rows = list(results)
        return rows
    
class Prayers:
    # connect with database
    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db")
        db = conn.cursor()
        return db
     # get all prayers of a certain topic from prayer table   
    def get_topic_prayers(self,topic=""):
        db = self.connect()
        sql = 'SELECT * FROM prayers WHERE topic LIKE "%s"' %(topic)
        results = db.execute(sql)    
        rows = list(results)
        return rows
    # display list of topics of prayers
    def display_topics_list(self):
        db = self.connect()
        sql = 'SELECT topic FROM prayers'
        results = db.execute(sql)    
        rows = list(results)
        return rows
    # select all prayers from prayers table
    def get_prayers(self):
        db = self.connect()
        sql = 'SELECT * FROM prayers'
        results = db.execute(sql)    
        rows = list(results)
        return rows
    # display prayers from a certain topic
    def display_prayers(self, topic=""):
        db = prayers.connect()
        sql = 'SELECT * FROM prayers WHERE topic LIKE "%s"' %(topic)
        results = db.execute(sql)    
        rows = list(results)
        
        for i in range(len(rows)):
            s = str(rows[i])
            l = MDLabel(text=s.strip("(')',"))
            self.ids.other.add_widget(l)
        
# create prayers object   
prayers = Prayers()

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class BookmarkCard(MDCard):
    box = ObjectProperty()
    card = ObjectProperty()
    title = StringProperty()
    text = StringProperty()
    date = StringProperty()
    
            
class BookmarksScreen(Screen):
    
    box = ObjectProperty()

    def on_enter(self):
        self.display_bookmarks()
    
    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db")
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
        
        for i in stuff:
            author = i[2].strip("(')',")
            text = i[3].strip("(')',")
            date = i[4].strip("(')',")
            m = BookmarkCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.box.add_widget(m)
   
class HighlightsScreen(Screen):
    
    hlight = ObjectProperty()
    # call function
    def on_enter(self):
        self.display_highlights()
    
    def connect(self):
        conn = sqlite3.connect("C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/liturgy.db")
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
            m = BookmarkCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.hlight.add_widget(m)
            
            
class TopicButton(MDFlatButton):
    text = StringProperty('')
    topicname = StringProperty('')
    # def __init__(self, text):
    #     super(TopicButton, self).__init__()
    #     self.text = text
        
    def get_topic(self, val):
        self.text = val
        SortedPrayersScreen.topicname = val
        MDApp.get_running_app().root.current = 'sorted_prayers'

class SortedPrayersScreen(Screen):

    topic_prayers = ObjectProperty()
    topicname = StringProperty('')
    # def __init__(self, **kwargs):
    #     super(SortedPrayersScreen, self).__init__(**kwargs)
        # self.text = TopicButton(self.text)
        # self.add_widget(TopicButton(text=self.text))

        
    # display prayers from a certain topic
    def display_prayers(self, topic=""):
        db = prayers.connect()
        sql = 'SELECT * FROM prayers WHERE topic LIKE "%s"' %(topic)
        results = db.execute(sql)    
        rows = list(results)
        
        for i in rows:
            text = i[2].strip("(')',")
            author = i[3].strip("(')',")
            date = i[4].strip("(')',")
            card = BookmarkCard(orientation='vertical',
                        title=author,text=text,date=date)
            self.topic_prayers.add_widget(card)
            
    def on_enter(self):
        self.display_prayers(self.topicname)


class PrayersTopicScreen(Screen):
    
    topic = ObjectProperty()
    
    def on_enter(self):
        self.create_topic_list()
        
    def create_topic_list(self):
        db = prayers.connect()
        sql = 'SELECT Topic FROM prayers'
        results = db.execute(sql)    
        rows = list(results)

        for i in rows:
            s = str(i)
            tx = s.strip("(')',")
            button = TopicButton(text=tx)
            self.topic.add_widget(button)
            
    def on_leave(self):
        self.topic.clear_widgets()
            
class HistoricalScreen(Screen):
    pass

class InspirationScreen(Screen):
    pass

class DevoScreen(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty
    
    
screen_manager = ScreenManager()
screens = [
            HomeScreen(name="home"), 
            SettingsScreen(name="settings"),
            BookmarksScreen(name="bookmarks"),
            HighlightsScreen(name="highlights"),
            PrayersTopicScreen(name="topic"),
            HistoricalScreen(name="events"),
            InspirationScreen(name="insp"),
            DevoScreen(name="devo"),
            SortedPrayersScreen(name='sorted_prayers')
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
    
    # # function to show notification popup
    # def show_alert_dialog(self):
    #     if not self.dialog:
    #         self.dialog = MDDialog(
    #             text="Would you like to allow notifications?",
    #             buttons=[
    #                 MDFlatButton(
    #                     text="No", text_color=self.theme_cls.primary_color,
    #                     on_release=self.disagreed
    #                 ),
    #                 MDFlatButton(
    #                     text="Yes", text_color=self.theme_cls.primary_color,
    #                     on_release=self.agreed
    #                 ),
    #             ],
    #             size_hint=[0.7, 0.6],
    #         )
    #     self.dialog.open()
    
    # # store results of notification popup 
    # def disagreed(self, obj):
    #     print("disagreed")
    #     self.dialog.dismiss()
    # def agreed(self, obj):
    #     print("agreed")
    #     self.dialog.dismiss()
    
        
    # # call notif popup when app opens
    # # def on_start(self):
    # #     self.show_alert_dialog()

            
Liturgy().run()