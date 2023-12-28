dice1 = 0
dice2 = 0

def on_button_pressed_a():
    displayResult()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global dice1, dice2
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    displayResult()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def displayResult():
    if dice1 > 0 and dice2 > 0:
        basic.show_number(dice1)
        basic.pause(300)
        basic.show_string("+")
        basic.show_number(dice2)
        basic.pause(200)
        basic.show_string("=")
        basic.show_number(dice1 + dice2)
        if dice1 + dice2 == 7:
            basic.show_icon(IconNames.GHOST)