#!/usr/bin/python3
def islower(c):
    if c:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        if c in lower:
            return True
        else:
            return False
    else:
        return None
