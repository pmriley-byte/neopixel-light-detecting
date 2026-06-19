led.enable(true)
// RGB (GRB format)
let strip = neopixel.create(DigitalPin.P13, 8, NeoPixelMode.RGB)
strip.setBrightness(127)
strip.clear()
strip.show()
let range1 = strip.range(0, 1)
let range2 = strip.range(0, 2)
let range3 = strip.range(0, 3)
let range4 = strip.range(0, 4)
let range5 = strip.range(0, 5)
let range6 = strip.range(0, 6)
let range7 = strip.range(0, 7)
let range8 = strip.range(0, 8)
basic.forever(function () {
    if (input.lightLevel() > 175) {
        range8.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (input.lightLevel() > 150) {
        range7.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 125) {
        range6.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 100) {
        range5.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 75) {
        range4.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 50) {
        range3.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 25) {
        range2.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (input.lightLevel() > 0) {
        range1.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else {
    	
    }
    strip.show()
    strip.clear()
})
