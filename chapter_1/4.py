l = ['q', 'r', '4', 3, 8, 'q']

def dublicate(l:list=l):
    if len(l) == len(set(l)):
        res = True
    else:
        res = False
    return res
    