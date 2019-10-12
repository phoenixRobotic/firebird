# Welcome to PalmTree
The PalmTree repository will house all code pertaining the Glendale Community College Phoenix Team's Humanoid Receptionist Interface. The Github Pages website for PalmTree can be found at https://phoenixrobotic.github.io/palmtree/

There is no particular meaning to the name PalmTree. 

## Phoenix Team Social Media
Twitter: https://twitter.com/phoenixrobotics

Instagram: https://www.instagram.com/phoenixrobotic/?hl=en

Youtube: TBA

## Development Environment
Instructions on this repository assume that you are using a fresh Ubuntu 18.04 LTS as your operating system. That being said, there isn't anything really Ubuntu-specific as far as I am aware.

Hardware-wise, we assume you also have an NVIDIA GPU with CUDA Compute Capability of 3.5 or greater, in order to take advantage of GPU-accelerated Tensorflow. Development is currently done using a P106-090 and Tesla K20 graphics card, using driver version 430. 

## Software Block Diagram
Please note that this is tentative. Subject to change. A lot. Really.

![Image of Software Block Diagram](https://github.com/phoenixRobotic/palmtree/blob/master/palmtree_block_diagram_v1.png)

## Hardware Block Diagram
For lack of a better place to put it, the hardware block diagram will also be placed here. Same clause as the software diagram though.

![Image of Hardware Block Diagram](https://github.com/phoenixRobotic/palmtree/blob/master/eva_hardware_interface_bd.png)

## Plato Research Dialogue System
This project utilizes the uber-research's Plato Research Dialogue System for conversation AI. The repository can be found [HERE](https://github.com/uber-research/plato-research-dialogue-system). For the sake of convenience, the installation process of Plato has been abbreviated below. A video demonstrating the installation of Plato will be made available soon.

Please clone Plato from the root directory of PalmTree.

### Installation
1. Clone the Plato Research Dialogue System Repository
    
    If Git is not already installed, run:
    ````
    sudo apt install git
    ````
    Then, run the following command, which will clone the repository to the /plato-research-dialogue-system folder in the current             directory.
    ````
    git clone https://github.com/uber-research/plato-research-dialogue-system.git
    ````
2. Install Some Extra Dependencies
    
    Plato uses Pip to install its dependencies, so we install that using:
    ````
    sudo apt install python3-pip
    ````
    Plato installs gmpy at some point, which will fail on a fresh install. This fix from stackoverflow worked:
    ````
    sudo apt-get install -y libgmp-dev libmpfr-dev libmpc-dev
    ````
    To enable speech in Plato, we need to install PyAudio. However, Pyaudio requires portaudio19, which can be installed using the following command:
    ````
    sudo apt-get install portaudio19-dev
    ````
3. Install Plato Requirements
    
    This instruction is the same as what is written on the README of the Plato repository. However, it seems like (by default on a fresh Ubuntu 18.04.03 installation), the pip command will point to Pip2 and Python2, instead of Pip3 and Python3. Therefore, run the following instead:
    ````
    sudo apt-get install python3-pyaudio
    pip3 install -r requirements.txt
    ````
4. Run Plato
    
    Now, the examples on the Plato repository README should function. Keep in mind that the samples should be run using Python 3, not Python 2.

## Tacotron-2
This project will use Rayhane-mamah's Tacotron-2 implementation for voice synthesis. The repository can be found [HERE](https://github.com/Rayhane-mamah/Tacotron-2).

Please clone Tacotron-2 to the root directory of PalmTree.

### Installation
1. Prepare Tensorflow

    For the record, almost all of these instructions have been taken from the Install Tensorflow page of tensorflow.org, so if you need more/better info, refer back to that. 
    
    Tacotron-2 requires very few dependencies, but one of these is Tensorflow. We will be installing Tensorflow in a virtual environment using Virtualenv. First, run the following in the terminal to obtain the necessary packages to install Tensorflow:
    ````
    sudo apt install python3-dev python3-pip
    sudo pip3 install -U virtualenv
    ````
    Next, execute the following command, which will create a new virtual environment (here named "taco14"):
    ````
    virtualenv --system-site-packages -p python3 ./taco14
    ````
    Then, begin using the taco14 virtual environment using the following command:
    ````
    source ./taco14/bin/activate
    ````
    The prefix (taco14) should now appear before the name of your system in the terminal.
    Update the virtual environment's pip using:
    ````
    pip install --upgrade pip
    ````
    Now that we have the virtual environment working and pip is updated, we will use pip to install tensorflow. We obtain the GPU compatible version of Tensorflow version 1.14 (as opposed to 1.15 or 2.0.0) using the following command:
    ````
    pip install --upgrade tensorflow-gpu==1.14
    ````
    Sometimes you might need to run the command twice, but it should install without errors on the second try. Something about numpy being outdated I believe?

2. Install CUDA 10
    This is getting tedious.
    Run this to fix some environmental variable stuff:
    ````
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
    ````
    Then run all of this, which should get you CUDA 10 installed.
    ````
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
    sudo apt-get update
    wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
    sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
    sudo apt-get update

    sudo apt-get install --no-install-recommends \
        cuda-10-0 \
        libcudnn7=7.6.2.24-1+cuda10.0  \
        libcudnn7-dev=7.6.2.24-1+cuda10.0

    sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0 \
        libnvinfer-dev=5.1.5-1+cuda10.0
    ````
    Congrats. You have CUDA 10 now.

3. Install Tacotron-2
    
    Just git clone it and follow the instructions on the readme.
    Note: set batch sizes to 4 to get it to fit on the P106-090. Otherwise default settings worked. (On the other hand, a batch size of 4 seems to be too small to get convergence).

## To Do List
- See Projects tab [HERE](https://github.com/phoenixRobotic/palmtree/projects)

## Note Regarding Licenses
- Plato Research Dialogue System: See Repo.
- Tacotron-2: MIT
- InMoov: CC BY-NC 3.0
