def say_my_name()->None:
    """Prints a name to the console"""
    print(""" 
              ######  ##     ##  ######     ###    ##    ## 
            ##    ## ##     ## ##    ##   ## ##   ###   ## 
            ##       ##     ## ##        ##   ##  ####  ## 
            ######  ##     ##  ######  ##     ## ## ## ## 
                ## ##     ##       ## ######### ##  #### 
          ##    ## ##     ## ##    ## ##     ## ##   ### 
          ######   #######   ######  ##     ## ##    ## """)

def say_many_names(multiplier):
    for i in range(multiplier):
        say_my_name()
