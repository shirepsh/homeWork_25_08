from fs import open_fs

def count_python_loc(fs):
    """Count non-blank lines of Python code.
    -after we wrote the function we need to give a variable that fit the func
    we give a variable with the open_fs func in order to open in right formate for fs 
    and run the count_python_loc we wrote
    we cant run it without the open_fs bec in this function we had 'walk' method and she 
    is not support string (if we will give a regular name of dic) just fs formate"""
    count = 0
    for path in fs.walk.files(filter=['*.py']): #for every path search the py files
        with fs.open(path) as python_file:      # open the files as py files 
            count += sum(1 for line in python_file if line.strip()) #count the blank space
    return count

# here we let the right dic to search into him

projects_fs = open_fs('.') 
#we give a variable with the open_fs func in order to open in right formate for fs and run the count_python_loc we wrote
#we cant run it without the open_fs bec in this function we had 'walk' method and she is not support string just fs formate
print(count_python_loc(projects_fs))


