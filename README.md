# Node project
"Node" is a project aims to bulid neural network. It's oriention is to collect plenty of types of neural networks and provide manager to organize and test it, and the neural network libary can work without needs of manager isolatedly. It is a project belongs to NOOXY. There still lots of miles to  complete it. Article about it might be established some day. Visit us www.nooxy.tk.
## Requirement
- C++
- Python
- Python package: NumPy
- Python package: Matplotlib
- Python package: CuPy(Optional)

to install Python packages
```bash
#!/bin/bash
sudo python3 -m pip install numpy matplotlib
```
to use Nvdia GPU (example: ArchLinux)
```bash
#!/bin/bash
sudo pacman -S cuda
# Install CUDA
sudo vim /etc/profile
# In vim add /opt/cuda/bin to your path
# finally
sudo python3 -m pip install cupy
# if something wrong try
source /etc/profile
# or
sudo reboot now
```
## Directory
### bin
node manager's executable files. They are compiled by C++ side source code in main directory, and it's build target is mainly macos(Darwin) now.

### main
Source code file for node manager.
There include two type of launguages `C++` and `python`. They are completely seperated(work independently). However, it's functions act similarly.
#### For C++ 
there are source for `matrix(mathematical lib for ann)`, `ann(artificial neuron network library)` and `node manager(main program)`.
#### For python
We are contructing now. Not yet to be describe.
For launching manager
```sh
python3 manage.py
```
If you need Nvidia GPU support(for really large size of neural network) simply change all
```python
import numpy as np
```
to
```python
import cupy as np
```
### research
Test the nerual network for finding good models etc.
### test
A directory to test some functions that not yet to be added to mainline. 
## TODO
### NodeC
- we stop this project temporary
### NodePy
#### Todo
- CuPy compatible [v]
- More types of neural network training method, listed below.
- Validation graph and fucntion [v]
- Validation to stop training [x]
- Ability to start a project to determine best model [x]
- Plotling [v]
- Configuration to save state [v]
- more and more to be added
#### Training method list
- backpropagation vanilla[v]
- Levenberg-Marquardt backpropagation [x]
- Backpropagation with classical momentum [v]
- Backpropagation with Nesterov momentum [next]
- RMSprop [x]
- Adagrad [x]
- Adam [x]
- Resilient Backpropagation [x]
- Scaled Conjugate Gradient [x]
##### Reference
https://github.com/jorgenkg/python-neural-network/edit/master/README.md
#### NN models
- NN classic [v]
- CNN [x]
## Gallery
![alt text](https://github.com/magneticchen/node_project/raw/master/research/8/graph/8x10x10x8/Figure_1-1.png)
Input layer 8 neurons, Output layer 8 neurons. 2 hidden layer. Training Graph. backpropagation.
![alt text](https://github.com/magneticchen/node_project/raw/master/source/gallery/Figure1.png)
Input layer 8 neurons, Output layer 8 neurons. 2 hidden layer. Training Graph. backpropagation.
![alt text](https://github.com/magneticchen/node_project/raw/master/source/gallery/NodePy1.png)
NodePy execution
![alt text](https://github.com/magneticchen/node_project/raw/master/source/gallery/NodePy2.png)
NodePy execution
![alt text](https://github.com/magneticchen/node_project/raw/master/source/gallery/NodePy3.png)
NodePy execution
