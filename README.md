# Bash-Colors-Python
Simple constants to implement bash colors in python f-strings 
\
\
This project also serves as self-learning resource to remind myself of some fundamental concepts
- How to create an installable python module
- Bash prompt color coding
- How to add a License

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

## Licensing Blurb
After a lot of questioning how licensing actually worked and which one gave me closely what I wanted. I ended up choosing BSD-2.
\
I chose BSD-2 for a couple reasons
- I wanted to have a real License, and one that people are famialir with
- I believe it has more clear langague than MIT
- I wanted to make using my software as painless as possible, so no need to really think about use-cases, forwarding the license, or attributing for basic usage/install
- I would have gone with Zero-Clause BSD, but it was not selectable as a regular license in GitHub at the time, and I wanted it to pop up when people hovered it in different views of the project
- I didn't really want any credit, but I suppose the language seems clear enough that actual redistribution of the source code is where it must be involved
