lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = int()
for i in lst:
    if not i%3 and i<30:
        print(f'Делиться на 3 и меньше 30: {i}')
    else:
        result+=i
print(f'Сумма остальных: {result}')