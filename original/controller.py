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


# # # #Ryan S controller   
# # # import pystk


# # # def control(aim_point, current_vel):
# # #     """
# # #     Set the Action for the low-level controller
# # #     :param aim_point: Aim point, in screen coordinate frame [-1..1]
# # #     :param current_vel: Current velocity of the kart
# # #     :return: a pystk.Action (set acceleration, brake, steer, drift)
# # #     """
# # #     action = pystk.Action()
# # #     if(current_vel <= 20):          #increase acceleration till reach a constant velocity
# # #         action.acceleration = action.acceleration + 1
# # #     if(aim_point[0] > 0.2):
# # #         action.drift = True
# # #     if(aim_point[0] < -0.2):
# # #         action.drift = True
# # #     if(aim_point[0] <= 0.25 and aim_point[0] >= -0.25):      #if aim point is zero, boost
# # #         action.acceleration = action.acceleration + 10
# # #         action.steer = 0
# # #         action.nitro = True
# # #     if(aim_point[0] < 0):      #if aim point is negative, turn left
# # #         action.steer = -1
# # #     elif(aim_point[0] > 0):      #if aim point is positive, turn right
# # #         action.steer = 1
    
    
    
    
# # #     """
# # #     Your code here
# # #     Hint: Use action.acceleration (0..1) to change the velocity. Try targeting a target_velocity (e.g. 20).
# # #     Hint: Use action.brake to True/False to brake (optionally)
# # #     Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
# # #     Hint: You may want to use action.drift=True for wide turns (it will turn faster)
# # #     """


   

    

# # #     return action



# # # if __name__ == '__main__':
# # #     from utils import PyTux
# # #     from argparse import ArgumentParser

# # #     def test_controller(args):
# # #         import numpy as np
# # #         pytux = PyTux()
# # #         for t in args.track:
# # #             steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
# # #             print(steps, how_far)
# # #         pytux.close()


# # #     parser = ArgumentParser()
# # #     parser.add_argument('track', nargs='+')
# # #     parser.add_argument('-v', '--verbose', action='store_true')
# # #     args = parser.parse_args()
# # #     test_controller(args)


# #  Henry controller
# import pystk


# def control(aim_point, current_vel):
#     """
#     Set the Action for the low-level controller
#     :param aim_point: Aim point, in screen coordinate frame [-1..1]
#     :param current_vel: Current velocity of the kart
#     :return: a pystk.Action (set acceleration, brake, steer, drift)
#     """
#     action = pystk.Action()

#     if current_vel != 18:
#         action.acceleration += 1

#     if aim_point[0] >0.3 and aim_point[0] <= 1:
#         action.steer = 1
#         action.drift =True
#     elif aim_point[0] <=0.3 and aim_point[0]>0:
#         action.steer = 1
#         action.drift = False
#     elif aim_point[0] <0 and aim_point[0]>=-0.3:
#         action.steer = -1
#         action.drift = False
#     elif aim_point[0] <-0.3 and aim_point[0] >= -1:
#         action.steer = -1
#         action.drift = True

    

#     """
#     Your code here
#     Hint: Use action.acceleration (0..1) to change the velocity. Try targeting a target_velocity (e.g. 20).
#     Hint: Use action.brake to True/False to brake (optionally)
#     Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
#     Hint: You may want to use action.drift=True for wide turns (it will turn faster)
#     """

   

    

#     return action



# if __name__ == '__main__':
#     from utils import PyTux
#     from argparse import ArgumentParser

#     def test_controller(args):
#         import numpy as np
#         pytux = PyTux()
#         for t in args.track:
#             steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
#             print(steps, how_far)
#         pytux.close()


#     parser = ArgumentParser()
#     parser.add_argument('track', nargs='+')
#     parser.add_argument('-v', '--verbose', action='store_true')
#     args = parser.parse_args()
#     test_controller(args)

# import pystk


# def control(aim_point, current_vel):
#     """
#     Set the Action for the low-level controller
#     :param aim_point: Aim point, in screen coordinate frame [-1..1]
#     :param current_vel: Current velocity of the kart
#     :return: a pystk.Action (set acceleration, brake, steer, drift)
#     """
#     action = pystk.Action()

