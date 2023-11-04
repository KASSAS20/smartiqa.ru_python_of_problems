def month_to_season(m: int) -> str:
    if m in [12, 1, 2]:
        return 'Зима'
    elif m in [3, 4, 5]:
        return 'Весна'
    elif m in [6, 7, 8]:
        return 'Осень'
    elif m in [9, 10, 11]:
        return 'Лето'
    else:
        return 'Неизвестный месяц'

if __name__ == '__main__':
    print(month_to_season(1))
    print(month_to_season(2))
    print(month_to_season(3))
    print(month_to_season(4))
    print(month_to_season(5))
    print(month_to_season(6))
    print(month_to_season(7))
    print(month_to_season(8))
    print(month_to_season(9))
    print(month_to_season(10))
    print(month_to_season(11))
    print(month_to_season(12))
    print(month_to_season(13))
    print(month_to_season(0))
