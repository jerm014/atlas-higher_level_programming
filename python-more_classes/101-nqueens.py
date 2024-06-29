#!/usr/bin/python3

import sys

result = sys.subprocess.run([sys.executable, "-c", "ls"])
print(result)
