import sys
import random

print('Если хочешь взять еще 1 карту напиши "еще". Если не хочешь больше брать карты напиши "пас".')
print('Твоя задача набрать наибольшее количество очков до 21.')
print('Если ты наберешь больше 21 очков, то ты проиграешь!')

letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
random_index1 = random.randint(0, len(letters_list) - 1)
print(letters_list[random_index1])

letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
random_index2 = random.randint(0, len(letters_list) - 1)
print(letters_list[random_index2])

a = input()
if a == 'еще':
    letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
    random_index3 = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index3])
elif a == 'пас' and letters_list[random_index1] + letters_list[random_index2] >= 17:
    print('Ты победил!!!')
    sys.exit()
elif a == 'пас' and letters_list[random_index1] + letters_list[random_index2] <= 17:
    print('Ты проиграл')
    sys.exit()
else:
    print('ошибка')
    sys.exit()
if letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] > 21:
    print('перебор')
    sys.exit()

b = input()
if b == 'еще':
    letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
    random_index4 = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index4])
elif b == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] >= 17:
    print('Ты победил!!!')
    sys.exit()
elif b == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] <= 17:
    print('Ты проиграл')
    sys.exit()
else:
    print('ошибка')
    sys.exit()
if letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] > 21:
    print('перебор')
    sys.exit()

c = input()
if c == 'еще':
    letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
    random_index5 = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index5])
elif c == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] >= 17:
    print('Ты победил!!!')
    sys.exit()
elif c == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] <= 17:
    print('Ты проиграл')
    sys.exit()
else:
    print('ошибка')
    sys.exit()
if letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] > 21:
    print('перебор')
    sys.exit()

d = input()
if d == 'еще':
    letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
    random_index6 = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index6])
elif d == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] >= 17:
    print('Ты победил!!!')
    sys.exit()
elif d == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] <= 17:
    print('Ты проиграл')
    sys.exit()
else:
    print('ошибка')
    sys.exit()
if letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] + letters_list[random_index6] > 21:
    print('перебор')
    sys.exit()

e = input()
if e == 'еще':
    letters_list: list[str] = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
    random_index7 = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index7])
elif e == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] + letters_list[random_index6] >= 17:
    print('Ты победил!!!')
    sys.exit()
elif e == 'пас' and letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] + letters_list[random_index6] <= 17:
    print('Ты проиграл')
    sys.exit()
else:
    print('ошибка')
    sys.exit()
if letters_list[random_index1] + letters_list[random_index2] + letters_list[random_index3] + letters_list[random_index4] + letters_list[random_index5] + letters_list[random_index6] + letters_list[random_index7] > 21:
    print('перебор')
    sys.exit()