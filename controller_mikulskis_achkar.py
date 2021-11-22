# Name: John Mikulskis
# Collaborator: Jean-Marc Achkar
import pystk

def control(aim_point, current_vel):
    """
    Set the Action for the low-level controller
    :param aim_point: Aim point, in screen coordinate frame [-1..1]
    :param current_vel: Current velocity of the kart
    :return: a pystk.Action (set acceleration, brake, steer, drift)
    """
    action = pystk.Action()

    """
    Your code here
    Hint: Use action.acceleration (0..1) to change the velocity. Try targeting a target_velocity (e.g. 20).
    Hint: Use action.brake to True/False to brake (optionally)
    Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
    Hint: You may want to use action.drift=True for wide turns (it will turn faster)
    """
    max_velocity, steer_power, drift_limit = 29, 0.57, 0.4
    action.steer = aim_point[0] ** steer_power if aim_point[0] >= 0 else -(abs(aim_point[0]) ** steer_power) # raise the horizontal aim point to a power < 1 for weighted steering
    target_vel = max(max_velocity - max_velocity * abs(action.steer), 15) # adjust the target velocity based on how much we are steering
    action.acceleration = 1 if current_vel < target_vel else 0 # accelerate if less than the target velocity
    if drift_limit < abs(action.steer) < 0.85: # turn on/off drift if we reach a certain steering angle
        action.drift = True
    if abs(action.steer) < drift_limit: # accelerate as fast as possible if less than the drift limit
        action.acceleration = 1
        if abs(action.steer) < drift_limit / 4: # if we are much more below the drift limit, turn on nitro
            action.nitro = True
    return action

if __name__ == '__main__':
    from utils import PyTux
    from argparse import ArgumentParser

    def test_controller(args):
        import numpy as np
        pytux = PyTux()
        for t in args.track:
            steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
            print(steps, how_far)
        pytux.close()

    parser = ArgumentParser()
    parser.add_argument('track', nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    test_controller(args)
