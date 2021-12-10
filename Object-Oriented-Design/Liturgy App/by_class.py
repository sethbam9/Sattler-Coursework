

KV = '''

ScreenManager:
    HomeScreen:
    SettingsScreen:
    BookmarksScreen:
    HighlightsScreen:
    HistoricalScreen:
    InspirationScreen:
    DevoScreen:
    PrayersTopicScreen:
    
<HomeScreen>:
    name: "home"
    NavigationLayout:
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
                                root.nav_drawer.set_state("close")
                                root.manager.current = "home"
                        OneLineListItem:
                            text: "Settings"
                            on_press:
                                root.nav_drawer.set_state("close")
                                root.manager.current = "settings"
                        OneLineListItem:
                            text: "Bookmarks"
                            on_press:
                                root.nav_drawer.set_state("close")
                                root.manager.current = "bookmarks"
                        OneLineListItem:
                            text: "Highlights"
                            on_press:
                                root.nav_drawer.set_state("close")
                                root.manager.current = "highlights"     
    MDIconButton:
        icon: "menu"
        pos_hint: {"top": 1}
        on_release: nav_drawer.set_state("open")
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

<BookmarksScreen>:
    name: "bookmarks"
    MDLabel:
        text: "Bookmarks"
        halign: "center"
        
<HighlightsScreen>:
    name: "highlights"
    MDLabel:
        text: "Highlights"
        halign: "center"
        
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
    id: container
    MDList:
        id: container
        pos_hint: {"center_x": .85, "center_y": .5}
    MDFlatButton:
        text: "Go Back"
        pos_hint: {"center_x": .85, "center_y": .1}
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

           
'''
