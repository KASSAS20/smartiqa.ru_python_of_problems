def calc(num:int) -> int:
    result = int()
    for i in [j for j in str(num)]:
        result+=int(i)
    return result
