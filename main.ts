let hdg = 0
basic.forever(function on_forever() {
    
    hdg = input.compassHeading()
    basic.showString("" + ("" + hdg))
})
