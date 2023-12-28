dice1 = 0
dice2 = 0

def on_gesture_shake():
    global dice1, dice2
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    basic.show_number(dice1)
    basic.pause(300)
    basic.show_string("+")
    basic.show_number(dice2)
    basic.pause(200)
    basic.show_string("=")
    basic.show_number(dice1 + dice2)
    if (dice1 + dice2==7):
        basic.show_icon(IconNames.GHOST)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
