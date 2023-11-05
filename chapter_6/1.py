
class Alphabet:
    def __init__(self, lang: str, letters:list[str]):
        self.lang = lang
        self.letters = letters
    

    def print(self):
        print(' '.join(self.letters))


    def letters_num(self):
        print(len(self.letters))

    
class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', list('abcdefghijklmnopqrstuvwxyz'))
    

    def is_en_letter(self, char:str) -> bool:
        return char.lower() in self.letters

    
    def letters_num(self) -> int:
        return EngAlphabet.__letters_num


    @staticmethod
    def example():
        print("I'am JASSAS.")


if __name__ == '__main__':
    Eng = EngAlphabet()
    Eng.print()
    print(Eng.letters_num())
    print(Eng.is_en_letter('F'))
    print(Eng.is_en_letter('Щ'))
    Eng.example()