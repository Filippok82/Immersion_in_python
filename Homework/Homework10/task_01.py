"""Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе
переданного типа и верните его из класса-фабрики."""


class Animals:
    def __init__(self, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str, name: str):
        """место обитания,покровы тела,температура,способ размножения"""
        self.habitat = habitat
        self.body_coverings = body_coverings
        self.temperature = temperature
        self.method_reproduction = method_reproduction
        self.name = name


class Insects(Animals):
    """Насекомые"""

    def __init__(self, name: str, body_structure: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.body_structure = body_structure


class Fish(Animals):
    """Рыбы"""

    def __init__(self, name: str, gills: bool, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.gills = gills

    def organ_gills(self):
        print('Наличие жаберного дыхания')


class Birds(Animals):
    """Птицы"""

    def __init__(self, name: str, flight: bool, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.flight = flight


class Amphibians(Animals):
    """Земноводные"""

    def __init__(self, name: str, respiratory: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.respiratory = respiratory


class Reptiles(Animals):
    """Пресмыкающиеся"""

    def __init__(self, name: str, crawl: str, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.crawl = crawl


class Mammals(Animals):
    """Млекопитающие"""

    def __init__(self, name: str, caring_for_offspring: bool, habitat: str, body_coverings: str, temperature: str,
                 method_reproduction: str):
        super().__init__(habitat, body_coverings, temperature, method_reproduction, name)
        self.caring_for_offspring = caring_for_offspring


f = Fish('Карповые', True, 'вода', 'чешуя', 'холоднокровные', 'икра')
f.organ_gills()
print(f.name)