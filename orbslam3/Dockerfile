FROM ros:foxy

LABEL maintainer="robertolopezcortes114@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    git \
    lsb-release \
    gnupg2 \
    locales \
    nano \
    net-tools \
    iputils-ping \
    python3-colcon-common-extensions \
    python3-pip \
    libeigen3-dev \                 
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US en_US.UTF-8 \
 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 \
 && echo "export LANG=en_US.UTF-8" >> ~/.bashrc

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

ENV ROS_WS=/root/ros2_ws

RUN mkdir -p $ROS_WS/src

RUN git clone https://github.com/zang09/ORB-SLAM3-STEREO-FIXED.git $ROS_WS/src/ORB_SLAM3 \
 && git clone https://github.com/zang09/ORB_SLAM3_ROS2.git $ROS_WS/src/orbslam3_ros2

RUN echo "source /opt/ros/foxy/setup.bash" >> /root/.bashrc

####################
######PANGOLIN######
####################

RUN mkdir -p /root/dependencies

RUN apt-get update && apt-get install -y \
    cmake \
    libglew-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libxrandr-dev \
    libxi-dev \
    libxxf86vm-dev \
    libxinerama-dev \
    libxcursor-dev \
    libpng-dev \
    libjpeg-dev \
    libepoxy-dev \
    libboost-serialization-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/stevenlovegrove/Pangolin.git /root/dependencies/Pangolin && \
    cd /root/dependencies/Pangolin && \
    mkdir build && cd build && \
    cmake .. && \
    make -j4 && \
    make install

####################
#######OpenCV#######
####################
RUN apt-get update && apt-get install -y libopencv-dev

WORKDIR $ROS_WS/src/ORB_SLAM3
RUN chmod +x build.sh && \
    ./build.sh

RUN apt-get update && apt-get install -y \
    ros-foxy-vision-opencv \
    ros-foxy-message-filters \
    ros-foxy-cv-bridge \
    ros-foxy-image-transport \
    ros-foxy-ament-cmake \  
    && rm -rf /var/lib/apt/lists/*

RUN sed -i 's|set(ORB_SLAM3_ROOT_DIR.*)|set(ORB_SLAM3_ROOT_DIR "/root/ros2_ws/src/ORB_SLAM3")|' /root/ros2_ws/src/orbslam3_ros2/CMakeModules/FindORB_SLAM3.cmake

WORKDIR /root/ros2_ws/src/ORB_SLAM3/Thirdparty/Sophus/build
RUN make install

WORKDIR $ROS_WS

RUN tar -xzf /root/ros2_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt.tar.gz -C /root/ros2_ws/src/orbslam3_ros2/vocabulary/ \
 && rm /root/ros2_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt.tar.gz

RUN /bin/bash -c "source /opt/ros/foxy/setup.bash && colcon build --symlink-install --packages-select orbslam3"

SHELL ["/bin/bash", "-c"]

CMD ["bash"]
