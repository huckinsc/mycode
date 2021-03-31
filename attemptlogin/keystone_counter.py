#!/usr/bin/python3

loginfail =0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# Commenting out as this in not practical for large files
#keystone_file_lines = keystone_file.readlines()
#for line in keystone_file_lines:
for line in keystone_file:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of fails is: ", loginfail)
keystone_file.close()
