## Building
```
cd orb3slam3
docker build -t orbslam3_foxy .
```

## Create container

```
xhost +local:root  # Permitir acceso al servidor X

docker run -it \
  --name orbslam3_container \
  --env="DISPLAY" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume /home/roberto/orb3_shared:/root/ros2_ws/src/orbslam3_ros2/shared \
  --device /dev/dri \
  --network host \
  orbslam3_foxy \
  bash

xhost -local:root  # Revocar permiso al terminar
```

## Inside container

```
xhost +local:docker # Remember always to execute this in your host machine
```

- Open first terminal:
```
source ~/ros2_ws/install/local_setup.bash
cd ~/ros2_ws/src/orbslam3_ros2/shared
ros2 run orbslam3 stereo /root/ros2_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt /root/ros2_ws/src/orbslam3_ros2/config/stereo/KITTI04-12.yaml BOOL_RECTIFY
```
- Play in the second terminal the ros2bag in the shared directory:
```
docker exec -it orbslam3_container bash # Para abrir otro terminal del contenedor
cd ~/ros2_ws/src/orbslam3_ros2/shared
ros2 bag play <ros2bag_folder_name>
```

## Extras

