parent_dir = "E:/pythonprojects/automate the boring stuff"

for i in range (1,19): # will create 18 folders from 1 to 18
    path  = ("chapter " + str(i))
    os.mkdir(os.path.join(parent_dir, path))
    
    

