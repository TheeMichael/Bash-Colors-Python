# Bash-Colors-Python
Simple constants to implement bash colors in python f-strings

## Installing

Use pip to install directly from git
```
pip install git+https://github.com/TheeMichael/Bash-Colors-Python.git
```

## Uninstalling

```
pip uninstall bashcolors
```

## Updating to Newest Version
Will need to uninstall package first, so that it actually updates, otherwise it will skip it
```
pip uninstall bashcolors
pip install git+https://github.com/TheeMichael/Bash-Colors-Python.git
```
## How to use
Import the module and sandwich desired text between a color and the end-constant in a python f string.
\
Example 1
```
import bash_colors as bc
print(f"{bc.GREEN_B}Example Text!{bc.ENDC}")
```
Example 2
```
from bashcolors import *
print(f"{GREEN_B}Example Text!{ENDC}")
```
## Built in Example
The example can help you see what all your bash terminal colors can look like.
\
To use the built in example:
```
import bashcolors as bc
bc.bash_colors_test()
```