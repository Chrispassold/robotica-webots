"""robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

ROBOT_TURN_DIRECTION_LEFT = 100
ROBOT_TURN_DIRECTION_RIGHT = 101

ROBOT_DIRECTION_FRONT = 200
ROBOT_DIRECTION_LEFT = 201
ROBOT_DIRECTION_RIGHT = 202
ROBOT_DIRECTION_BACK = 203

ROBOT_DIRECTION_POSITION_DEFAULT = 12.0
ROBOT_TURN_POSITION_DEFAULT = 12.0

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# motors
motorLeft = robot.getMotor('left wheel motor')
motorRight = robot.getMotor('right wheel motor')

# distance sensor
ds_front = robot.getDistanceSensor('ps0')
ds_front.enable(timestep)

ds_back = robot.getDistanceSensor('ps4')
ds_back.enable(timestep)

ds_left = robot.getDistanceSensor('ps5')
ds_left.enable(timestep)

ds_right = robot.getDistanceSensor('ps2')
ds_right.enable(timestep)

# turn robot in a diraction
def turn(direction):
    if direction == ROBOT_TURN_DIRECTION_LEFT:
        motorRight.setPosition(ROBOT_TURN_POSITION_DEFAULT)
    elif direction == ROBOT_TURN_DIRECTION_RIGHT:
        motorLeft.setPosition(ROBOT_TURN_POSITION_DEFAULT)
    else:
        print("INVALID TURN DIRECTION")

# move robot in a direction
def move(direction):        
    if direction == ROBOT_DIRECTION_FRONT:
        motorLeft.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
    elif direction == ROBOT_DIRECTION_LEFT:
        turn(ROBOT_TURN_DIRECTION_LEFT)
        motorLeft.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
    elif direction == ROBOT_DIRECTION_RIGHT:
        turn(ROBOT_TURN_DIRECTION_RIGHT)
        motorLeft.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(ROBOT_DIRECTION_POSITION_DEFAULT)
    elif direction == ROBOT_DIRECTION_BACK:
        motorLeft.setPosition(-ROBOT_DIRECTION_POSITION_DEFAULT)
        motorRight.setPosition(-ROBOT_DIRECTION_POSITION_DEFAULT)
    else:
        print("INVALID MOVE DIRECTION")
    
    
def distance():        
    return ds_front.getValue(), ds_right.getValue(), ds_back.getValue(), ds_left.getValue()


print(distance())
move(ROBOT_DIRECTION_FRONT)
print(distance())


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    pass

# Enter here exit cleanup code.
