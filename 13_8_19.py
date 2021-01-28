ticket = int(input('Введите количество билетов'))
age = [int(input('Введите возраст')) for i in range(ticket)]
price = 0
for j in range(len(age)):

    if age[j] <= 18:
        print('free')
    elif age[j] >= 18 and age[j] <= 25:
        print('990 р')
        price = price + 990
    elif age[j]> 25:
        print('1390 р')
        price = price + 1390
if ticket <= 3:
    print('Цена', price)
else:
    discount = price * 10 // 100
    print('скидка', discount)
    print('цена со скидкой', price - discount)









































