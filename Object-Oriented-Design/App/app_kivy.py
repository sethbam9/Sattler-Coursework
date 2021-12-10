KV = """
#: import SlideTransition kivy.uix.screenmanager.CardTransition
<TopicButton>:
    text: self.text
    on_release: self.get_topic(self.text)
        
<BookmarkCard>:
    id: card
    card: card
    orientation: "vertical"
    size_hint: .5, None
    height: box_top.height
    focus_behavior: True
    ripple_behavior: True
    pos_hint: {"center_x": .5, "center_y": .5}
    
    MDBoxLayout:
        id: box_top
        spacing: "80dp"
        adaptive_height: True

        MDBoxLayout:
            id: text_box
            orientation: "vertical"
            adaptive_height: True
            spacing: "10dp"
            padding: "10dp", "10dp", "10dp", "10dp"

            MDLabel:
                text: root.title
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_style: "Button"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: root.date
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_style: "Subtitle2"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: root.text
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Primary"
            MDIconButton:
                icon: "delete"
    
ScreenManager:
    HomeScreen:
    SettingsScreen:
    BookmarksScreen:
    HighlightsScreen:
    HistoricalScreen:
    InspirationScreen:
    DevoScreen:
    PrayersTopicScreen:
    SortedPrayersScreen
  
    
<HomeScreen>:
    name: "home"
    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            nav_drawer: nav_drawer  
            state: "close"
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: "Home"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "home"
                    OneLineListItem:
                        text: "Settings"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "settings"
                    OneLineListItem:
                        text: "Bookmarks"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "bookmarks"
                    OneLineListItem:
                        text: "Highlights"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "highlights"    
    MDIconButton:
        icon: "menu"
        pos_hint: {"top": 1}
        on_release: 
            nav_drawer.set_state("open")
            root.manager.transition = "CardTransition()"
        
    MDCard:
        size_hint: None, None
        size: "260dp", "120dp"
        pos_hint: {"center_x": .5, "center_y": .75}
        MDLabel:
            text: app.date
            height: self.texture_size[1]
            halign: 'center'
        Image:
            source: "C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/prayer.jpg"
            size: "130dp", "100dp"
            valign: 'right'
            halighn: 'center'
            
    MDTextButton:
        text: "- Devo -"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_name: "C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/better-jack//Better Jack.ttf"
        font_size: 20
        pos_hint: {"center_x": .5, "center_y": .55}
        on_release: root.manager.current = "devo"
    
    MDTextButton:
        text: "- Prayers by Topic -"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_name: "C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/better-jack//Better Jack.ttf"
        font_size: 20
        pos_hint: {"center_x": .5, "center_y": .43}
        on_release: root.manager.current = "topic"
        
    MDTextButton:
        text: "- Daily Inspiration -"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_name: "C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/better-jack//Better Jack.ttf"
        font_size: 20
        pos_hint: {"center_x": .5, "center_y": .31}
        on_release: root.manager.current = "insp"
        
    MDTextButton:
        text: "- Historical Events -"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_name: "C:/Users/June Zimmerman/OneDrive - FLI/OO Design/Liturgy App/better-jack//Better Jack.ttf"
        font_size: 20
        pos_hint: {"center_x": .5, "center_y": .19}
        on_release: root.manager.current = "events"
        

            
<SettingsScreen>:
    name: "settings"
    MDLabel:
        text: "Settings"
        height: self.texture_size[1]
        halign: "center"
        valign: "center"
    MDFlatButton:
        text: 'Go Back'
        on_release: root.manager.current = "home"

<BookmarksScreen>:
    name: "bookmarks"
    id: box
    box: box
    MDList:
        id: box
        padding: 5
    MDFlatButton:
        text: 'Go Back'
        on_release: root.manager.current = "home"
        
<HighlightsScreen>:
    name: "highlights"
    id: hlight
    hlight: hlight
    MDList:
        id: hlight
        padding: 5
        pos_hint: {"center_x": .5, "center_y": .75}
        
    MDFlatButton:
        text: 'Go Back'
        on_release: root.manager.current = "home"
            
<DevoScreen>:
    name: 'devo'
    MDLabel:
        text: 'Devo'
        halign: 'center'
    MDFlatButton:
        text: 'Go Back'
        on_release: root.manager.current = "home"
        
<PrayersTopicScreen>:
    name: 'topic'
    id: topic
    topic: topic
    MDList:
        id: topic
        pos_hint: {"center_x": .85, "center_y": .5}
    
    MDFlatButton:
        text: "Go Back"
        pos_hint: {"center_x": .85, "center_y": .1}
        on_release: root.manager.current = "home"
        

<SortedPrayersScreen>:
    name: 'sorted_prayers'
    id: topic_prayers
    topic_prayers: topic_prayers
    MDList:
        id: topic_prayers
        
    MDFlatButton:
        text: "Go Back"
        on_release: root.manager.current = "home"
        
    
        
<InspirationScreen>:
    name: 'insp'
    MDLabel:
        text: 'Daily Inspiration'
        halign: 'center'
        
<HistoricalScreen>:
    name: 'events'
    MDLabel:
        text: 'Historical Events'
        halign: 'center'
        

"""
