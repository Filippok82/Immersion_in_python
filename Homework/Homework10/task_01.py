"""Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе
переданного типа и верните его из класса-фабрики."""


class Animals:
    def __init__(self, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, name: str):
        """место обитания,покровы тела,температура,способ размножения, название """
        self.habitat = habitat
        self.body_coverings = body_coverings
        self.temperature = temperature
        self.method_reproduction = method_reproduction
        self.name = name


class Fish(Animals):
    """Рыбы"""

    def __init__(self, name: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, gills):
        super().__init__(name, habitat, body_coverings, temperature, method_reproduction)
        self.gills = gills

    def organ_gills(self):
        return f'Наличие жаберного дыхания {self.gills}'


class Birds(Animals):
    """Птицы"""

    def __init__(self, name: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, flight: bool):
        super().__init__(name, habitat, body_coverings, temperature, method_reproduction)
        self.flight = flight

    def fly(self):
        print('Умение летать')


class Amphibians(Animals):
    """Земноводные"""

    def __init__(self, name: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, respiratory: bool):
        super().__init__(name, habitat, body_coverings, temperature, method_reproduction)
        self.respiratory = respiratory

    def respirator_organ(self):
        print('Умение дышать легкими и кожей')


class Reptiles(Animals):
    """Пресмыкающиеся"""

    def __init__(self, name: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, crawl: bool, ):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.crawl = crawl

    def crawl_skill(self):
        print('Умение ползать')


class Mammals(Animals):
    """Млекопитающие"""

    def __init__(self, name: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, caring_for_offspring: bool):
        super().__init__(name, habitat, body_coverings, temperature, method_reproduction)
        self.caring_for_offspring = caring_for_offspring

    def brain_activity(self):
        print('Забота о потомстве')


# if __name__ == '__main__':
#     fish = Fish('Карповые', True, 'вода', 'чешуя', 'холоднокровные', 'икра')
#     fish.organ_gills()
#     bird = Birds('Вьюрковые', True, 'наземно-воздушный', 'перья', 'теплокровные', 'яйца')
#     bird.fly()
#     amphibia = Amphibians('Бесхвостые','наземно-водный', 'кожа', 'холоднокровные', 'икра и личинки',True)
#     amphibia.respirator_organ()
#     reptile = Reptiles('Крокодилы', True, 'наземно-водный', 'роговые чешуйки', 'холоднокровные', 'яйца')
#     reptile.crawl_skill()
#     mammal = Mammals('Хищники', True, 'наземно-водный', 'кожа шерсть', 'теплокровные', 'живорождение')
#     mammal.brain_activity()
#     print(mammal.name, mammal.temperature, mammal.habitat, mammal.body_coverings)


class AnimalFabric(Mammals):

    def __init__(self, name=None, habitat=None, body_coverings=None, temperature=None, method_reproduction=None,
                 caring_for_offspring=True):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name, caring_for_offspring)

    def creat(self):
        return f'Животное: название {self.name}, среда обитания - {self.habitat},' \
               f' покровы тела - {self.body_coverings}, температура тела - {self.temperature},' \
               f'способ  репродукции - {self.method_reproduction} '

    def feature(self):
        return f'Особенность класса млекопитающие - забота о потомстве{self.caring_for_offspring}'


if __name__ == '__main__':
    fabric = AnimalFabric(name='Собака', habitat='наземный', body_coverings='шерсть', temperature='теплокровные',
                          method_reproduction='живорождение')
    print(fabric.creat())
    print(fabric.body_coverings)
    print(fabric.feature())
