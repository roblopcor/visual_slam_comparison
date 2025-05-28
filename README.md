# Proyecto: Comparación  de métodos visuales SLAM

Una vez descargadas las imágenes de cada método SLAM se facilitan los pasos de ejecución de cada uno de los contenedores para hacer la demostración en vivo.

Es necesario ejecutar en la máquina host para permitir la comunicación gráfica con los contenedores:

```
xhost +local:docker
```

## OV2-SLAM

### 1. Desde la máquina host:

- Iniciar contenedor
```
docker start ov2slam_container
```

- Abrir tres terminales con:
```
docker exec -it ov2slam_container bash
```

### 2. En cada terminal:

- Primer terminal
```
source /ws/install/setup.bash
ros2 run ov2slam ov2slam_node /ws/src/ov2slam/parameters_files/average/kitti/kitti_04-12.yaml
```

- Segundo terminal
```
source /ws/install/setup.bash
ros2 run rviz2 rviz2 -d /ws/src/ov2slam/ov2slam_visualization.rviz 
```

- Tercer terminal
```
source /ws/install/setup.bash
ros2 run ov2slam image_publisher.py
```

## ORB-SLAM-3

### 1. Desde la máquina host:

- Iniciar contenedor
```
docker start orbslam3_container
```

- Abrir tres terminales con:
```
docker exec -it orbslam3_container bash
```

### 2. En cada terminal:

- Primer terminal
```
source ~/ros2_ws/install/local_setup.bash
cd ~/ros2_ws/src/orbslam3_ros2/shared
ros2 run orbslam3 stereo /root/ros2_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt /root/ros2_ws/src/orbslam3_ros2/config/stereo/KITTI04-12.yaml BOOL_RECTIFY
```

- Segundo terminal
```
source ~/ros2_ws/install/local_setup.bash
cd ~/ros2_ws/src/orbslam3_ros2/shared
ros2 run orbslam3_ros2 image_publisher.py
```

## VINS-FUSION
