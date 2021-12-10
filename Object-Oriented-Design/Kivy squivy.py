import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

db = r"C:\Users\sethb\OneDrive\Desktop\Sattler College\5. Fall 2020\CS 202 Object-Oriented Design\bible-sqlite.db"
conn = sqlite3.connect(db)

class Scripture:

    def __init__(self, passage):
        self.passage = passage

    def GetChapter(self, book, ch):
        scripture = []
        chapter = conn.execute("SELECT * FROM t_kjv WHERE b = %s AND c = %s" % (book, ch))
        for i in chapter:
            n = 50
            c = str(i[2])
            v = str(i[3])
            t = i[4]
            all = "%s:%s %s\n" % (c, v, t)
            scripture.append(all)
        self.passage = ''.join(scripture)
        return self.passage

scripture = Scripture(None)
chapter = scripture.GetChapter(1, 2)

class MainApp(App):
    def build(self):
        label = Label(text="%s" % (chapter),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
