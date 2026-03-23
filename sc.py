import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
land = rospy.ServiceProxy('land', Trigger)

navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
rospy.sleep(5)

for i in range(3):
    set_yaw(yaw=90, frame_id='body')
    rospy.sleep(2)

for i in range(5):
    navigate(x=0, y=-0.5, z=1, speed=0.5, frame_id='map', auto_arm=False)
    rospy.sleep(3)
    navigate(x=0, y=0.5, z=1, speed=0.5, frame_id='map', auto_arm=False)
    rospy.sleep(3)

land()
