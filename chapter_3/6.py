s = 'арозаупаланалапуазора'

def pallidrom(s:str) -> bool:
    if s == s[::-1].lower():
        return True
    else:
        return False
    