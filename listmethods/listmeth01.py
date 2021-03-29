#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["shh","http","https"]
print(proto)
print(proto[1])
proto.extend("dns")
protoa.append("dns")
print(proto)
proto2 = [22,80,443,53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)

my_list = ["Hello","world."]
new_list = ["This", "is", "Python!"]
my_list.extend(new_list);
print(my_list)
