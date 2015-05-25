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
    STATS = ["replete", "happy", "clean", "health", "energy"]
    def __init__():
        self.replete = 100
        self.happy = 100
        self.clean = 100
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

    def apply(self, item):
        self.replete += item.food
        self.happy += item.happiness
        self.clean += item.hygiene
        self.health += item.health
        self.energy += item.energy
        self.constrain_stats()

    def feed(self, food):
        if food.is_snack():
            self.apply(food)
        if self.hunger >=
