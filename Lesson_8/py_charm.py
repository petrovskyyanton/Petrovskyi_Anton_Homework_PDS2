def mane_function(x):
    print(x)
    for i in range(10):
        print(i**2)
    dictionary = {'key_1': 1, 'key_2': 2, 'key_3': 3}
    list_of_smth = [dictionary, 1234, None, f'String with {x}']
def test_function(y):
    t = int(input('Number:'))
    a = t//10
    print(f'String with {y} and {a}')


print(test_function(1), mane_function(1))
