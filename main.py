hdg = 0

def on_forever():
    global hdg
    hdg = input.compass_heading()
    basic.show_string("" + str((hdg)))
basic.forever(on_forever)
