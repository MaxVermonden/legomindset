def on_forever():
    pass

def drive_forward(speed=100):
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, speed)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, speed)

def drive_backwards(speed=50): #Hier moet ik nog bedenken hoe ik het wil gebruiken.
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, speed)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, speed)
    
def turn_left(angle=50):
    maqueen.motor_stop(maqueen.Motors.M1)
    #maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, angle)
    maqueen.servo_run(maqueen.Servos.S2, 90)
    #basic.show_string("LEFT")
    #maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 0)
    #basic.pause(100)
    
def turn_right(angle=50):
    maqueen.motor_stop(maqueen.Motors.M2)
    #maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, angle)
    maqueen.servo_run(maqueen.Servos.S1, 90)
    
def demonstrate_pickup():
    drive_forward(0)
    music.set_volume(100)
    music.play_tone(Note.C, music.beat(400))
    basic.show_string("PU")
    basic.pause(100)
    

def demonstrate_dropping():
    drive_forward(0)
    music.set_volume(150)
    music.play_tone(Note.D3, music.beat(400))
    basic.show_string("DR")
    basic.pause(100)

def avoid_or_pickup():
    Randomchoice = randint(0,2)
    if Randomchoice == 0:
        #basic.show_string("PU")
        demonstrate_pickup()
    elif Randomchoice == 1:
        #basic.show_string("LE")
        turn_left()
    elif Randomchoice == 2:
        #basic.show_string("RI")
        turn_right()
        
while True:
    while maqueen.ultrasonic(0) >= 20:
        drive_forward()
        if maqueen.ultrasonic(0) < 20:
            avoid_or_pickup()

        
            

            
            
            
    
   