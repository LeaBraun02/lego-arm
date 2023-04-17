#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile





ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch = TouchSensor(Port.S1)


Right = 10 
Middle = -355
Side = -490
Left = -650


# ev3.speaker.say('Hello World')

def robot_pick(place): 
    # Initiliaze the arm motor
    arm_motor.run_until_stalled(-2000, then=Stop.HOLD, duty_limit=20)
    arm_motor.reset_angle(0)
    arm_motor.run_target(200, 300, then=Stop.HOLD)
    
    #Initializing the turrning
    while not touch.pressed():
        turning_motor.run_angle(50,50, then=Stop.HOLD)
    turning_motor.reset_angle(0)

    turning_motor.run_target(90, place, then=Stop.COAST)
    # picking the item 
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
    
    arm_motor.run_target(90, 485, then=Stop.HOLD)
    claw_motor.run_target(200, -20, then=Stop.HOLD)
    arm_motor.run_target(90, 280, then=Stop.HOLD)
    

def robot_release(place):
    # moving toward targt
    turning_motor.run_target(90, place, then=Stop.COAST)
    arm_motor.run_target(90, 465, then=Stop.HOLD)
    claw_motor.run_target(200, -90, then=Stop.HOLD)
    arm_motor.run_target(90, 320, then=Stop.COAST)
    



# robot_pick(Middle)
# ev3.speaker.say(str(color_sensor.color()))
# print(color_sensor.color())
# robot_release(Side)








Right = 10 
Middle = -365
Side = -550
Left = -660


# ev3.speaker.say('Hello World')

def initialize():
    # Initiliaze the arm motor
    arm_motor.run_until_stalled(-2000, then=Stop.HOLD, duty_limit=20)
    arm_motor.reset_angle(0)
    arm_motor.run_target(300, 300, then=Stop.HOLD)

def robot_pick(place): 
    #Initializing the turrning
    while not touch.pressed():
        # turning_motor.run_angle(90,100, then=Stop.HOLD)
        turning_motor.run_until_stalled(600, then=Stop.HOLD, duty_limit=30)
        turning_motor.run_angle(90,20)
    turning_motor.reset_angle(0)

    turning_motor.run_target(90, place, then=Stop.COAST)
    
    # picking the item 
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
    
    arm_motor.run_target(300, 485, then=Stop.HOLD)
    time.sleep(2) 
    claw_motor.run_target(200, -20, then=Stop.HOLD)
    arm_motor.run_target(300, 300, then=Stop.HOLD)
    

def robot_release(place):
    # moving toward targt
    turning_motor.run_target(90, place, then=Stop.COAST)
    arm_motor.run_target(300, 465, then=Stop.HOLD)
    claw_motor.run_target(200, -90, then=Stop.HOLD)
    arm_motor.run_target(300, 320, then=Stop.COAST)
    


def check_color():
    if  not str(color_sensor.color()) == 'Color.BLACK' or  not str(color_sensor.color()) == 'None':
        ev3.speaker.say('item loaded')
        c = str(color_sensor.color())
        ev3.speaker.say(str(c[6:]))
     
    else:
        ev3.speaker.say('No item loaded')

def release_based_on_color():
    if str(color_sensor.color()) == 'Color.BLUE':
        robot_release(Middle)
    elif str(color_sensor.color()) == 'Color.GREEN':
        robot_release(Side)
    elif str(color_sensor.color()) == 'Color.YELLOW' or str(color_sensor.color()) == 'Color.RED':
        robot_release(Left)
    else:
        ev3.speaker.say('color not identified')
        
def run_check():
    robot_pick(Right)
    check_color()
    release_based_on_color()
    arm_motor.run_target(300, 300, then=Stop.HOLD)

initialize() 
for i in range(5):
    run_check()
    print(i)
    
    if str(color_sensor.color()) == 'Color.BLACK':
        time.sleep(5)
        run_check()
        if str(color_sensor.color()) == 'Color.BLACK':
            ev3.speaker.say('no item found')
            ev3.speaker.say('Shutting down')
            exit()
        else:
            print('second loop')
            
    else:
        print('first loop')
        
