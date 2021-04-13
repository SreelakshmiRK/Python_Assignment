#import os
# String to store the OS command
# comm = "echo Tinitiate.com"
# comm = "echo path"
# Run the OS command using system function
# os.system(comm)


import subprocess
#subprocess.call(['echo','Hello Tinitiate'], shell=True)
#syntax of file path for opening python file from another python file
#subprocess.call(['python',"C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\test1.py"], shell=True)  
subprocess.call(['python','C:/Users\\sreen\\OneDrive\\Desktop\\Python/test1.py'], shell=True)
# subprocess.call(['python','C:/Users\\sreen\\OneDrive\\Desktop\\Python/Main.py'], shell=True)


# ## >```
# ## >```

# Capture Standard Output
# Execute a SYNTACTICALLY VALID DOS command on windows using subprocess.Popen
# Capture Standard Out and Standard Error in SDOut and SDErr variables
# (SDOut,SDErr) = subprocess.Popen( ['python',"C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\test1.py"]
                                 # ,stdout=subprocess.PIPE
                                 # ,stderr=subprocess.PIPE
                                 # ,shell=True).communicate()
(SDOut,SDErr) = subprocess.Popen( ['python',r'C:\Users\sreen\OneDrive\Desktop\Python\test1.py']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()
#Print the SDOut and SDErr variables
print('------ Standard Out and Standard Error in binary-----------')
print(SDOut)
print(SDErr)
print('------ Standard Out and Standard Error using decode(utf-8)-----------')
print(SDOut.decode('utf-8'))
print(SDErr.decode('utf-8'))
