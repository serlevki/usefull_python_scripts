#!/bin/bash/python3

import shutil # ------>For copy file
import os     # ------>For check if file exist and got size
import sys    # ------>For CLI arguments

"""
--------HOW to use-------
         script name   logfile  trigger size(kb)    count of backup file
python   purgelog.py   log.txt  10                  3
"""

if(len(sys.argv) < 4):
    print("Missing arguments!")
    exit(1)

file_name        = sys.argv[1]
limit_size       = int(sys.argv[2])
logs_file_number = int(sys.argv[3])

if(os.path.isfile(file_name) == True):            # check if main log file exists
    log_file_size = os.stat(file_name).st_size   # get size of main file
    log_file_size = log_file_size // 1024        # convert to kb

    if(log_file_size >= limit_size):
        if(logs_file_number > 0):
            for current_file_number in range (logs_file_number, 1, -1):
                src = file_name + "_" + str(current_file_number - 1)
                dst = file_name + "_" + str(current_file_number)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied " + src + " to" + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copird from: " + file_name + " to" + file_name + "_1")

        myfile = open(file_name, 'w')
        myfile.close()
