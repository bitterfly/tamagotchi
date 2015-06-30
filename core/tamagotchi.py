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
from random import randint

class Tamagotchi:
    def __init__(self):
        self.stats = {"food": 100, "happiness": 100, "hygiene": 100,
                 "health": 100, "energy": 100, "age": 0}
        self.is_sleeping = False
        self.is_dead = False
        self.is_playing = False
        self.is_sick = False

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

    def decrease_to_minimum(self, statistic, full_hours, time_given):
        self.stats[statistic] -= (time_given * 1) / (full_hours * 36)

    def increase_to_maximum(self, statistic, full_hours, time_given):
        self.stats[statistic] += (time_given * 1) / (full_hours * 36)

    def random_event(self):
        if(randint(0, 10000) == 0):
            self.is_sick = True
    def cure(self):
        self.is_sick = False

    def second_pass(self, seconds=1):
        "Докато спиш всички статове падат за 8 часа, освен сънят, който се възстановява"
        if self.is_sleeping:
            self.increase_to_maximum("energy", 8, seconds)
            self.decrease_to_minimum("happiness", 12, seconds)
            self.decrease_to_minimum("hygiene", 12, seconds)
            self.decrease_to_minimum("food", 12, seconds)
        else:
            "Докато играеш, повечето статистики падат по-бързо."
            if self.is_playing:
                self.decrease_to_minimum("energy", 3, seconds)
                self.decrease_to_minimum("hygiene", 3, seconds)
                self.decrease_to_minimum("food", 4, seconds)
                self.increase_to_maximum("happiness", 1, seconds)
            else:
                self.decrease_to_minimum("energy", 4, seconds)
                self.decrease_to_minimum("hygiene", 4, seconds)
                self.decrease_to_minimum("food", 4, seconds)
                self.decrease_to_minimum("happiness", 4, seconds)

        if (self.stats["happiness"] <= 50 or
               self.stats["hygiene"] <= 50):
                self.is_sick = True
        if self.is_sick:
            self.decrease_to_minimum("health", 5, seconds)

        self.constrain_stats()

        self.random_event()

        if (self.stats["food"] == 0 or
           self.stats["health"] == 0):
           self.is_dead = True
