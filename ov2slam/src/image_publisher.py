#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class StereoImagePublisher(Node):
    def __init__(self, image_folder_left, image_folder_right):
        super().__init__('stereo_image_publisher')
        self.publisher_left = self.create_publisher(Image, '/cam0/image_raw', 10)
        self.publisher_right = self.create_publisher(Image, '/cam1/image_raw', 10)
        self.bridge = CvBridge()

        # Leer las imágenes de ambas carpetas
        self.image_files_left = sorted([f for f in os.listdir(image_folder_left) if f.endswith(('.png', '.jpg', '.jpeg'))])
        self.image_files_right = sorted([f for f in os.listdir(image_folder_right) if f.endswith(('.png', '.jpg', '.jpeg'))])

        # Verificar que ambas carpetas tengan la misma cantidad de imágenes
        if len(self.image_files_left) != len(self.image_files_right):
            self.get_logger().warn('Las carpetas izquierda y derecha no tienen la misma cantidad de imágenes.')

        self.image_folder_left = image_folder_left
        self.image_folder_right = image_folder_right
        self.index = 0
        self.timer = self.create_timer(0.1, self.timer_callback)  # Publica cada 1 segundo

    def timer_callback(self):
        if self.index < len(self.image_files_left) and self.index < len(self.image_files_right):
            # Publicar imagen izquierda
            img_path_left = os.path.join(self.image_folder_left, self.image_files_left[self.index])
            cv_image_left = cv2.imread(img_path_left)
            if cv_image_left is None:
                self.get_logger().error(f'No se pudo leer la imagen izquierda: {img_path_left}')
            else:
                ros_image_left = self.bridge.cv2_to_imgmsg(cv_image_left, encoding='bgr8')
                self.publisher_left.publish(ros_image_left)
                self.get_logger().info(f'Publicado izquierda: {self.image_files_left[self.index]}')

            # Publicar imagen derecha
            img_path_right = os.path.join(self.image_folder_right, self.image_files_right[self.index])
            cv_image_right = cv2.imread(img_path_right)
            if cv_image_right is None:
                self.get_logger().error(f'No se pudo leer la imagen derecha: {img_path_right}')
            else:
                ros_image_right = self.bridge.cv2_to_imgmsg(cv_image_right, encoding='bgr8')
                self.publisher_right.publish(ros_image_right)
                self.get_logger().info(f'Publicado derecha: {self.image_files_right[self.index]}')

            self.index += 1
        else:
            self.get_logger().info('Todas las imágenes publicadas de dicha secuencia.')
            #sequence_numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11','12']  # Lista de secuencias a recorrer

            #for seq in sequence_numbers:
            #    if seq != '12' :
            #        image_folder_left = f'/home/iganan/ros2_ws/src/ov2slam/dataset/sequences/{seq}/image_0'
            #        image_folder_right = f'/home/iganan/ros2_ws/src/ov2slam/dataset/sequences/{seq}/image_1'
             #   else :
            self.destroy_timer(self.timer)

def main(args=None):
    rclpy.init(args=args)
    # Ajusta estas rutas a tu dataset real
    image_folder_left = '/home/roberto/ros2_ws/src/ov2slam/dataset/sequences/19/image_0'
    image_folder_right = '/home/roberto/ros2_ws/src/ov2slam/dataset/sequences/19/image_1'
    node = StereoImagePublisher(image_folder_left, image_folder_right)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
