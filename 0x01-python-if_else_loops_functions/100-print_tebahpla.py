#!/usr/bin/python3
print(''.join(
    [chr(i).upper() if i % 2 != 0 else chr(i) for i in range(122, 96, -1)]
))
