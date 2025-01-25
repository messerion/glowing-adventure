class Runner:
    def __init__(self, name):

        self.name = name
        self.distance = 0

    def walk(self):

        self.distance += 5

    def run(self):

        self.distance += 10
