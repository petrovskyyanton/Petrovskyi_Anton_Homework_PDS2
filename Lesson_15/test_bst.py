from Task_from_Lesson_14 import Tree

def test_insert_1():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75])
    assert test_tree.__str__() == 'Node 50, left Node 25, left None, right None, right Node 75, left None, right None'


def test_insert_2():
    test_tree = Tree()
    test_tree.insert_from_list([50, None, None])
    assert test_tree.id_node == 50

def test_get_min_1():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75, 10, 30, 60, 80])
    assert test_tree.get_min() == 10

def test_get_min_2():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75, None, 30, 60, 80])
    assert test_tree.get_min() == 25


def test_get_max_1():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75, 10, 30, 60, 80])
    assert test_tree.get_max() == 80


def test_get_max_2():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75, None, 30, 60, None])
    assert test_tree.get_max() == 75

def test_delete_1():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75])
    test_tree.delete(75)
    assert test_tree.__str__() == 'Node 50, left Node 25, left None, right None, right None'

def test_delete_2():
    test_tree = Tree()
    test_tree.insert_from_list([50, 25, 75])
    test_tree.delete(50)
    assert test_tree.__str__() == 'Node 75, left Node 25, left None, right None, right None'