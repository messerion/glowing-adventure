class Runner:
    def __init__(self, name, speed):
        """
        Инициализация бегуна

        :param name: имя бегуна
        :param speed: скорость бегуна
        """
        self.name = name
        self.speed = speed
        self.distance = 0  # пройденная дистанция
        self.race_time = 0  # время забега

    def run(self, time):
        """
        Метод бега с учетом скорости

        :param time: время бега
        """
        distance_covered = self.speed * time
        self.distance += distance_covered
        self.race_time = time

    def walk(self, time):
        """
        Метод ходьбы с учетом скорости

        :param time: время ходьбы
        """
        distance_covered = self.speed * 0.5 * time
        self.distance += distance_covered

    def __eq__(self, other):
        """
        Сравнение бегунов по имени

        :param other: другой бегун
        :return: True, если имена совпадают
        """
        if isinstance(other, Runner):
            return self.name == other.name
        return False


class Tournament:
    def __init__(self, distance, runners):
        """
        Инициализация соревнования

        :param distance: дистанция забега
        :param runners: список бегунов
        """
        self.distance = distance
        self.runners = runners

    def start(self):
        """
        Метод старта соревнования

        :return: словарь результатов
        """
        results = {}

        # Сортировка бегунов по скорости в обратном порядке
        sorted_runners = sorted(self.runners, key=lambda x: x.speed, reverse=True)

        for place, runner in enumerate(sorted_runners, 1):
            time = self.distance / runner.speed
            runner.run(time)
            results[place] = runner.name  # Сохраняем только имя бегуна в результатах

        return results


import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        """Инициализация словаря результатов"""
        cls.all_results = {}

    def setUp(self):
        """Создание бегунов перед каждым тестом"""
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_usain_nick_race(self):
        """Забег Усэйна и Ника"""
        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()

        # Сохраняем результаты для вывода в tearDownClass
        self.__class__.all_results[1] = results

    def test_andrey_nick_race(self):
        """Забег Андрея и Ника"""
        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()

        # Сохраняем результаты для вывода в tearDownClass
        self.__class__.all_results[2] = results

    def test_three_runners_race(self):
        """Забег Усэйна, Андрея и Ника"""
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()

        # Сохраняем результаты для вывода в tearDownClass
        self.__class__.all_results[3] = results


@classmethod
def tearDownClass(cls):
    """Вывод результатов после всех тестов"""
    for key, value in cls.all_results.items():
        print(value)


if __name__ == '__main__':
    unittest.main()
