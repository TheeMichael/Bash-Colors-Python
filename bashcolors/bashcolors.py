r"""
Bash Colors provides f-string usable constants for color coding terminal outputs using bash

Example:
  - import bash_colors as bc
  - print(f"{bc.GREEN_B}Example Text!{bc.ENDC}")
"""

ENDC = "\033[0m"
'''End Color Termination Value'''

#------------------------------
# Bold Colors
#------------------------------
BLACK_B="\033[1;30m"
'''Black Bold'''

RED_B="\033[1;31m"
'''Red Bold'''

GREEN_B="\033[1;32m"
'''Green Bold'''

YELLOW_B="\033[1;33m"
'''Yellow Bold'''

BLUE_B="\033[1;34m"
'''Blue Bold'''

MAGENTA_B="\033[1;35m"
'''Magenta Bold'''

CYAN_B="\033[1;36m" 
'''Cyan Bold'''

GRAY_B="\033[1;90m" 
'''Gray Bold'''



#------------------------------
# Light Bold Colors
#------------------------------
L_RED_B="\033[1;91m"
'''Light Red Bold'''

L_GREEN_B="\033[1;92m"
'''Light Green Bold'''

L_YELLOW_B="\033[1;93m"
'''Light Yellow Bold'''

L_BLUE_B="\033[1;94m"
'''Light Blue Bold'''

L_MAGENTA_B="\033[1;95m"
'''Light Magenta Bold'''

L_CYAN_B="\033[1;96m" 
'''Light Cyan Bold'''

L_GRAY_B="\033[1;37m"
'''Light Gray Bold'''

WHITE_B="\033[1;97m"
'''White Bold'''



#------------------------------
# Regular Colors
#------------------------------
BLACK="\033[30m"
'''Black'''

RED="\033[31m"
'''Red'''

GREEN="\033[32m"
'''Green'''

YELLOW="\033[33m"
'''Yellow'''

BLUE="\033[34m"
'''Blue'''

MAGENTA="\033[35m"
'''Magenta'''

CYAN="\033[36m" 
'''Cyan'''

GRAY="\033[90m" 
'''Gray'''



#------------------------------
# Light Colors
#------------------------------
L_RED="\033[91m"
'''Light Red'''

L_GREEN="\033[92m"
'''Light Green'''

L_YELLOW="\033[93m"
'''Light Yellow'''

L_BLUE="\033[94m"
'''Light Blue'''

L_MAGENTA="\033[95m"
'''Light Magenta'''

L_CYAN="\033[96m" 
'''Light Cyan'''

L_GRAY="\033[37m"
'''Light Gray'''

WHITE="\033[97m"
'''White'''

TEST_VAR=0
TEST_VAR2=1
def bash_colors_test():
    #Blacks
    print(f"{BLACK}Black{ENDC}")
    print(f"{BLACK_B}Black Bold{ENDC}")
    
    print('')

    #Reds
    print(f"{RED}Red{ENDC}")
    print(f"{RED_B}Red Bold{ENDC}")

    print(f"{L_RED}Light Red{ENDC}")
    print(f"{L_RED_B}Light Red Bold{ENDC}")
    
    print('')

    #Greens
    print(f"{GREEN}Green{ENDC}")
    print(f"{GREEN_B}Green Bold{ENDC}")
    
    print(f"{L_GREEN}Light Green{ENDC}")
    print(f"{L_GREEN_B}Light Green Bold{ENDC}")

    print('')
    
    #Yellows
    print(f"{YELLOW}Yellow{ENDC}")
    print(f"{YELLOW_B}Yellow Bold{ENDC}")
    
    print(f"{L_YELLOW}Light Yellow{ENDC}")
    print(f"{L_YELLOW_B}Light Yellow Bold{ENDC}")

    print('')

    #Blues
    print(f"{BLUE}Blue{ENDC}")
    print(f"{BLUE_B}Blue Bold{ENDC}")
    
    print(f"{L_BLUE}Light Blue{ENDC}")
    print(f"{L_BLUE_B}Light Blue Bold{ENDC}")

    print('')
    
    #Magentas
    print(f"{MAGENTA}Magenta{ENDC}")
    print(f"{MAGENTA_B}Magenta Bold{ENDC}")

    print(f"{L_MAGENTA}Light Magenta{ENDC}")
    print(f"{L_MAGENTA_B}Light Magenta Bold{ENDC}")

    print('')
    
    #Cyans
    print(f"{CYAN}Cyan{ENDC}")
    print(f"{CYAN_B}Cyan Bold{ENDC}")

    print(f"{L_CYAN}Light Cyan{ENDC}")
    print(f"{L_CYAN_B}Light Cyan Bold{ENDC}")

    print('')
    
    #Grays
    print(f"{GRAY}Gray{ENDC}")
    print(f"{GRAY_B}Gray Bold{ENDC}")

    print(f"{L_GRAY}Light Gray{ENDC}")
    print(f"{L_GRAY_B}Light Gray Bold{ENDC}")

    print('')

    #Whites
    print(f"{WHITE}White{ENDC}")
    print(f"{WHITE_B}White Bold{ENDC}")

    print('')


if __name__ == "__main__":
    bash_colors_test()