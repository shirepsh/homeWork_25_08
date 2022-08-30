"""
display to the user a menue with 3 options- 
every option in a different color
"""
class bcolors:
    """ now we display the colors options as a class"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colourful_menu ():
    """ we add to the menu the desired color, 
    important commant- until we wont change the color, the termianl continue to display in the color we set
    in the last line, we need to set also to comeback original color - ENDC"""
    print (f"{bcolors.HEADER}1- open the file")
    print (F"{bcolors.FAIL}2- delete the file ")
    print (f"{bcolors.OKBLUE}3- add to the file{bcolors.ENDC}")
    return

def main():
    colourful_menu()

if __name__=="__main__":
    main()