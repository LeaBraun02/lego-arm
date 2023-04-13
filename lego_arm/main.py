#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
# Definitions
ev3 = EV3Brick()
base_motor = Motor(Port.C)
elbow_motor = Motor(Port.B)
gripper_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
base_switch = TouchSensor(Port.S1)

ev3.speaker.beep()

wait(10)

elbow_motor.run_until_stalled(-80, then=Stop.Hold, duty_limit=20)
wait(10)
elbow_motor.hold()
ev3.speaker.beep()

base_motor.run(60)
while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()
ev3.speaker.beep()

gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.hold()
ev3.speaker.beep()



#turning_motor.run_angle(70, -180, then=Stop.COAST)

#arm_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=20)

#turning_motor.run_target(70,0, then=Stop.COAST)

# while True:
#    print(turning_motor.angle())
#    wait(500)




# Create your objects here.
# Definitions
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch = TouchSensor(Port.S1)


ev3.speaker.say('hello World')
arm_motor.run_angle(90, -190, then=Stop.HOLD)

while not touch.pressed():
    turning_motor.run_angle(50,50, then=Stop.HOLD)

claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
claw_motor.reset_angle(0)
claw_motor.run_target(200, -90)
arm_motor.run_angle(90, 190, then=Stop.HOLD)
claw_motor.run_angle(50, 70, then=Stop.HOLD)
arm_motor.run_angle(90, -190, then=Stop.HOLD)

ev3.speaker.say(str(color_sensor.color()))

turning_motor.run_angle(-90,300, then=Stop.COAST)
arm_motor.run_angle(90, 190, then=Stop.HOLD)
claw_motor.run_angle(50, -60, then=Stop.HOLD)
arm_motor.run_angle(90, -190, then=Stop.COAST)




# Create your objects here.
# Definitions
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch = TouchSensor(Port.S1)


ev3.speaker.say('hello World')
arm_motor.run_angle(90, -190, then=Stop.HOLD)

while not touch.pressed():
    turning_motor.run_angle(50,50, then=Stop.HOLD)

claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
claw_motor.reset_angle(0)
claw_motor.run_target(200, -90)
arm_motor.run_angle(90, 190, then=Stop.HOLD)
claw_motor.run_angle(50, 70, then=Stop.HOLD)
arm_motor.run_angle(90, -190, then=Stop.HOLD)

ev3.speaker.say(str(color_sensor.color()))

turning_motor.run_angle(-90,300, then=Stop.COAST)
arm_motor.run_angle(90, 190, then=Stop.HOLD)
claw_motor.run_angle(50, -60, then=Stop.HOLD)
arm_motor.run_angle(90, -190, then=Stop.COAST)



