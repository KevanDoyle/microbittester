let hdg = 0
basic.forever(function () {
    hdg = input.compassHeading()
    basic.showString("" + (hdg))
})
