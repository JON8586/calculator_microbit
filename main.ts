input.onPinPressed(TouchPin.P0, function () {
    mode += 1
    basic.showNumber(mode)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    a += 1
    basic.showNumber(a)
})
input.onPinPressed(TouchPin.P2, function () {
    mode = 0
    basic.showNumber(mode)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    if (mode == 0) {
        basic.clearScreen()
        basic.showNumber(a + b)
        a = 0
        b = 0
    }
    if (mode == 1) {
        basic.clearScreen()
        basic.showNumber(a - b)
        a = 0
        b = 0
    }
    if (mode == 2) {
        basic.clearScreen()
        basic.showNumber(a * b)
        a = 0
        b = 0
    }
    if (mode == 3) {
        basic.clearScreen()
        basic.showNumber(a / b)
        a = 0
        b = 0
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    b += 1
    basic.showNumber(b)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showNumber(mode)
    basic.pause(100)
    basic.clearScreen()
})
let mode = 0
let b = 0
let a = 0
a = 0
b = 0
mode = 0
