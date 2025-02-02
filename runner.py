class Runner:
    def __init__(self, name, speed):

        self.name = name
        self.speed = speed
        self.distance = 0  # пройденная дистанция
        self.race_time = 0  # время забега

    def run(self, time):

        distance_covered = self.speed * time
        self.distance += distance_covered
        self.race_time = time

    def walk(self, time):

        distance_covered = self.speed * 0.5 * time
        self.distance += distance_covered

    def __eq__(self, other):

        if isinstance(other, Runner):
            return self.name == other.name
        return False


class Tournament:
    def __init__(self, distance, runners):

        self.distance = distance
        self.runners = runners

    def start(self):

        results = {}


        sorted_runners = sorted(self.runners, key=lambda x: x.speed, reverse=True)

        for place, runner in enumerate(sorted_runners, 1):
            time = self.distance / runner.speed
            runner.run(time)
            results[place] = runner.name

        return results


import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):

        cls.all_results = {}

    def setUp(self):

        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_usain_nick_race(self):

        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()

        # Сохраняем результаты для вывода в tearDownClass
        self.__class__.all_results[1] = results

    def test_andrey_nick_race(self):

        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()


        self.__class__.all_results[2] = results

    def test_three_runners_race(self):

        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()


        self.__class__.all_results[3] = results


@classmethod
def tearDownClass(cls):

    for key, value in cls.all_results.items():
        print(value)


if __name__ == '__main__':
    unittest.main()
