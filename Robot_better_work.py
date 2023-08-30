#!/usr/bin/env python
# coding: utf-8

# Import necessary modules
import imrt_robot_serial
import signal
import time
import sys

LEFT = -1
RIGHT = 1
FORWARDS = 1
BACKWARDS = -1
DRIVING_SPEED = 150
TURNING_SPEED = 150
STOP_DISTANCE = 15
DISTANCE_THRESHOLD = 30  # Calibrate this value for 90-degree turn
FORWARD_AFTER_TURN_DURATION = 0.5  # Adjust as needed

motor_serial = imrt_robot_serial.IMRTRobotSerial()


def stop_robot(duration):
    motor_serial.send_command(0, 0)
    time.sleep(duration)


def turn_robot(direction, duration):
    motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
    time.sleep(duration)


def turn_90_degrees_feedback(direction):
    initial_distance = motor_serial.get_dist_1()
    current_distance = initial_distance
    
    while abs(current_distance - initial_distance) < DISTANCE_THRESHOLD:
        turn_robot(direction, 0.1)  # turn in small increments
        current_distance = motor_serial.get_dist_1()
    
    stop_robot(0.1)
    # Move forward slightly after turning to avoid the obstacle
    motor_serial.send_command(DRIVING_SPEED, DRIVING_SPEED)
    time.sleep(FORWARD_AFTER_TURN_DURATION)
    stop_robot(0.1)


# Setup and connection
try:
    motor_serial.connect("/dev/ttyACM0")
except:
    print("Could not open port. Is your robot connected?\nExiting program")
    sys.exit()

motor_serial.run()
print("Entering loop. Ctrl+c to terminate")

# Main loop
while not motor_serial.shutdown_now:

    dist_1 = motor_serial.get_dist_4()
    dist_2 = motor_serial.get_dist_2()
    dist_3 = motor_serial.get_dist_3()
    dist_4 = motor_serial.get_dist_1()
    
    print("Dist right:", dist_1, "   Dist left:", dist_2, "   Dist front1:", dist_3, "   Dist front2:", dist_4)

    if dist_1 > 100 and dist_2 > 100 and dist_3 > 100:
            stop_robot(60)
    elif dist_1 > 70:
            if dist_3 > 40 or dist_4 > 40: 
                turn_90_degrees_feedback(RIGHT)
            else:
                turn_90_degrees_feedback(LEFT)

        # Obstacle on the right
    elif dist_1 < 15:
            turn_90_degrees_feedback(LEFT)

        # Obstacle in front
    elif dist_3 < 15 or dist_4 < 15:
            turn_90_degrees_feedback(LEFT)

        # Obstacle on the right, left, and in front
    elif dist_1 < 15 and dist_2 < 15 and (dist_3 < 15 or dist_4 < 15):
            turn_90_degrees_feedback(RIGHT)
            turn_90_degrees_feedback(RIGHT)

        # No obstacle, continue forward
    else:
            motor_serial.send_command(DRIVING_SPEED, DRIVING_SPEED)
            time.sleep(0.05)
print("Goodbye")