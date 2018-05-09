# Creating Programs for the Commmand Line - The _OS_ and _SYS_ modules

Writing Python programs are very useful but at some point you may want to share a bit of code that another person can then run.  And that person may have no experience with Python or programming or even the command line.  In order for that person to use what you have done, your program really needs to become a black box where something goes in and something comes out.  While we are interested in how a particular piece of code works, most people are not.  They just want an answer to their question and if your piece of code gets them that answer without too much investment of time and energy then they are more likely to use it.  As long as they do not have to look at your code.

To create black box programs you have to get your script communicating with the surrounding computer system.  To do this, we are going to learn about _sys_ and _os_ modules.  

### The _sys_ module

The _sys_ module (short for 'system') is what allows you to capture command line arguments and get information about the operating system.  This allows one to get info about the operating system, then you can utilize that information in the script.  Like all module, _sys_ has lots of capabilites I encourage you to explore.  Here are a few that are most useful.

_sys_ provides an easy method for entering command line arguments.  So if you wanted to create a script to be called in the command line, it would look something like this.

```bash
python myProgram.py "Harvey the Rabbit" "Posters" 1800
```
Inside of the myProgram.py, sys can capture and utilize these command line arguments.  In this case, _sys.argv[0]_ is the program itself "myProgram.py", _sys_agrv[1]_ is the next argument, "Harvey the Rabbit", _sys_argv[2]_ is "Posters", and _sys.argv[3]_ is the integer 1800.  Inside of the script these arguments can be called using _.argv[]_.

The following are other useful aspects of sys.

```python
sys.platform #returns a string of the operating system

sys.getwindowsversion() #returns the version of windows

sys.exit(arg) #will stop the execution of the script and exit.
```

### The _os_ module

The _os_ module allows for manipulation of the filesystem in the operating system.  It is a very useful module for finding the path or establishing a new path to which objects can be stored.  

```python
os.chdir(path)
```
Changes the current working directory to the path name provided.

```python
os.getcwd()
```
Retrieves the string of the current working directory.  Same as 'pwd' in command line. 

```python
os.listdir()
```
Returns a list of all the files in a path.


### The _system_ module

While _sys_ can get information about the operating system, I find the _system_ module to be much more useful and easy to use.

```python
import system
import sys

print platform.system()
>>'Linux'
print sys.platform
>>'Linux2'
```
platform.system() yields an answer that is simply easier to understand with fewer possible errors.  It is going to yield either "Windows", "Linux", or "Os" (I think) with no other associated info.  

##### Question:  Why is knowing the operating system important?  Answer: You are about to find out.


### Practice #1 

You are going to create a script that takes a command line agrument, determines the operating system being used and creates ten new directories (folders) in the current working directory with those names plus the numbers one through 10.  In other words if the person enters:

```bash
makeDirectory.py "newFolder_"
```
The script will create ten folder (directories) "newFolder_1", "newFolder_2", "newFolder_3", etc. in the current working directory.  

### Practicr #2

Now that you have done this, extend your program to take a second command line argument to create as many directories as the user wants.  In other words, it should work like so:

```bash
makeDirectory_v2.py "newFolder_" 10
```
The second argument passed in command line will be number of directories the user wants to create.  

### Practice #3

Create a script that only creates one folder but uses the time and date to create a unique name for the directory.  The input will be the same as practice #1 but instead fo creating ten files it will create something like this:

```
newFolder_11200304052018
```
You can break up the name any way you want just make sure that unique names are created using the time and date.  