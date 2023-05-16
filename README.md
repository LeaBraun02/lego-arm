# lego-arm-group3 (PA1473)



# PA1473 - Software Development: Agile Project 

your team write a good readme-file for your project. (The file is called README.md in your project directory.)
You are of course free to add more sections to your readme if you want to.

Readme-files on GitHub are formatted using Markdown. You can find information about how to format using Markdown here: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Your readme-file should include the following sections:


## Introduction
The goal of this project is to program a LEGO arm to perform various tasks according to user stories provided by the customer. The LEGO arm will be equipped with sensors, motors, and other necessary components to enable its functionality.


## Getting started

In order to develop the project beside a robot with three motors, arm, turning and claw and two sensors, touch and color, a code editer is needed. in this project visual studio code (vscode) is used. To connect vscode with robot the extension "LEGO® MINDSTORMS Education EV3 MicroPython" has been used. We also need to install pybrick library to be able to import class Motor, color and touch sensor, so don't need to code it by ourselves.
If a new project is created through lego extension all the essential imports codes will be there including imports for this project. 

## Building and running

This is where you explain how to make the project run. What is your startup procedure? Does the program accept different arguments to do different things?

You should also describe how to operate your program. Does it need manual input before it starts picking up and sorting the items?

All codes are in building functions with self explanatory names. Based on different user stories there are different functions but from the top the function initialize, robot_pick, robot_release and check_color is used in all user stories. 

The functions release_based_on_input do not take any argument but a dictionary is defiend globly in which the user specify which color should be droped at which position, it will simply take the item from user specified position and drop based on color which is also specified by the user.
The function pick_and_release take two argument range, how many times it should pick item and drop based on color, second argument is position which is the privious dictionary. 

The last two functions, pick_hight and pick_and_release_anywhere are for taking item from elevated position and droping any where. It take a dictionary as an argument in which the pick and drop zone is specified by user. 

## Features

Lastly, you should write which of the user stories you did and didn't develop in this project, in the form of a checklist. Like this:

We did: 
- [x] US01: As a customer, I want the robot to pick up items
- [x] US01B: As a customer, I want the robot to pick up items from a designated position
- [x] US02: As a customer, I want the robot to drop off items
- [x] US02B: As a customer, I want the robot to drop items off at a designated position.
- [x] US03: As a customer, I want the robot to be able to determine if an item is present at a given location.
- [x] US04: As a customer, I want the robot to tell me the color of an item
- [x] US04B: As a customer, I want the robot to tell me the color of an item at a designated position
- [x] US05: As a customer, I want the robot to drop items off at different locations based on the color of the item
- [x] US06: As a customer, I want the robot to be able to pick up items from elevated positions
- [x] US08B As a customer, I want to be able to calibrate items with three different colors and drop the items off at specific drop-off zones based on color
- [x] US09: As a customer, I want the robot to check the pickup location periodically to see if a new item has arrived 
    

We did not do: 
- [ ] US08 As a customer, I want to be able to calibrate maximum of three different colors and assign them to
specific drop-off zones
- [ ] US10: As a customer, I want the robots to sort items at a specific time.
- [ ] US11: As a customer, I want two robots to communicate and work together on items sorting without colliding with each other
- [ ] US12: As a customer, I want to be able to manually set the locations and heights of one pick-up zone and two drop-off zones. (Implemented either by manually dragging the arm to a position or using buttons) 
