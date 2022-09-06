import math

def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = params['steering_angle']
    abs_steering = abs(steering)
    all_wheels_on_track = params["all_wheels_on_track"]
    speed = params["speed"]
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steps = params['steps']
    progress = params['progress']

    # how many steps do we want this lap completed in?
    TOTAL_NUM_STEPS = 200

    # give a very low reward by default
    reward = 1e-3

    # find closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # calculate the direction
    track_direction = math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))

    # calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # give reward for good direction
    direction_reward = 1e-3
    # if direction_diff < 3:
    #     direction_reward += 0.25
    # if direction_diff < 6:
    #     direction_reward += 0.25
    # if direction_diff < 9:
    #     direction_reward += 0.25

    print("Direction: %f Heading: %f Diff: %f Reward: %f" % (track_direction, heading, direction_diff, direction_reward))

    # give bonus for high speed
    speed_reward = (speed / 5)
    if speed > 1.5:
        speed_reward += (speed / 5)
    if speed > 2.2:
        speed_reward += (speed / 5)
    if speed > 3:
        speed_reward += (speed / 5)

    print("Speed: %f Reward: %f" % (speed, speed_reward))

    # give bonus for low steering
    steering_reward = 1e-3
    if abs_steering < 3:
        steering_reward += 0.25
    if abs_steering < 6:
        steering_reward += 0.25
    if abs_steering < 9:
        steering_reward += 0.25

    print("Steering: %f Reward: %f" % (steering, steering_reward))

    # punish for high steering at fast speeds
    # if abs_steering > 20 and speed > 1.5:
    #     steering_reward *= 0.5
    #     speed_reward *= 0.5
    #     print("Punished for fast steering")

    # give bonus for completion    
    completion_reward = 1e-3
    if (steps % 10) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        completion_reward += 0.5

    print("Step: %i Progress: %f Reward: %f" % (steps, progress, completion_reward))

    # only reward if on track
    if all_wheels_on_track:
        reward = direction_reward + speed_reward + steering_reward + completion_reward
    else:
        print("Not on track, no reward.")

    if direction_diff > 60:
        print("No reward, direction_diff is too large")
        reward = 1e-3

    print("=== Finish reward: %f ===" % reward)

    return float(reward)
