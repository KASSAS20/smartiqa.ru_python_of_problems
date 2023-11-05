class Human:
    default_name = None
    default_age = 0


    def __init__(self, name:str=default_name, age:int=default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None


    def info(self) -> print:
        print(f'name: {self.name}\nage: {self.age}\nmoney: {self.__money}\nhouse: {self.__house}')

    @staticmethod
    def default_info(name:str = default_name, age:int = default_age) -> print:
        print(f'name: {name}\nage: {age}')


    def earn_money(self, count: int) -> None:
        self.__money += count

    
    def buy_house(self, house, discount: int) -> print:
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(price, house)
        else:
            print('Не достаточно денег')


    def __make_deal(self, price:int, house) -> None:
        self.__money -= price
        self.__house = house

class House:
    def __init__(self, area: float, price: int) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: float) -> float:
        return self._price - discount


class SmallHouse(House):
    default_area = 40


    def __init__(self, price: float) -> None:
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    Human.default_info()
    Hum = Human('SAS', 19)
    Hum.info()
    SH = SmallHouse(20000000)
    Hum.buy_house(SH, 1000000)
    Hum.earn_money(10000000000000000)
    Hum.buy_house(SH, 1000000)
    Hum.info()
