"""
 Hunger meter:
* meal, която се дава определен брой пъти. Ще се купува с пари от играта от магазин.
* snack - без ограничение.
Ако тамагочио стане прекалено тежко и не спортува, умира.

Happy meter:
* Забавление - mini game - snake. Освен попълване на хепинес метъра, тамагочито олеква, а играта носи пари. Намалява Cleanliness meter.

Clenliness meter:
* Тамагочито се къпе.

Health meter:
* От време на време ще се разболява  и трябва да му се купи лекарство от магазина.
* Ако не се почиства се разболява.
"""

class Tamagotchi:
    STATS = ["food", "happiness", "hygiene", "health", "energy"]
    def __init__(self):
        self.food = 100
        self.happiness = 100
        self.hygiene = 100
        self.health = 100
        self.energy = 100
        self.age = 0
        self.is_sleeping = False

    def constrain(self, value):
        value = min(100, value)
        value = max(0, value)
        return value

    def constrain_stats(self):
        for statistic in self.STATS:
            self.__dict__[statistic] = self.constrain(self.__dict__[statistic])

    # FIXME
    def apply(self, item):
        for statistic in self.STATS:
            self.__dict__[statistic] += item.__dict__[statistic]
        self.constrain_stats()

    def second_pass(self, seconds=1):
        #Енергията става на 0 за 8 часа

        if self.is_sleeping:
            self.energy += seconds * 1 / (8*36)
            is_sleeping = 1;
        else:
            self.energy -= seconds * 1 / (8*36)
        self.hygiene -= seconds * 1 / (8*36)

        #Гладът и щастието стават на 0 за 4 часа
        self.food -= seconds * 1 / (4*36)
        self.happiness -= seconds * 1 / (4*36)

        self.constrain_stats()
