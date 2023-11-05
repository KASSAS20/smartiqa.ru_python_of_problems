class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}


    def __init__(self, index: int) -> None:
        self._index = index
        self._state = 0
    

    def grow(self) -> None:
        self._state += 1


    def is_rep(self) -> bool:
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, count: int) -> None:
        self.tomatoes = [Tomato(index) for index in range(count)]


    def grow_all(self) -> None:
        for tomato in self.tomatoes:
            tomato.grow()


    def all_are_ripe(self) -> bool:
        result = True
        for i in self.tomatoes:
            if i._state != 3:
                result = False
        return result

    
    def give_away_all(self) -> None:
        self.tomatoes = []


class Gardener:
    def __init__(self, name: str, plant:TomatoBush) -> None:
        self.name = name
        self._plant = plant


    def work(self) -> None:
        self._plant.grow_all()

    
    def harvest(self) -> print:
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Плоды еще не созрели')


    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')









if __name__ == '__main__':
    Gardener.knowledge_base()
    TB = TomatoBush(count = 5)
    GD = Gardener(name = 'Садовник БУШ', plant=TB)
    GD.work()
    GD.harvest()
    GD.work()
    GD.work()
    GD.harvest()