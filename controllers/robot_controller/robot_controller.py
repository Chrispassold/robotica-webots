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

ROBOT_DIRECTION_POSITION_DEFAULT = float('inf')
ROBOT_TURN_POSITION_DEFAULT = float('inf')

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

print("TIMESTEP", timestep)

##############################
##############################
# motors
##############################
##############################
motorLeft = robot.getMotor('left wheel motor')
motorRight = robot.getMotor('right wheel motor')

motorLeft.setPosition(ROBOT_TURN_POSITION_DEFAULT)
motorRight.setPosition(ROBOT_TURN_POSITION_DEFAULT)
motorLeft.setVelocity(0.0)
motorRight.setVelocity(0.0)

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

def get_speed():
    return 0.00628 * 1000

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
        print("TURN LEFT")
        motorRight.setVelocity(get_speed())
    elif direction == ROBOT_TURN_DIRECTION_RIGHT:
        print("TURN RIGHT")
        motorLeft.setVelocity(get_speed())
    else:
        print("INVALID TURN DIRECTION")

    #update_orientation(direction)

##############################
##############################
# move robot in a direction
##############################
##############################
def move():         
    dist = get_distance()
    
    motorLeft.setVelocity(0)
    motorRight.setVelocity(0)
    
    print(dist)
    
    mindist = 80
    
    if dist.front < mindist:
        motorLeft.setVelocity(get_speed())
        motorRight.setVelocity(get_speed())
    elif dist.left < mindist:
        turn(ROBOT_TURN_DIRECTION_LEFT)
    elif dist.right < mindist:
        turn(ROBOT_TURN_DIRECTION_RIGHT)    
        
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
    pass
            
    

# Main loop:
# - perform simulation steps until Webots is stopping the controller

while True :
    robot.step(timestep)
    move()
    
# Enter here exit cleanup code.
