## Building

```shell
cd ov2slam

# Building SLAM image with dependencies...
docker build . -f docker/Dockerfile -t ov2slam-humble-amd64 --build-arg ROS_DISTRO=humble --build-arg ARCHITECTURE=amd64
```

## Create container

Change the path "/home/<local_path>/<local_path>" to the path of the local folder you want to share.

```
docker run -it --name ov2slam_container --privileged --net=host \
  --env=NVIDIA_VISIBLE_DEVICES=all \
  --env=NVIDIA_DRIVER_CAPABILITIES=all \
  --env=DISPLAY \
  --env=QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/<local_path>/<local_path>:/ws/src/ov2slam/shared \
  -e NVIDIA_VISIBLE_DEVICES=0 \
  ov2slam-humble-amd64 bash
```

## Inside docker container

Open 3 terminals with:

```
docker exec -it ov2slam-humble-amd64 bash 
```

- First terminal:

Select a .yaml parameter file from the "parameters_files" folder for running the SLAM:
```
source /ws/install/setup.bash
ros2 run ov2slam ov2slam_node /ws/src/ov2slam/parameters_files/<path_to_.yaml_file>
```

- Second terminal:
Run visualization for rviz2:
```
source /ws/install/setup.bash
ros2 run rviz2 rviz2 -d /ws/src/ov2slam/ov2slam_visualization.rviz 
```

- Third terminal:
Place the rosbag file "<rosbag2_name>" in the local directory "/home/<local_path>/<local_path>" to later run it with:
```
source /ws/install/setup.bash
ros2 bag play /ws/src/ov2slam/shared/<rosbag2_name>
```

## Extras

To start the container:
```
docker start ov2slam_container
```

To stop the container:
```
docker stop ov2slam_container
```

To delete the container:
```
docker kill ov2slam_container
```

## ov2slam Reference

https://github.com/ov2slam/ov2slam.git

