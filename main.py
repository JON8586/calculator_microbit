def on_pin_pressed_p0():
    global mode
    mode += 1
    basic.show_number(mode)
    basic.pause(100)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global a
    basic.clear_screen()
    a += 1
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global mode
    mode = 0
    basic.show_number(mode)
    basic.pause(100)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global a, b
    if mode == 0:
        basic.clear_screen()
        basic.show_number(a + b)
        a = 0
        b = 0
    if mode == 1:
        basic.clear_screen()
        basic.show_number(a - b)
        a = 0
        b = 0
    if mode == 2:
        basic.clear_screen()
        basic.show_number(a * b)
        a = 0
        b = 0
    if mode == 3:
        basic.clear_screen()
        basic.show_number(a / b)
        a = 0
        b = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    basic.clear_screen()
    b += 1
    basic.show_number(b)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_number(mode)
    basic.pause(100)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

mode = 0
b = 0
a = 0
a = 0
b = 0
mode = 0