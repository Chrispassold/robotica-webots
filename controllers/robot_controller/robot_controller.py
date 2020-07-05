"""robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from collections import namedtuple

ROBOT_ORIENTATION_NORTH = 300
ROBOT_ORIENTATION_EAST = 301 #right
ROBOT_ORIENTATION_SOUTH = 302
ROBOT_ORIENTATION_WEST = 303 #left

ROBOT_TURN_DIRECTION_LEFT = 100
ROBOT_TURN_DIRECTION_RIGHT = 101

ROBOT_DIRECTION_FRONT = 200
ROBOT_DIRECTION_BACK = 203

ROBOT_DIRECTION_POSITION_DEFAULT = 12.0
ROBOT_TURN_POSITION_DEFAULT = 12.0

Distances = namedtuple('Distance', 'front right back left')

##############################
##############################
# create the Robot instance.
##############################
##############################
robot = Robot()

##############################
##############################
# initial orientation
##############################
##############################
orientation = ROBOT_ORIENTATION_NORTH

##############################
##############################
# get the time step of the current world.
##############################
##############################
timestep = int(robot.getBasicTimeStep())

##############################
##############################
# motors
##############################
##############################
motorLeft = robot.getMotor('left wheel motor')
motorRight = robot.getMotor('right wheel motor')

##############################
##############################
# distance sensor setup
##############################
##############################
ds_front = robot.getDistanceSensor('ps0')
ds_front.enable(timestep)

ds_back = robot.getDistanceSensor('ps4')
ds_back.enable(timestep)

ds_left = robot.getDistanceSensor('ps5')
ds_left.enable(timestep)

ds_right = robot.getDistanceSensor('ps2')
ds_right.enable(timestep)

##############################
##############################
# change orientation based on turn direction
##############################
##############################
def update_orientation(turn_direction):
    if turn_direction == ROBOT_TURN_DIRECTION_LEFT:
        if orientation == ROBOT_ORIENTATION_NORTH:
            orientation = ROBOT_ORIENTATION_WEST
        elif orientation == ROBOT_ORIENTATION_EAST:
            orientation = ROBOT_ORIENTATION_NORTH
        elif orientation == ROBOT_ORIENTATION_SOUTH:
            orientation = ROBOT_ORIENTATION_EAST
        elif orientation == ROBOT_ORIENTATION_WEST:
            orientation = ROBOT_ORIENTATION_SOUTH
        else:
            print("INVALID TURN DIRECTION")
    elif turn_direction == ROBOT_TURN_DIRECTION_RIGHT:
        if orientation == ROBOT_ORIENTATION_NORTH:
            orientation = ROBOT_ORIENTATION_EAST
        elif orientation == ROBOT_ORIENTATION_EAST:
            orientation = ROBOT_ORIENTATION_SOUTH
        elif orientation == ROBOT_ORIENTATION_SOUTH:
            orientation = ROBOT_ORIENTATION_WEST
        elif orientation == ROBOT_ORIENTATION_WEST:
            orientation = ROBOT_ORIENTATION_NORTH
        else:
            print("INVALID TURN DIRECTION")


##############################
##############################
# turn robot in a direction and change orientation
##############################
##############################
def turn(direction):
    if direction == ROBOT_TURN_DIRECTION_LEFT:
        motorRight.setPosition(ROBOT_TURN_POSITION_DEFAULT)
    elif direction == ROBOT_TURN_DIRECTION_RIGHT:
        motorLeft.setPosition(ROBOT_TURN_POSITION_DEFAULT)
    else:
        print("INVALID TURN DIRECTION")

    update_orientation(direction)

##############################
##############################
# move robot in a direction
##############################
##############################
def move(direction):        
    if direction == ROBOT_DIRECTION_FRONT:
        motorLeft.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
    elif direction == ROBOT_DIRECTION_BACK:
        motorLeft.setPosition(-ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(-ROBOT_DIRECTION_POSITION_DEFAULT)
    else:
        print("INVALID MOVE DIRECTION")
    
##############################
##############################
# return distance in all directions
##############################
##############################
def get_distance():        
    return Distances(front=ds_front.getValue(), right=ds_right.getValue(), back=ds_back.getValue(), left=ds_left.getValue())

##############################
##############################
# execute next step
##############################
##############################
def next_step():
    dist = get_distance()
    print(dist)
    

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while True:
    robot.step(timestep)
    next_step()
    move(ROBOT_DIRECTION_FRONT)
    
# Enter here exit cleanup code.
