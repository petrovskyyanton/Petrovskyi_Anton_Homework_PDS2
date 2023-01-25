import hashlib

dic = {'anton': '202cb962ac59075b964b07152d234b70', 'andrew': '962012d09b8170d912f0669f6d7d9d07',
       'ann': '2d59ca9b3bc9b2be20dca1d1d13198e3'}


def registration():
    login = input("Please, enter your new LOGIN:")
    while True:
        if login not in dic.keys():
            psd1 = input("Please, enter new PASSWORD:")
            psd2 = input("Please, enter new PASSWORD again:")
            if psd1 == psd2:
                psd = psd1
                hash_object = hashlib.md5(bytes(f'{psd}', encoding="utf-8"))
                hash_psd = hash_object.hexdigest()
                dic[login] = hash_psd
                break
            else:
                print('Passwords do not match! Try again')
        else:
            login = input("Please, enter ANOTHER LOGIN:")


def authorisation():
    i = 0
    while i < 10:
        login = input("Please, enter your LOGIN:")
        psd = input("Please, enter your PASSWORD:")
        hash_object = hashlib.md5(bytes(f'{psd}', encoding="utf-8"))
        hash_psd = hash_object.hexdigest()
        if (login, hash_psd) in dic.items():
            print('The authorization is successful!')
            break
        else:
            i += 1
            if i < 10:
                print('Login or/and password are incorrect! Try again!')
            else:
                print('You entered incorrect login or/and password 10 times!')
                break


registration()
authorisation()

print(dic)
