#!/usr/bin/env python3

#Author: Samip Paudel
#Author ID: 168727212
#Date Created: 2025/01/25

import sys

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print("timer")
    sys.exit(1)

while timer > 0:
    print(f"{timer}")
    timer -= 1

print('blast off!')