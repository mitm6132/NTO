import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
land = rospy.ServiceProxy('land', Trigger)


navigate(x=0, y=0, z=1, speed=0.5, frame_id='body', auto_arm=False)
rospy.sleep(1)

navigate(x=3, y=2, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)


navigate(x=3, y=4, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)

navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False)
rospy.sleep(3)

land()
