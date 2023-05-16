#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from sys import exit

# Definitions
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch = TouchSensor(Port.S1)


position = {'right': 5, 'middle': -365, 'side': -550, 'left': -660}
# Right = 0
# Middle = -365
# Side = -550
# Left = -660
# blue = input(
#     'Where to release blue item, Right, Middle, Side or Left, else press enter: ').lower()
# red = input(
#     'Where to release red item, Right, Middle, Side or Left, else press enter: ').lower()
# green = input(
#     'Where to release green item, Right, Middle, Side or Left, else press enter: ').lower()
# yellow = input(
#     'Where to release yellow item, Right, Middle, Side or Left, else press enter: ').lower()

blue, red, green, yellow = 'middle', 'right', 'left', 'side'
colors = {'BLUE': blue, 'GREEN': green, 'YELLOW': yellow, 'RED': red}

color_position = 320


def initialize():
    # Initiliaze the arm motor
    arm_motor.run_until_stalled(-2000, then=Stop.HOLD, duty_limit=40)
    arm_motor.reset_angle(0)
    arm_motor.run_target(300, 300, then=Stop.HOLD)


def robot_pick(place):
    # Initializing the turrning
    while not touch.pressed():
        # turning_motor.run_angle(90,100, then=Stop.HOLD)
        turning_motor.run_until_stalled(600, then=Stop.HOLD, duty_limit=30)
        turning_motor.run_angle(90, 20)
    turning_motor.reset_angle(0)

    turning_motor.run_target(200, place, then=Stop.COAST)

    # picking the item
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
    arm_motor.run_target(300, 485, then=Stop.HOLD)
    time.sleep(3)
    claw_motor.run_target(200, -20, then=Stop.HOLD)
    arm_motor.run_target(300, color_position, then=Stop.HOLD)
    # 260 är höjden på blocket i grader, ju lägre grad desto högre höjd från marken.


def robot_release(x=False, y=False, place=False):
    # moving toward targt
    if place:
        turning_motor.run_target(200, place, then=Stop.COAST)
        arm_motor.run_target(300, 465, then=Stop.HOLD)
        claw_motor.run_target(200, -90, then=Stop.HOLD)
        arm_motor.run_target(300, 320, then=Stop.COAST)
    else:
        turning_motor.run_target(200, x, then=Stop.COAST)
        arm_motor.run_target(300, y, then=Stop.COAST)
        claw_motor.reset_angle(0)
        claw_motor.run_target(200, -90)


def check_color():
    if not str(color_sensor.color()) == 'Color.BLACK' and not str(color_sensor.color()) == 'None':
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


def release_based_on_input():
    if str(color_sensor.color()) == 'Color.BLUE':
        robot_release(position[colors['BLUE']])
    elif str(color_sensor.color()) == 'Color.GREEN':
        robot_release(position[colors['GREEN']])
    elif str(color_sensor.color()) == 'Color.YELLOW':
        robot_release(position[colors['YELLOW']])
    elif str(color_sensor.color()) == 'Color.RED':
        robot_release(position[colors['RED']])

    else:
        ev3.speaker.say('color not identified')


def run_check(position):
    robot_pick(position)
    check_color()
    release_based_on_input()
    arm_motor.run_target(300, 250, then=Stop.HOLD)


def pick_and_release(r, position):
    initialize()
    for i in range(r):
        run_check(position)
        print(i+1)
        print(str(color_sensor.color())[6:])

        if str(color_sensor.color()) == 'Color.BLACK':
            time.sleep(5)
            ev3.speaker.say('looking for new item')
            run_check()

            if str(color_sensor.color()) == 'Color.BLACK':
                time.sleep(5)
                ev3.speaker.say('looking for new item')
                run_check()

                if str(color_sensor.color()) == 'Color.BLACK':
                    ev3.speaker.say('no item found')
                    ev3.speaker.say('Shutting down')
                    exit()
                else:
                    print('thered loop')

            else:
                print('second loop')

        else:
            print('first loop')


# robot_pick(Right)

# # ev3.speaker.say(str(color_sensor.color()))
# print(color_sensor.color())
# print(color_sensor.rgb())

# a = color_sensor.rgb()
# l = [i for i in a]
# l_sort = sorted(l)
# l_index = [l.index(l_sort[-1]), l.index(l_sort[-2])]
# l_max = [l_sort[-1], l_sort[-2], l_sort[-3]]

# print(l_max[0])

# if l[0] > 7 and l[1] > 7:
#     print("Yellow")

# elif l[0] >= 12:
#     print("Red")

# elif l[1] >= 12:
#     print("Green")

# elif l[2] >= 12:
#     print("Blue")

# else:
#     pass


#  US06
def pick_hight(x, y):

    while not touch.pressed():
        # turning_motor.run_angle(90,100, then=Stop.HOLD)
        turning_motor.run_until_stalled(600, then=Stop.HOLD, duty_limit=30)
        turning_motor.run_angle(90, 20)
    turning_motor.reset_angle(0)
    arm_motor.run_target(300, y, then=Stop.HOLD)
    turning_motor.run_target(200, x, then=Stop.COAST)

    # take item from position ...
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
    time.sleep(3)
    claw_motor.run_target(200, -20, then=Stop.HOLD)
    arm_motor.run_target(300, 300, then=Stop.HOLD)

    check_color()


# parameter x and y position

pick_drop = {'pick': 'side', 'drop': [-100, 200]}

initialize()
if type(pick_drop['pick']) == str:
    robot_pick(place=position[pick_drop['pick']])
    check_color()
else:
    pick_hight(x=pick_drop['pick'][0], y=pick_drop['pick'][1])

if type(pick_drop['drop']) == str:
    robot_release(place=position[pick_drop['drop']])
else:
    robot_release(x=pick_drop['drop'][0], y=pick_drop['drop'][1])
