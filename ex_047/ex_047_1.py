
from typing import Text


def print_my_name()->None:
    """Prints a name to the console"""
    print(""" 
              ######  ##     ##  ######     ###    ##    ## 
            ##    ## ##     ## ##    ##   ## ##   ###   ## 
            ##       ##     ## ##        ##   ##  ####  ## 
            ######  ##     ##  ######  ##     ## ## ## ## 
                ## ##     ##       ## ######### ##  #### 
          ##    ## ##     ## ##    ## ##     ## ##   ### 
          ######   #######   ######  ##     ## ##    ## """)

def print_my_name_2()->None:
    """Prints a name to the console"""
    print(r"""
      _____                           
     (      ,   .   ____   ___  , __  
      `--.  |   |  (      /   ` |'  `.
         |  |   |  `--.  |    | |    |
    \___.'  `._/| \___.' `.__/| /    |
                                        """)

print_my_name()
print_my_name_2()