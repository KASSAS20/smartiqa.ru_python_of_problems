def calc(a:int, b:int, operation: str) -> int or float:
    result = 'Операция не поддерживаеться'
    if (isinstance(a, (int, float))) and (isinstance(b, (int, float))):
        match operation:
            case '+':
                result = a+b
            case '-':
                result = a-b
            case '*':
                result = a*b
            case '/':
                if b is not 0:
                    result = a/b
    return result

if __name__ == '__main__':
    print(calc(2,4,'-'))
    print(calc(2,4,'+'))
    print(calc(2,4,'*'))
    print(calc(2,4,'/'))
    print(calc(2,4,'a'))
    print(calc(2,0,'/'))

