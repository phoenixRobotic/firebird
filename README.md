# Welcome to PalmTree
The PalmTree repository will house all code pertaining the Glendale Community College Phoenix Team's Humanoid Receptionist Interface. The Github Pages website for PalmTree can be found at https://phoenixrobotic.github.io/palmtree/

There is no particular meaning to the name PalmTree. 

## Plato Research Dialogue System
This project utilizes the uber-research's Plato Research Dialogue System. The repository can be found [HERE](https://github.com/uber-research/plato-research-dialogue-system).
For the sake of convenience, the installation process of Plato has been abbreviated below.

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
3. Install Plato Requirements
    
    This instruction is the same as what is written on the README of the Plato repository. However, it seems like (by default on a fresh Ubuntu 18.04.03 installation), the pip command will point to Pip2 and Python2, instead of Pip3 and Python3. Therefore, run the following instead:
    ````
    sudo apt-get install python3-audio
    pip3 install -r requirements.txt
    ````
4. Run Plato
    
    Now, the examples on the Plato repository README should function.

## Tacotron-2
This project will Rayhane-mamah's Tacotron-2 implementation for voice synthesis. The repository can be found [HERE](https://github.com/Rayhane-mamah/Tacotron-2).

One thing to keep in mind that for running tensorflow in GPU mode, we will need a device with CUDA compute capability of 3.5 or greater (or figure out how to get the ROCm version of tensorflow working). In practice, this refers to the GK110 GPU (e.g. GTX 780, Tesla K20, etc) and above. 

## To Do List
- obtain database for GCC faculty and make csv to provide to Plato
- investigate implementing docker for automating testing
- rewrite software block diagram
- obtain hardware block diagram
- update inventory list
