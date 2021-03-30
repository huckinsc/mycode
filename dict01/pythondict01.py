#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])

print(switch.get("lynx"))


print(switch.get("lynx"), "The key is in another castle....")

print(switch.get("version"))
print(switch.keys())
print(switch.values())

switch.pop("version")
print(switch.keys())
print(switch.values())

switch["adminlogin"] = "kar08"
print(switch.keys())
print(switch.values())

switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())
