#!/usr/bin/python3
def add_integer(a, b=98):
    if a:
        if isinstance(a, (int, float)) or isinstance(b, (int, float)):
            if type(a) == float:
                a = int(a)
            if type(b) == float:
                b = int(b)
            return a + b
        else:
            try:
                if (type(a) != int and type(a) != float):
                    print(a, end=" ")
                    raise Exception
                if (type(b) != int and type(b) != float):
                    print(b, end=" ")
                    raise Exception
            except Exception:
                print("must be an integer")
