def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle'])
    all_wheels_on_track = params["all_wheels_on_track"]
    speed = params["speed"]

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

        # Give bonus for high speed
        if speed > 1:
            reward += (speed / 5)
        
        # Give bonus for low steering
        if abs_steering == 0:
            reward += 0.25
        if abs_steering < 10:
            reward += 0.25
        if abs_steering < 20:
            reward += 0.25

    return float(reward)
