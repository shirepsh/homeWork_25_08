"""
1- we make an array from numpy methods - using arange
2- we save those array into a file - using savez 
we will give to the file the name.npz
we give to every array a name x_axis, y_axis
3- delete the variable x and y in order to leran how to load the information from load method in numpy
3.del x, y
4- load the npz file into our workspacr again
5- after we loaded our array back again, we can load them into their vriable
"""

from unittest.mock import MagicMixin
import numpy as np

def main():

    x = np.arange(1, 11)
    # print (x)

    y = x * 2
    # print (y)

    """
    then we save those array into a file - using savez 
    we will give to the file the name.npz
    we give to every array a name x_axis, y_axis
    """

    np.savez ("x_y_array.npz", x_axis = x, y_axis = y)

    """
    now - i delete the variable x and y in order to leran how to load the information from load method in numpy
    1- del x, y
    2- whos - show me which variable are the function contains 
    (in order to make sure our workspace empty and now we can load the file into the workspace)
    """
    del x, y
 
    """
    now we load the npz file into our workspace again
    """
    load_xy = np.load ("x_y_array.npz")
    print (load_xy.files)


    """
    after we loaded our array back again, we can load them into their vriable
    """
    x = load_xy["x_axis"]
    y = load_xy["y_axis"]
    print(x)
    print(y)

if __name__ == "__main__":
    main()