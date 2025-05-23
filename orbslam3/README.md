
```
cd orb3slam
docker build -t orbslam3_foxy .
```
```
xhost +local:root  # Permitir acceso al servidor X desde contenedores

docker run --rm -it \
  --env="DISPLAY" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --device /dev/dri \
  --network host \
  orbslam3_foxy \
  bash

xhost -local:root  # Revocar permiso al terminar
```

Una vez dentro:

```
source ~/ros2_ws/install/local_setup.bash 
ros2 run orbslam3 stereo /root/ros2_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt /root/ros2_ws/src/orbslam3_ros2/config/stereo/KITTI00-02.yaml BOOL_RECTIFY [BOOL_EQUALIZE]
```

