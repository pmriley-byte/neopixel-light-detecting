def turnLeft(theDelay: number):
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P13, speedSlow)
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P14, speedSlow)
    basic.pause(theDelay)
def calibrate():
    global padding, samples, lightCalAll, lightCal
    music.play_tone(494, music.beat(BeatFraction.HALF))
    basic.pause(2000)
    padding = 75
    samples = 10
    for index in range(samples):
        lightCalAll = lightCalAll + input.light_level()
        music.play_tone(659, music.beat(BeatFraction.EIGHTH))
        basic.pause(150)
    lightCal = lightCalAll / samples + padding
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
def goBackward(theDelay2: number):
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P13, speedFast)
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P14, speedFast)
    basic.pause(theDelay2)
def goForward(theDelay3: number):
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P13, speedFast)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P14, speedFast)
    basic.pause(theDelay3)

def on_button_pressed_a():
    global lightCal, lightCalAll
    stopMoving(1000)
    lightCal = 0
    lightCalAll = 0
    calibrate()
input.on_button_pressed(Button.A, on_button_pressed_a)

def stopMoving(theDelay4: number):
    ContinuousServo.turn_off_motor(DigitalPin.P13)
    ContinuousServo.turn_off_motor(DigitalPin.P14)
    basic.pause(theDelay4)
def turnRight(theDelay5: number):
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P13, speedSlow)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P14, speedSlow)
    basic.pause(theDelay5)

def on_button_pressed_b():
    stopMoving(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

samples = 0
padding = 0
lightCalAll = 0
lightCal = 0
speedSlow = 0
speedFast = 0
speedFast = 50
speedSlow = 20
lightCal = 0
lightCalAll = 0
music.set_built_in_speaker_enabled(True)
basic.pause(1000)
calibrate()

def on_forever():
    if input.light_level() > lightCal:
        goBackward(1)
    else:
        stopMoving(1)
basic.forever(on_forever)
