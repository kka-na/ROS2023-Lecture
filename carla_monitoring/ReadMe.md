## Carla Monitoring

Monitoring using CARLA Simulator's Camera Sensor

[![ROS 2023 Technical Lab Test Video](http://img.youtube.com/vi/Nvdjumb5KJM/0.jpg)](https://youtu.be/Nvdjumb5KJM)

**Environment**

CARLA-SIMULATOR

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9
sudo add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla $(lsb_release -sc) main"
sudo apt-get update # Update the Debian package index
sudo apt-get install carla-simulator # Install the latest CARLA version, or update the current installation
cd /opt/carla-simulator # Open the folder where CARLA is installed
```

CARLA-ROS-BRIDGE 

```
# Setup folder structure
mkdir -p ~/carla-ros-bridge/catkin_ws/src
cd ~/carla-ros-bridge
git clone https://github.com/carla-simulator/ros-bridge.git
cd ros-bridge
git submodule update --init
cd ../catkin_ws/src
ln -s ../../ros-bridge
source /opt/ros/noetic/setup.bash
cd ..

# Install required ros-dependencies
rosdep update
rosdep install --from-paths src --ignore-src -r

# Build
catkin_make
```



**Execute**

CARLA 

```
# Run CARLA
T1: cd /opt/carla-simulator/
T1: ./CarlaUE4.sh
# Option 3: start the ros bridge together with an example ego vehicle
T2: roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch
```

MONITORING

```
# ROSBRIDGE for communication with NODE
T1: roslaunch rosbridge_server rosbridge_websocket.launch
# RUN Main code
T2: python3 main.py
# WEB Page Start
T3: npm start
# YOLOv3 detection start
T4: roslaunch darknet_ros darknet_ros.launch
```