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
