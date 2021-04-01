#!/usr/bin/env python3

import pyexcel

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_rating = input("What is the rating? ")
    input_extra = input("any extra info? ")
    d = {"IP": input_ip, "driver": input_driver, "rating":input_rating, "extra": input_extra}
    return d

mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break


filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'/home/student/static/{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
