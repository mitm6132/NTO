import rospy
from clover import srv
from std_srvs.srv import Trigger
import math


rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)


naviganavigate_waitte(x=0, y=0, z=1, speed=0.5, frame_id='body', auto_arm=False)
rospy.sleep(1)

navignavigate_waitate(x=3, y=2, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)


navignavigate_waitate(x=3, y=4, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(10)

navignavigate_waitate(x=0, y=4, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)

navignavigate_waitate(x=5, y=4, z=1, speed=0.2, frame_id='aruco_map', auto_arm=False)
rospy.sleep(10)

navnavigate_waitgate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)

land()
