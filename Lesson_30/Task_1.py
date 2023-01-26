class HashTable:
    def __init__(self, length_of_table):
        self.length_of_table = length_of_table
        self.table = [None]*length_of_table

    def print(self):
        for i in self.table:
            if i is not None:
                print(f'{i[0]} : {i[1]}')
            else:
                print(f'{None} : {None}')

    def setitem(self, key, value):
        index = hash(key) % self.length_of_table
        try:
            for i in self.table:
                if i is not None:
                    index += 1
                    continue
                if i is None:
                    self.table[index] = [key, value]
                    break
        except IndexError as ex:
            print(f'{ex}')

    def getitem(self, key):
        index = hash(key) % self.length_of_table
        value = self.table[index]
        if value is None:
            raise KeyError(key)
        return f'{value[0]} : {value[1]}'

    def delitem(self, key):
        index = hash(key) % self.length_of_table
        self.table[index] = None


A = HashTable(10)
A.setitem(3, 0)
A.setitem(0, '2')
A.setitem(0, '3')
A.setitem('1', '3')
A.print()
print("*"*10)
A.delitem(3)
print(A.getitem(0))
print("*"*10)
A.print()
