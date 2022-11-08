list_of_smth = [1, 3.0, '3.0', 4, 5, 6, 7, 8, 9]


def func(list_of_numbers):
    try:
        q = 0
        for i in list_of_numbers:
            if isinstance(i, int) or isinstance(i, float):
                q += 1
            else:
                continue
        if q == len(list_of_numbers):
            set_of_numbers = set(list_of_numbers)
            if len(set_of_numbers) == len(list_of_numbers):
                return 'Всі числа у списку унікальні'
            else:
                return 'У списку чисел зустрічаються повтори'
        else:
            raise TypeError('Numbers from list are not valid!')
    except Exception as ex:
        return ex


print(func(list_of_smth))
