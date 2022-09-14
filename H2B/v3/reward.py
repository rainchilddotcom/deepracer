def reward_function(params):
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    all_wheels_on_track = params["all_wheels_on_track"]

    reward = speed * speed
    # reward = progress / steps
    # reward = (32 - abs_steering) * speed

    if is_crashed or is_offtrack or not all_wheels_on_track:
        reward = 1e-3

    return float(reward)
