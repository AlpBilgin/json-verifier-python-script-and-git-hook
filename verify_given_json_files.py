#!/usr/bin/env python3

import sys
from lib import verify_json_file 

flag = 0

for i in range(len(sys.argv)):
  if i>0 and not verify_json_file.verify_json_file(sys.argv[i]):
    print("{} is broken".format(sys.argv[i]))
    flag = 1

exit(flag)

