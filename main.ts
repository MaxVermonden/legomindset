function on_forever() {
    
}

function drive_forward(speed: number = 100) {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, speed)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, speed)
}

function drive_backwards(speed: number = 50) {
    // Hier moet ik nog bedenken hoe ik het wil gebruiken.
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, speed)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, speed)
}

function turn_left(angle: number = 50) {
    maqueen.motorStop(maqueen.Motors.M1)
    // maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, angle)
    maqueen.servoRun(maqueen.Servos.S2, 90)
}

// basic.show_string("LEFT")
// maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 0)
// basic.pause(100)
function turn_right(angle: number = 50) {
    maqueen.motorStop(maqueen.Motors.M2)
    // maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, angle)
    maqueen.servoRun(maqueen.Servos.S1, 90)
}

function demonstrate_pickup() {
    drive_forward(0)
    music.setVolume(100)
    music.playTone(Note.C, music.beat(400))
    basic.showString("PU")
    basic.pause(100)
}

function demonstrate_dropping() {
    drive_forward(0)
    music.setVolume(150)
    music.playTone(Note.D3, music.beat(400))
    basic.showString("DR")
    basic.pause(100)
}

function avoid_or_pickup() {
    let Randomchoice = randint(0, 2)
    if (Randomchoice == 0) {
        // basic.show_string("PU")
        demonstrate_pickup()
    } else if (Randomchoice == 1) {
        // basic.show_string("LE")
        turn_left()
    } else if (Randomchoice == 2) {
        // basic.show_string("RI")
        turn_right()
    }
    
}

while (true) {
    while (maqueen.Ultrasonic(0) >= 20) {
        drive_forward()
        if (maqueen.Ultrasonic(0) < 20) {
            avoid_or_pickup()
        }
        
    }
}
