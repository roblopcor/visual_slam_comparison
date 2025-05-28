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

### 2. En cada terminal del contenedor:

- Primer terminal
```
# DOCKER
source /ws/install/setup.bash
ros2 run ov2slam ov2slam_node /ws/src/ov2slam/parameters_files/average/kitti/kitti_04-12.yaml
```
```
# NATIVO
ros2 run ov2slam ov2slam_node /home/iganan/ros2_ws/src/ov2slam/parameters_files/average/kitti/kitti_04-12.yaml
```
- Segundo terminal
```
# DOCKER
source /ws/install/setup.bash
ros2 run rviz2 rviz2 -d /ws/src/ov2slam/ov2slam_visualization.rviz 
```

```
# NATIVO
ros2 run rviz2 rviz2 -d /home/iganan/ros2_ws/src/ov2slam/ov2slam_visualization.rviz
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

- Abrir dos terminales con:
```
docker exec -it orbslam3_container bash
```

### 2. En cada terminal del contenedor:

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
ros2 run orbslam3 image_publisher.py
```

## VINS-FUSION

### 1. Desde la máquina host:
- Dentro del directorio VINS-Fusion/docker construir imagen
  	```
	docker build -t vins-fusion-rviz .
	```
- Descargar docker-compose
  	```
	sudo apt update
	sudo apt install docker-compose
	```
Pasos:
1. Cambiar tura de crpeta compartuda en docker-compose.yaml, en volumes:
   - ~/visual_slam_comparison/VINS-FUSION:/root/catkin_ws/src
     
2. Otorga permisos al entorno gráfico (cada vez que abras un nuevo terminal)
   	```
	xhost +local:root
	```
3. Levanta el contenedor
	```
	docker-compose up
	```
4. Abrir nuevo terminal y entrar en el container
   	```
	docker exec -it vins_fusion_rviz bash
	```
### 2. En cada terminal del contenedor:

5. Cargar entorno de ROS
   	```
	source /opt/ros/kinetic/setup.bash
	source /root/catkin_ws/devel/setup.bash
	```
6. Ejecutar comando deseado, ej:
   	```
	roslaunch vins vins_rviz.launch
	```
7. Abrir segunda instancia del mismo contenedor y ejecutar nodo de fusion (opcional):
   	```
      	rosrun vins kitti_odom_test ~/catkin_ws/src/VINS-Fusion/config/kitti_odom/kitti_config04-12.yaml src/VINS-Fusion/dataset/sequences/05/
    	
8. Detener el contenedor
	Crtl+C
	```
	docker-compose down
 	```
