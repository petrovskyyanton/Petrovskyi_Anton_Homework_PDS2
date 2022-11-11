import math


class StrangeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f'Something wrong: {self.message}'


def sqrt():
    try: # Спроба прийняти додатнє число та вирахувати квадратний корінь з нього
        n = float(input('Enter a positive number:'))
        if n > 0:
            return math.sqrt(n) # Якщо число додатнє - повертається квадратний корінь з цього числа
        else:
            raise StrangeError('Negative number!') # Якщо число від'ємне - викликається помилка StrangeError
    except Exception as ex: # Інші типи помилок (зокрема помилки вводу)
        return ex


print(sqrt())
