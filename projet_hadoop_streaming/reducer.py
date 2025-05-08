#!/usr/bin/env python
# reducer.py

import sys

current_key = None
current_sum = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        continue

    parts = line.split('\t')
    if len(parts) != 2:
        continue

    key, value = parts
    try:
        count = int(value)
    except ValueError:
        continue

    if key == current_key:
        current_sum += count
    else:
        if current_key is not None:
            sys.stdout.write("%s\t%d\n" % (current_key, current_sum))
        current_key = key
        current_sum = count

# emet le dernier groupe
if current_key is not None:
    sys.stdout.write("%s\t%d\n" % (current_key, current_sum))
