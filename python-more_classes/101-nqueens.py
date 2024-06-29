#!/usr/bin/python3

import sys

result = sys.subprocess.run([sys.executable, "-c", "print('ocean')"])
print(result)
