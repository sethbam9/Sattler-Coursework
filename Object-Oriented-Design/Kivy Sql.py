import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from functools import partial


db = r"C:\Users\sethb\OneDrive\Desktop\Sattler College\5. Fall 2020\CS 202 Object-Oriented Design\bible-sqlite.db"

conn = sqlite3.connect(db)

cursor = conn.execute("SELECT * FROM t_kjv")
names = list(map(lambda x: x[0], cursor.description))
print (names)

class Scripture:

    def __init__(self, passage):
        self.passage = passage

    def GetChapter(self, ch):
        scripture = []
        chapter = conn.execute("SELECT * FROM t_kjv WHERE b = 19 AND c = %s" % (ch))
        for i in chapter:
            n = 50
            c = str(i[2])
            v = str(i[3])
            t_temp = i[4]
            t = '-\n'.join(t_temp[i:i+n] for i in range(0,len(t_temp),n))
            all = "%s:%s, %s\n" % (c, v, t)
            scripture.append(all)
        self.passage = ''.join(scripture)
        print(self.passage)

scripture = Scripture(None)
scripture.GetChapter(15)

cursorObj = conn.cursor()
cursorObj.execute('SELECT name from sqlite_master where type= "table"')
print(cursorObj.fetchall())


# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):

    # When adding widgets, we need to specify the height manually
    # (disabling the size_hint_y) so the dropdown can calculate
    # the area it needs.
    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
    dropdown.add_widget(btn)

# create a big main button
mainbutton = Button(text='Hello', size_hint=(None, None))

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton.bind(on_release=dropdown.open)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
dropdown.bind(on_select=partial (scripture.GetChapter, 5))

# https://blog.kivy.org/2014/07/wrapping-text-in-kivys-label/
runTouchApp(mainbutton)
