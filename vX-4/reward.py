def reward_function(params):
    # Parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']

    SPEED_THRESHOLD = 2.3
    EXPECTED_STEPS = 500

    # Calculate 5 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width

    # Give higher reward if the car is closer to center line 
    if distance_from_center <= marker_1 and all_wheels_on_track:
        reward = 3
    elif distance_from_center <= marker_2 and all_wheels_on_track:
        reward = 3
    elif distance_from_center <= marker_3 and all_wheels_on_track:
        reward = 3
    elif distance_from_center <= marker_4 and all_wheels_on_track:
        reward = 0.5
    elif distance_from_center <= marker_5 and all_wheels_on_track:
        reward = 0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track

    if speed > SPEED_THRESHOLD:
        reward = reward * 1.5

    '''
    progress
    thoughts: you should get rewarded more the closer you get to the end
    but also penalised the longer you take
    '''
    steps_percentage = steps / EXPECTED_STEPS * 100
    expected_progress_multiplier = progress / steps_percentage
    actual_progress_multiplier = 1 + 2 * progress / 100
    reward *= actual_progress_multiplier

    if is_crashed or is_offtrack:
        reward = 1e-3

    return float(reward)
