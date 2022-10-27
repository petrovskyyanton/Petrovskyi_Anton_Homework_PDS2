def mane_function(x):
    print(x)
    for i in range(10):
        print(i**2)
    dictionary = {'key_1': 1, 'key_2': 2, 'key_3': 3}
    list_of_smth = [dictionary, 1234, None, f'String with {x}']
    set_of_smth = (1, 3, 24, f'{x}')
    return list_of_smth, set_of_smth


def test_function(y):
    t = int(input('Number:'))
    a = t//10
    print(f'String with {y} and {a}')


print(test_function(1), mane_function(1))
