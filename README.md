# Bash-Colors-Python
Simple constants to implement bash colors in python f-strings

## How to use
Rather than clone the repo, just wget the file and use it where you want
```
wget https://raw.githubusercontent.com/TheeMichael/Bash-Colors-Python/main/bash_colors.py
```

Then import and use fstrings
\
\
Example 1
```
import bash_colors as BC
print(f"{BC.GREEN_B}Example Text!{BC.ENDC}")
```
Example 2
```
from bash_colors import *
print(f"{GREEN_B}Example Text!{ENDC}")
```
## Built in Example
To use the built in example run the file from the terminal
```
python3 ./bash_colors.py
```