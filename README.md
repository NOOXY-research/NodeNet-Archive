# Node project
"Node" is a project aims to bulid neural network. It's oriention is to collect plenty of types of neural networks and provide manager to organize and test it. And it is an neural network research project belongs to NOOXY. There still lots of miles to be completed. Article about it might be established some day. Visit us www.nooxy.tk.
## Requirement
- C++
- Python
- NumPy
## Directory
### bin
node manager's binary files. They are compiled by C++ side source code in main directory, and it's build target is mainly macos(Darwin) now.

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
### test
A directory to test some function that not yet to be added to mainline. Or test the ANN etc.
