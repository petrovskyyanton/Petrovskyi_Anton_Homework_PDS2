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

    def set_item(self, key, value):
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

    def get_item_from_key(self, key):
        for i in self.table:
            if i[0] == key:
                index = hash(key) % self.length_of_table
                val = self.table[index]
                if val is None:
                    raise KeyError(key)
                return f'{val[0]} : {val[1]}'

    def get_item_from_value(self, value):
        for i in self.table:
            if i[1] == value:
                return f'{i[0]} : {i[1]}'

    def del_item(self, key):
        index = hash(key) % self.length_of_table
        self.table[index] = None


A = HashTable(10)
A.set_item(3, 0)
A.set_item(0, '2')
A.set_item(0, '3')
A.set_item('1', '3')
A.print()
print("*"*10)
A.del_item(3)
print(A.get_item_from_key(0))
print(A.get_item_from_value('3'))
print("*"*10)
A.print()
