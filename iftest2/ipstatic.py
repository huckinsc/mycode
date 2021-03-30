#!/usr/bin/env python3

import ipaddress

ipchk = input("Apply an IP address: ")

if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
    try:
        addr_obj = ipaddress.ip_address(ipchk)
        print("Looks like the IP address was set: " + ipchk)
    except:
        print("Not a valid address.")
else:
    print("You did not enter a value")
