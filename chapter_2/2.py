def out(lst: list[int]) -> print:
    for i in lst:
        if i == 139:
            break
        elif not i%2:
            print(i)

if __name__ =='__main__':
    out([1,2,3,4,5,6,7,139,8,9,10])