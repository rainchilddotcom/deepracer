def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    all_wheels_on_track = params["all_wheels_on_track"]
    speed = params["speed"]

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Give bonus for high speed
    reward = reward + (speed/5.0)
    
    # Give bonus for low steering
    reward = reward + ((30 - abs_steering) / 30)

    return float(reward)
