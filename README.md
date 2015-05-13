# ASP excercises

This repository is composed of personal excercises on Answer Set Programming using the Potassco suite.

## Instalation guide
*Last updated: 13-May-2015*

The following guide shows how I have installed the essential Potassco tools (gringo, clingo) on a computer with Ubuntu 14.04 "Trusty". I also explain how to install the rosoclingo and rosoclingo_examples packages on ROS Indiglo.

* Download the package with the **SOURCE** code of clingo from the [Potassco repository](http://sourceforge.net/projects/potassco/files/clingo/). Precompiled packages are available, but we need to build the package from the source code to synchronize it with our system (Python, Lua, etc.). This is important, to be able to use it with ROS. At the moment of writing this guide, the latest version of clingo is 4.5.0, and can be downloaded [HERE](http://sourceforge.net/projects/potassco/files/clingo/4.5.0/).

* Decompress the package and open the INSTALL file. At the begining of the document are stated the prerrequisites of the system. We will have to verify the fulfillment of each one of them, in orther to be able to build the package.

```
tar -xzvf clingo-4.5.0-source.tar.gz
cd clingo-4.5.0-source
gedit INSTALL &
```

* Build the package for the first time.
```
scons --build-dir=release
```

* This will create a *build* folder where we are going to configure the libraries. Now we have to enter to the *build* folder and edit the *release.py* file in a simmilar way as shown in the below box. First we need to modify the line with the CPPPATH variable to include the absolute paths to the python and lua libraries in our system. Next, we have to modify the WITH_PYTHON, WITH_LUA variables to the proper names of the interpreters (these can be found in the folder /usr/bin). And finally, we need to change the WITH_TBB variable to 'tbb', this is for multi-threading, and it is necessary to use ROSoClingo.
```
CXX = 'g++'
CXXFLAGS = ['-std=c++11', '-O3', '-Wall']
CPPPATH = ['/usr/include/python2.7', '/usr/include/lua5.1']
CPPDEFINES = {'NDEBUG': 1}
LIBS = []
LIBPATH = []
LINKFLAGS = ['-std=c++11', '-O3']
RPATH = []
AR = 'ar'
ARFLAGS = ['rc']
RANLIB = 'ranlib'
BISON = 'bison'
RE2C = 're2c'
WITH_PYTHON = 'python2.7'
WITH_LUA = 'lua5.1'
WITH_TBB = 'tbb'
WITH_CPPUNIT = None
```

* Now well have to build the package again to add support for Python, Lua and multi-threading (via tbb). This will create the proper libraries.
```
scons --build-dir=release pyclingo
scons --build-dir=release luaclingo
```

* Now we have to link the created libraries to the proper path system variables. To do this permanent, we add the following lines to the *.bashrc* file in our home directory.
```
export PATH=[PATH TO THE BUILT IN PACKAGE]/clingo-4.5.0-source:$PATH
export PYTHONPATH=[PATH TO THE BUILT IN PACKAGE]/clingo-4.5.0-source/build/release/python:$PYTHONPATH
```

* Finally, we will have to create symbolic links for *clingo* and *gringo* in the /usr/bin folder, in order to use clingo and gringo as terminal commands.
```
sudo ln -s [PATH TO THE BUILT IN PACKAGE]/clingo-4.5.0-source/build/release/clingo /usr/bin/clingo
sudo ln -s [PATH TO THE BUILT IN PACKAGE]/clingo-4.5.0-source/build/release/gringo /usr/bin/gringo
```

### Installing ROSoClingo

To install the rosoclingo and rosoclingo_examples (only if desired, but is not necessary), we first need to have the basic Potassco suite installed (just as described before). We also need a compatible version of ROS being installed in our system.

We need download the packages rosoclingo and rosoclingo_examples from [HERE](http://www.cs.uni-potsdam.de/rosoclingo/).

Next, we have to move them and unpack them inside the src folder in our catkin workspace.

Finally, we can just build the workspace using catkin_make command. If the clingo and gringo were properly installed, the packages should be built correctly.


## Material

* Latest Potassco guide v2.0, can be downloaded [HERE](http://sourceforge.net/projects/potassco/files/guide/2.0/). (May-2015)


## Useful links
