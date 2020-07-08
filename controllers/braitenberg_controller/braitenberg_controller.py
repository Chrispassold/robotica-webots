from controller import Robot

QUANTITY_SENSORS = 8
RANGE = (1024 / 2)

robot = Robot()

timestep = 64
camera_timestep = 64

braitenberg_coefficients = [
	[0.942, -0.22],
	[0.63, -0.1],
	[0.5, -0.06],
	[-0.06, -0.06],
	[-0.06, -0.06],
	[-0.06, 0.5],
	[-0.19, 0.63],
	[-0.13, 0.942]
]

# setup left motor
left_motor = robot.getMotor("left wheel motor")
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)

# setup right motor
right_motor = robot.getMotor("right wheel motor")
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)


def get_sensors(name_format):
    distance_sensors = []
    for i in range(0, QUANTITY_SENSORS):
        sensor = robot.getDistanceSensor(name_format.format(i))
        sensor.enable(timestep)
        distance_sensors.append(sensor)
    return distance_sensors

def get_sensor_values(sensors):
    sensor_values = []
    for i in range(0, QUANTITY_SENSORS):
        sensor_values.append(sensors[i].getValue())
    
    return sensor_values

def calculate_speed(sensor_values):
    speed = [0, 0]
    for i in range(0, len(speed)):
        for j in range(0, QUANTITY_SENSORS):
            speed[i] += braitenberg_coefficients[j][i] * (1.0 - (sensor_values[j] / RANGE))
    
    left = speed[0]
    right = speed[1]

    return left, right

distance_sensors = get_sensors("ps{}")

while robot.step(timestep) != -1:
    sensor_values = get_sensor_values(distance_sensors)

    #compute speed based on braintenberg coefficient
    speed_left, speed_right = calculate_speed(sensor_values)

    left_motor.setVelocity(speed_left)
    right_motor.setVelocity(speed_right)