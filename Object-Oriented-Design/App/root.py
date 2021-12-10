

"""

<Manager>:
    Screen1:
        id: screen1
        name: 'Screen 1'
    Screen2:
        id: screen2
        name: 'Screen 2'
        var: screen1.num # binding

<Screen1>:
    Button:
        text: 'This is a button'
        on_press: root.calledwithbutton()

<Screen2>:
    Label:
        text: str(root.var)
        
"""