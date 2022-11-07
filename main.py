def on_forever():
    pass

picked_up = False

def drive_forward(speed=100):
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, speed)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, speed)

def drive_backwards(speed=50): 
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, speed)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, speed)
    basic.show_string("Back")
    maqueen.motor_stop(maqueen.Motors.ALL)

    
def turn_left(angle=50):
    maqueen.motor_stop(maqueen.Motors.M1)
    maqueen.servo_run(maqueen.Servos.S2, 90)
    
def turn_right(angle=50):
    maqueen.motor_stop(maqueen.Motors.M2)
    maqueen.servo_run(maqueen.Servos.S1, 90)
    
    
def demonstrate_pickup():
    global picked_up
    drive_forward(0)
    music.set_volume(100)
    music.play_tone(Note.C, music.beat(400))
    basic.show_string("PU")
    basic.pause(500)
    pickedup = True
    

def demonstrate_dropping():
    global picked_up
    drive_forward(0)
    music.set_volume(100)
    music.play_tone(Note.D3, music.beat(400))
    basic.show_string("DR")
    basic.pause(500)
    pickedup = False

def avoid_or_pickup():
    RandomChoice = randint(0,3)
    if RandomChoice == 0 and not picked_up:
        demonstrate_pickup()
    elif RandomChoice == 0 and picked_up:
        Randomdiratpu = randint(0,1) #tweede randomizer toegevoegd, zodat de kans
            #dat die links of rechts afslaat in het algemeen even groot is'''
        if Randomdiratpu == 0:
          turn_left()
        else: 
            turn_right()
    elif RandomChoice == 1:
        turn_right()
    elif RandomChoice == 2:
        turn_left()
    elif RandomChoice == 3 and picked_up:
        demonstrate_dropping()
    elif RandomChoice == 3 and not picked_up:
        drive_backwards
               
while True:
    while maqueen.ultrasonic(0) >= 20:
        drive_forward()
    else: 
        avoid_or_pickup()

        
            

            
            
            
    
   