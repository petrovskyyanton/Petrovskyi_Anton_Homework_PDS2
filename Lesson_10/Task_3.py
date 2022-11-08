import sys
import math


class StrangeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return 'Somthing wrong!'


def sqrt():
    try:
        n = int(input('Enter a positive number:'))
        if n > 0:
            return math.sqrt(n)
        else:
            raise StrangeError()
    except Exception as ex:
        return ex


print(sqrt())
