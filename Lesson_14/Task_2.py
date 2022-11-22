class Tree:

    def __init__(self, id_node=None):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node {self.id_node}, left {self.left}, right {self.right}'

    # Insert method to create nodes
    # def insert(self, id_node):
    #     if self.id_node:
    #         if id_node < self.id_node:
    #             if self.left is None:
    #                 self.left = Tree(id_node)
    #             else:
    #                 self.left.insert(id_node)
    #         elif id_node > self.id_node:
    #             if self.right is None:
    #                 self.right = Tree(id_node)
    #             else:
    #                 self.right.insert(id_node)
    #     else:
    #         self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    def insert(self, value):
        if self.id_node is None:
            self.id_node = value
            return
        if self.id_node == value:
            raise ValueError(f'{value} already exists')
        if value < self.id_node:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Tree(value)

    def insert_from_list(self, list_of_elements):
        if len(list_of_elements) % 2 == 0:
            raise ValueError(f'{list_of_elements} is invalid list')
        end = (len(list_of_elements) - 3) // 2
        for i in range(end + 1):
            value = list_of_elements[i]
            if value is None:
                continue
            left = list_of_elements[2 * i + 1]
            right = list_of_elements[2 * i + 2]
            if left is not None:
                if left >= value:
                    raise ValueError(f'{left} is greatest than {value}')
            if right is not None:
                if right <= value:
                    raise ValueError(f'{right} is less than {value}')
        for i in list_of_elements:
            if i is None:
                continue
            self.insert(i)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.id_node

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.id_node


example_1 = Tree()
list_example_1 = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]
example_1.insert_from_list(list_example_1)
list_example_2 = [10, 5, 15, 4, 6, 14, 20]
example_2 = Tree()
example_2.insert_from_list(list_example_2)
print(example_1)
print(example_2)
print(f'Max value: {example_1.get_max()}, min value: {example_1.get_min()}')
print(f'Max value: {example_2.get_max()}, min value: {example_2.get_min()}')

