list1 = range(1, 101)
for number in list1:
    if number % 7 == 0:
        print(str(number) + ' Это число целочисленно делится на 7 без остатка')

for number in list1:
    if number % 7 != 0:
        print(str(number) + ' Это число делится на 7 с остатком')
