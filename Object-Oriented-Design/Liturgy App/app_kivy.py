
KV = """
<MyLabel@Label>:
    color: 0, 0, 0, 1

<TopicButton>:
    text: self.text
    theme_text_color: "Custom"
    text_color: app.theme_cls.primary_color
    font_style: "Button"
    font_size: 20
    bold: True
    on_release: self.get_topic(self.text)

<VerseButton>:
    text_size: self.width, None
    size_hint: 1, None
    height: self.texture_size[1]
    on_release: self.bookmark_vs()


<PrayerCard>:
    id: prayer_card
    prayer_card: prayer_card
    orientation: "vertical"
    size_hint: .5, None
    height: box_top.height
    focus_behavior: True
    ripple_behavior: True
    pos_hint: {"center_x": .5, "center_y": .5}

    MDBoxLayout:
        id: box_top
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
                font_style: "Overline"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: root.text
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Primary"

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
                text: "Saved:" + " " + root.date
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_style: "Overline"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: root.text
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Primary"
            MDIconButton:
                icon: "delete"
                root: 'bookmarks'
                on_release: root.remove_bookmark(root.text)

ScreenManager:
    HomeScreen:
    SettingsScreen:
    BookmarksScreen:
    HighlightsScreen:
    HistoricalScreen:
    InspirationScreen:
    PrayersTopicScreen:
    SortedPrayersScreen
    UserInfo:
    PreDevoScreen:
    PsalmDevoScreen:
    PrayerDevoScreen:
    TextFormatting:
    ThemeOptions:
    ContentOptions:
    NotificationOptions:

<HomeButtons@MDTextButton>:
    theme_text_color: "Custom"
    text_color: app.theme_cls.primary_color
    font_name: "C:/Users/sethb/OneDrive/Desktop/Sattler College/5. Fall 2020/CS 202 Object-Oriented Design/Liturgy App/better-jack/Better Jack.ttf"

<HomeScreen>:
    name: "home"

    MDIconButton:
        icon: "menu"
        pos_hint: {"top": 1}
        on_release:
            nav_drawer.set_state("open")

    MDCard:
        size_hint: None, None
        size: "260dp", "120dp"
        pos_hint: {"center_x": .5, "center_y": .75}
        MDLabel:
            text: app.date
            height: self.texture_size[1]
            halign: 'center'
        Image:
            source: "C:/Users/sethb/OneDrive/Desktop/Sattler College/5. Fall 2020/CS 202 Object-Oriented Design/Liturgy App/prayer.jpg"
            size: "130dp", "100dp"
            valign: 'right'
            halighn: 'center'

    HomeButtons:
        text: "- Devo -"
        pos_hint: {"center_x": .5, "center_y": .55}
        on_release: root.manager.current = "pre_devo"

    HomeButtons:
        text: "- Prayers by Topic -"
        pos_hint: {"center_x": .5, "center_y": .43}
        on_release: root.manager.current = "topic"

    HomeButtons:
        text: "- Daily Inspiration -"
        pos_hint: {"center_x": .5, "center_y": .31}
        on_release: root.manager.current = "insp"

    HomeButtons:
        text: "- Historical Events -"
        pos_hint: {"center_x": .5, "center_y": .19}
        on_release: root.manager.current = "events"

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            nav_drawer: nav_drawer
            state: "close"
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "Home"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "home"
                        IconLeftWidget:
                            icon: 'home'
                    OneLineIconListItem:
                        text: "Settings"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "settings"
                        IconLeftWidget:
                            icon: 'settings'
                    OneLineIconListItem:
                        text: "Bookmarks"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "bookmarks"
                        IconLeftWidget:
                            icon: 'bookmark'
                    OneLineIconListItem:
                        text: "Highlights"
                        on_press:
                            nav_drawer.set_state("close")
                            root.manager.current = "highlights"
                        IconLeftWidget:
                            icon: 'format-color-highlight'

<SettingsLabels@MDLabel>:
    size_hint_y: 0.20
    text_size: self.size
    valign: "center"
    font_style: 'H5'

<SettingsScreen>:
    name: 'settings'
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        cols: 1

        MDToolbar:
            pos_hint: {"top": 1}
            title: 'Settings'
            left_action_items: [['home', lambda x: root.back_button()]]

        BoxLayout:
            orientation: 'vertical'
            cols: 1

            size_hint: [.9, .9]
            pos_hint: { 'top' : .95, 'right': .95}

            SettingsLabels:
                text: "Account"

            MDTextButton:
                size_hint_y: 0.20
                text: "User Info"
                on_press: root.manager.current = 'userinfo'

            SettingsLabels:
                text: "Theme"

            MDTextButton:
                size_hint_y: 0.20
                text: "Theme Options"
                on_press: root.manager.current = 'themeoptions'

            SettingsLabels:
                text: "Preferences"

            MDTextButton:
                size_hint_y: 0.20
                text: "Content Preferences"
                on_press: root.manager.current = 'contentoptions'

            MDTextButton:
                size_hint_y: 0.20
                text: "Notifications"
                on_press: root.manager.current = 'notificationoptions'

            MDTextButton:
                size_hint_y: 0.20
                text: "Text Formatting"
                on_press: root.manager.current = 'textformat'

            MDTextButton:
                size_hint_y: 0.20
                text: "Restore Default"
                font_size: "18sp"
                color: .761, .190, .810, 1

<UserInfo>:
    name: 'userinfo'
    orientation: 'vertical'
    MDToolbar:
        pos_hint: {"top": 1}
        title: 'User Info'
        left_action_items: [['arrow-left',  lambda x: root.back_button()]]
    BoxLayout:
        orientation: 'vertical'
        cols: 1
        pos_hint: {"center_y": 0.9}
        height: self.minimum_height
        padding: "16dp"

        MDTextField:
            id : name
            text: root.content_list[3]
            hint_text: "User Name"

        MDTextField:
            id: password
            text: root.content_list[2]
            hint_text: "Password"

        MDTextField
            id: email
            text: root.content_list[4]
            hint_text: "Email"

        MDRaisedButton:
            text: "Save"
            on_release: root.save()

<TextFormatting>:
    name: 'textformat'
    orientation: 'vertical'

    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Text Formatting'
        left_action_items: [['arrow-left',  lambda x: root.back_button()]]
    FloatLayout:

        size_hint: [.9, .9]
        pos_hint: { 'top' : .95, 'right': .95}

        MDLabel:
            size_hint_y: 0.20
            text_size: self.size
            text: "Font Size: " + str(size.value) + " px"
            pos_hint: {'center_x': .8, 'center_y': 0.8}

        Slider:
            id: size
            min: 8
            max: 64
            step: 1
            size_hint_y: 0.20
            pos_hint: {'center_x': .5, 'center_y': 0.6}
            value: root.content_list[3]

        Spinner:
            id: font

            text: root.content_list[2]

            values: ["Arial", "Times New Roman", "Roboto"]

            size_hint: None, None
            size: 200, 50
            pos_hint: {'center_x': .5, 'center_y': 0.4}

        MDRaisedButton:
            text: "Save"
            pos_hint: {'center_x': .5, 'center_y': .2}
            on_release: root.save()

<ContentOptions>:
    name: 'contentoptions'
    orientation: 'vertical'

    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Content Options'
        left_action_items: [['arrow-left',  lambda x: root.back_button()]]
    FloatLayout:

        size_hint: [.9, .9]
        pos_hint: { 'top' : .85, 'right': .95}

        MyLabel:
            text: "Prayers"
            pos_hint: {'center_x': .3, 'center_y': 0.875}
        MDCheckbox:
            id: prayers
            active: root.content_list[1]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': 0.875}
        MyLabel:
            text: "Psalms"
            pos_hint: {'center_x': .3, 'center_y': 0.8}
        MDCheckbox:
            id: psalms
            active: root.content_list[2]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .8}
        MyLabel:
            text: "Scripture"
            pos_hint: {'center_x': .3, 'center_y': .725}
        MDCheckbox:
            id: scripture
            active: root.content_list[3]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .725}
        MyLabel:
            text: "Hymns"
            pos_hint: {'center_x': .3, 'center_y': .65}
        MDCheckbox:
            id: hymns
            active: root.content_list[4]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .65}
        MyLabel:
            text: "Patristics"
            pos_hint: {'center_x': .3, 'center_y': .575}
        MDCheckbox:
            id: patristics
            active: root.content_list[5]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .575}
        MyLabel:
            text: "Commmentary"
            pos_hint: {'center_x': .3, 'center_y': .5}
        MDCheckbox:
            id: commentary
            active: root.content_list[6]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .5}
        MyLabel:
            text: "Anabaptist"
            pos_hint: {'center_x': .3, 'center_y': .425}
        MDCheckbox:
            id: anabaptist
            active: root.content_list[7]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .425}
        MyLabel:
            text: "Biblical Languages"
            pos_hint: {'center_x': .3, 'center_y': .35}
        MDCheckbox:
            id: languages
            active: root.content_list[8]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .35}
        MyLabel:
            text: "Audio"
            pos_hint: {'center_x': .3, 'center_y': .275}
        MDCheckbox:
            id: audio
            active: root.content_list[9]
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .275}
        MDRaisedButton:
            text: "Save"
            pos_hint: {'center_x': .5, 'center_y': .15}
            on_release: root.save()

<ThemeOptions>:
    name: 'themeoptions'
    orientation: 'vertical'

    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Theme Options'
        left_action_items: [['arrow-left',  lambda x: root.back_button()]]
    FloatLayout:

        size_hint: [.9, .9]
        pos_hint: { 'top' : .85, 'right': .95}

        BoxLayout:
            pos_hint: {'center_x': .5, 'center_y': .6}
            RelativeLayout:
                ImageToggleButton:
                    id: classic
                    group: 'theme'
                    source: "C:/Users/sethb/OneDrive/Desktop/Sattler College/5. Fall 2020/CS 202 Object-Oriented Design/Liturgy App/classic.jpg"
                    state: root.classic

            RelativeLayout:
                ImageToggleButton:
                    id: modern
                    group: 'theme'
                    source: "C:/Users/sethb/OneDrive/Desktop/Sattler College/5. Fall 2020/CS 202 Object-Oriented Design/Liturgy App/classic2.jpeg"
                    state: root.modern

        MDRaisedButton:
            text: "Save"
            pos_hint: {'center_x': .5, 'center_y': .3}
            on_release: root.save()

<NotificationOptions>:
    name: 'notificationoptions'
    orientation: 'vertical'

    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Notifications'
        left_action_items: [['arrow-left',  lambda x: root.back_button()]]
    FloatLayout:

        size_hint: [.9, .9]
        pos_hint: { 'top' : .95, 'right': .95}

        MyLabel:
            text: "On/Off"
            pos_hint: {'center_x': .25, 'center_y': .8}
        MDCheckbox:
            id: checked
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .75, 'center_y': .8}
            active: root.content_list[5]

        Spinner:
            id: type

            text: root.content_list[6]

            values: ["Banner", "Popup"]

            size_hint: None, None
            size: 200, 50
            pos_hint:{'center_x':.5, 'top': 0.7}


        Spinner:
            id: schedule

            text: root.content_list[7]

            values: ["3/day", "2/day", "Daily", "Weekly", "Monthly", "Yearly"]

            size_hint: None, None
            size: 200, 50
            pos_hint:{'center_x':.5, 'top': 0.5}

        MDRaisedButton:
            text: "Save"
            pos_hint: {'center_x': .5, 'center_y': .3}
            on_press: root.save()

<BookmarksScreen>:
    name: "bookmarks"
    id: box
    box: box
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Bookmarks"
            left_action_items: [['home', lambda x: app.back_button()]]

        ScrollView:
            MDList:
                id: box

<HighlightsScreen>:
    name: "highlights"
    id: hlight
    hlight: hlight
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Highlights"
            left_action_items: [['home', lambda x: app.back_button()]]

        ScrollView:
            MDList:
                id: hlight

<PrayersTopicScreen>:
    name: 'topic'
    id: topic
    topic: topic
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Prayers by Topic"
            left_action_items: [['home', lambda x: app.back_button()]]

        ScrollView:
            pos_hint: {'center_x': .75, 'center_y': .8}
            MDList:
                id: topic

<SortedPrayersScreen>:
    name: 'sorted_prayers'
    id: topic_prayers
    topic_prayers: topic_prayers
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Prayers by Topic"
            left_action_items: [['arrow-left', lambda x: root.back_button()]]

        ScrollView:
            MDList:
                id: topic_prayers

<InspirationScreen>:
    name: 'insp'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Daily Inspiration"
            left_action_items: [['home', lambda x: app.back_button()]]
        MDLabel:
            text: 'Daily Inspiration'
            halign: 'center'

<HistoricalScreen>:
    name: 'events'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Historical Events"
            left_action_items: [['home', lambda x: app.back_button()]]
        MDLabel:
            text: 'Historical Events'
            halign: 'center'

<PreDevoScreen>:
    name: 'pre_devo'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "C:/Users/sethb/OneDrive/Desktop/Sattler College/5. Fall 2020/CS 202 Object-Oriented Design/Liturgy App/calm.jpg"
    MDLabel:
        text: root.quote
        halign: "justify"
        size_hint: 0.5, None
        pos_hint: {'center_x':0.5,'center_y':0.7}
        font_style: "H6"
    MDRectangleFlatButton:
        text: 'Time'
        text_color: 0, 0, 0, 1
        font_size: root.width/20
        size_hint: 0.25, 0.05
        pos_hint: {'center_x':0.5,'center_y':0.35}
    MDRectangleFlatButton:
        text: 'BEGIN'
        text_color: 0, 0, 0, 1
        font_size: root.width/10
        size_hint: 0.5, 0.1
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'psalm'

<DevoTitle>:
    halign: "center"
    pos_hint: {'center_x':0.5,'center_y':0.92}
    font_style: "H4"

<DevoTop>:
    pos_hint:{'center_y':1.4}
    rows: 1
    MDIconButton:
        id: homebtn
        icon: "home"
        user_font_size: root.width/10
        pos_hint: {'center_x':0.1,'center_y':0.92}
        size_hint: None, None
    MDLabel:
        font_style: "H4"
    MDIconButton:
        id: textbtn
        icon: "text"
        user_font_size: root.width/10
        pos_hint: {'center_x':0.9,'center_y':0.92}
        size_hint: None, None

<DevoBottom>:
    # size_hint_x: .8
    pos_hint:{'center_y':-0.35, 'center_x':.65}
    rows:1
    MDIconButton:
        id: leftbtn
        icon: "menu-left"
        user_font_size: root.width/13
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size_hint: None, None
    MDIconButton:
        id: bookmarkbtn
        icon: "bookmark-outline"
        user_font_size: root.width/10
        pos_hint: {'center_x':0.1,'center_y':0.18}
        size_hint: None, None
    MDIconButton:
        id: audiobtn
        icon: "play-circle-outline"
        user_font_size: root.width/10
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size_hint: None, None
    MDIconButton:
        id: rightbtn
        icon: "menu-right"
        user_font_size: root.width/13
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size_hint: None, None

<DevoBar>
    value: 10
    color: app.theme_cls.accent_color
    pos_hint: {'center_y':0.05, 'center_x': .5}
    size_hint_x: .9

<PsalmDevoScreen>:
    name: 'psalm'
    on_pre_enter: root.getVerses(root.ch)

<PrayerDevoScreen>:
    name: 'prayer'
    on_pre_enter: root.getVerses(root.ch)

"""
