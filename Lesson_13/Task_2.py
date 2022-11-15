import time
import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print("Int List:", int_list)
print("Float List:", float_list)
print("String List:", str_list)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums, number_of_iteraton):
    cur_time = time.time()
    for i in range(number_of_iteraton):
        n = len(nums)

        for i in range(n, -1, -1):
            heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
    return (time.time() - cur_time)/number_of_iteraton


copy_my_list_1 = int_list
copy_my_list_2 = float_list
copy_my_list_3 = str_list
iteration_number = int(input("Number of iteration:"))
t1 = heap_sort(copy_my_list_1, iteration_number)
t2 = heap_sort(copy_my_list_2, iteration_number)
t3 = heap_sort(copy_my_list_3, iteration_number)
print("Shell Sort:", copy_my_list_1, copy_my_list_2, copy_my_list_3)
print(f'Time for sorting integers: {t1}\nTime for sorting floats: {t2}\nTime for sorting words: {t3}')
