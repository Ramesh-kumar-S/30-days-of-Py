#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b=bin(n)[2:]
    s=b.split("0")
    c=[]
    count=0
    for i in s:
        c.append(i.count("1"))
    print(max(c))

