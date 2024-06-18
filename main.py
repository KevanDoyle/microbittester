hdg = 0
def on_forever():
    hdg = input.compass_heading()
    basic.show_string(hdg`)
basic.forever(on_forever)
