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
    def __init__(self):
        self.stats = {"food": 100, "happiness": 100, "hygiene": 100,
                 "health": 100, "energy": 100, "age": 0}
        self.is_sleeping = False
        self.is_dead = False

    def constrain(self, value):
        value = min(100, value)
        value = max(0, value)
        return value

    def constrain_stats(self):
        for statistic, value in self.stats.items():
            self.stats[statistic] = self.constrain(value)

    def apply(self, item):
        for statistic, value in self.stats.items():
            self.stats[statistic] += item.stats[statistic]
        self.constrain_stats()

    def second_pass(self, seconds=1):
        #Енергията става на 0 за 8 часа
        sleep_bonus = 0

        if self.is_sleeping:
            self.stats["energy"] += seconds * 1 / (8*36)
            is_sleeping = 1;
            sleep_bonus = 4
        else:
            self.stats["energy"] -= seconds * 1 / (8*36)
            #Здравето ще пада само в будно състояние, за да не умре,
            #докато спи :Д

            if (self.stats["happiness"] <= 50 or
               self.stats["hygiene"] <= 50):
                self.stats["health"] -= seconds * 1 / (4 * 36)

        self.stats["hygiene"] -= seconds * 1 / ((4 + sleep_bonus) * 36)

        #Гладът и щастието стават на 0 за 4 часа
        #!!! проба
        self.stats["food"] -= seconds * 1 / ((4 + sleep_bonus)*36)
        self.stats["happiness"] -= seconds * 1 / ((4 + sleep_bonus)*36)

        self.constrain_stats()

        if (self.stats["food"] == 0 or
           self.stats["health"] == 0):
           self.is_dead = True
