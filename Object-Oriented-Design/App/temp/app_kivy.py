screen_helper = """

ScreenManager:
    SettingsScreen:

<SettingsScreen>:
    name: 'settings'
    orientation: 'vertical'
    GridLayout:
        cols: 1
        MDToolbar:
            title: 'Settings'
            left_action_items: [['home', lambda x: print(x)]]
        GridLayout:
            cols: 1

            # padding: 20
            # spacing: dp(5)
            MDLabel:
                # text_size: self.size
                text_size: root.width, 0
                # size: (0, 20)
                text: "Hello"
                # font_style: 'H5'
                # markup: True
                # valign: "top"
                # size_hint_y: 0.1
                texture_size: (0, 0)
            MDList:
                # size: self.size
                # valign: "bottom"
                OneLineListItem:
                    text: "Test"
                OneLineListItem:
                    text: "Test"
                OneLineListItem:
                    text: "Test"
            MDList:
                # size: self.size
                # valign: "bottom"
                OneLineListItem:
                    text: "Test"
                OneLineListItem:
                    text: "Test"
                OneLineListItem:
                    text: "Test"

"""
