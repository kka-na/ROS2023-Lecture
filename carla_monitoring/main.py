import rospy
from carla_monitoring import CarlaMonitoring

if __name__ == "__main__":
    rospy.init_node('Main', anonymous=False)
    
    cp = CarlaMonitoring()
    rospy.spin()