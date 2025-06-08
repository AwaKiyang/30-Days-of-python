import os
#in python we use Os module to perform operating systems task. the OS module in python provides functions for creating , changing current working directory
#os.getcwd()
cwd = os.getcwd()
print(cwd) #C:\Users\awaki\Desktop\python codes\module

#os.mkdir
#os.mkdir('waar')

#os.chdir
newdir = 'C:/Users/awaki/Desktop/python codes/module/waar'
os.chdir(newdir)
print(cwd)