screen_helper = """
ScreenManager:
    HomeScreen:
    PreDevoScreen:
    PsalmDevoScreen:
    PrayerDevoScreen:

<HomeScreen>:
    name: 'home'
    # on_pre_enter: root.wait()
    MDRectangleFlatButton:
        text: 'Devo'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'psalm'
    MDIconButton:
        icon: "account"
        user_font_size: root.width/10
        pos_hint: {'center_x':0.1,'center_y':0.9}
        size_hint: None, None
        on_press: root.manager.current = 'menu'

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