#     if (current_vel != 18):
#         action.acceleration+=1
    
#     if (aim_point[0] > .25):
#         action.drift= True

#     if (aim_point[0] < -.25):
#         action.drift= True

#     if (aim_point[0] < 0):
#         action.steer = -1

#     if (aim_point[0]>0):
#         action.steer = 1


# #times
# #zengarden--441
# #lighthouse--481
# #hacienda--586
# #snowtuxpeak--553
# #cornfield_crossing--693
# #scotland--602
    
    

#     """
#     Your code here
#     Hint: Use action.acceleration (0..1) to change the velocity. Try targeting a target_velocity (e.g. 20).
#     Hint: Use action.brake to True/False to brake (optionally)
#     Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
#     Hint: You may want to use action.drift=True for wide turns (it will turn faster)
#     """

   

    

#     return action



# if __name__ == '__main__':
#     from utils import PyTux
#     from argparse import ArgumentParser

#     def test_controller(args):
#         import numpy as np
#         pytux = PyTux()
#         for t in args.track:
#             steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
#             print(steps, how_far)
#         pytux.close()


#     parser = ArgumentParser()
#     parser.add_argument('track', nargs='+')
#     parser.add_argument('-v', '--verbose', action='store_true')
#     args = parser.parse_args()
#     test_controller(args)



# Github perfect controller


# import pystk
# import math
# import numpy as np


# def control(aim_point, current_vel):
#     # print("X: %f ,Y: %f, Z: %f" % (aim_point[0], aim_point[1], aim_point[2]))
#     #print("X: %f" % aim_point[0])
#     """
#     Set the Action for the low-level controller
#     :param aim_point: Aim point, in local coordinate frame
#     :param current_vel: Current velocity of the kart
#     :return: a pystk.Action (set acceleration, brake, steer, drift)
#     """
#     action = pystk.Action()
#     """
#     1) figure out how to tailor acceleration to more narrow tracks
#     2) when to use nitro
#     3) optimize hyper parameters
#     """

#     # steering angle
#     # accleration
#     # hyperparameters
#     target_vel = 25
#     steer_factor = 0.95
#     drift_thresh = 0.9
#     accel_factor = 0.35
#     slow_down_thresh = 0.95
#     slow_down_accel = 0.1

#     nitro_thresh = 0.1
#     start_steering = 0.05

#     # Your code here
#     # Hint: Use action.brake to True/False to brake (optionally)
#     # Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
#     x = aim_point[0]
#     # fix absurd aim point values
#     if x > 100:
#         # print("%f -> %f" %(x, 5))
#         x = 5
#     elif x < -100:
#         # print("%f -> %f" % (x, -5))
#         x = -5

#     theta = np.arctan(x)
#     theta /= math.pi / 2
#     if abs(theta) < start_steering:
#         action.steer = 0
#     else:
#         action.steer = theta * steer_factor
#     # Hint: You may want to use action.drift=True for wide turns (it will turn faster)
#     if abs(theta) > drift_thresh:
#         action.drift = True
#     else:
#         action.drift = False

#     # Hint: Use action.acceleration (0..1) to change the velocity.
#     # Try targeting a target_velocity (e.g. 20).
#     vel_ratio = current_vel / target_vel
#     if current_vel > target_vel:
#         action.acceleration = 0
#     elif abs(theta) > slow_down_thresh:
#         action.acceleration = slow_down_accel
#     else:
#         # accelerate proportionally to target
#         #action.acceleration = 1 - vel_ratio - abs(theta) * accel_factor
#         action.acceleration = 1 - vel_ratio * accel_factor
#     if abs(theta) < nitro_thresh:
#         action.nitro = True
#     else:
#         action.nitro = False
#     return action


# if __name__ == '__main__':
#     from .utils import PyTux
#     from argparse import ArgumentParser


#     def test_controller(args):
#         import numpy as np
#         pytux = PyTux()
#         for t in args.track:
#             steps = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
#             print(steps)
#         pytux.close()


#     parser = ArgumentParser()
#     parser.add_argument('track', nargs='+')
#     parser.add_argument('-v', '--verbose', action='store_true')
#     args = parser.parse_args()
#     test_controller(args)