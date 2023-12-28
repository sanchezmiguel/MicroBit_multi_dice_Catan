let dice1 = 0
let dice2 = 0
input.onGesture(Gesture.Shake, function () {
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    basic.showNumber(dice1)
    basic.pause(300)
    basic.showString("+")
    basic.showNumber(dice2)
    basic.pause(200)
    basic.showString("=")
    basic.showNumber(dice1 + dice2)
    if (dice1 + dice2 == 7) {
        basic.showIcon(IconNames.Ghost)
    }
})
