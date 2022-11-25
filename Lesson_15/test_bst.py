from Task_from_Lesson_14 import Tree

def test_insert_1():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75])
    assert test_tree.id_node == 50

def test_insert_2():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75])
    assert test_tree.left == 'Node 25, left None, right None'