#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""
import sys
Status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
i = 0
fileSize = 0

for input in sys.stdin:
    ListInput = input.split(' ')
    if len(ListInput) > 2:
        Thestatus = ListInput[-2]
        f_size = int(ListInput[-1])
        if Thestatus in Status:
            Status[Thestatus] += 1
    fileSize += f_size
    i += 1
    if i == 10:
        print("File size: {:d}".format(fileSize))
        for key, value in sorted(Status.items()):
            if value != 0:
                print("{}: {:d}".format(key, value))
        i = 0

print("File size: {:d}".format(fileSize))
for key, value in sorted(Status.items()):
    if value != 0:
        print("{}: {:d}".format(key, value))