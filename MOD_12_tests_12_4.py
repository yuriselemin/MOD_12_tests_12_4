import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest:
    def test_walk(self):
        try:
            runner = Runner('John', -5)
            runner.walk()
            logging.info('test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', str(e))

    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info('test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner: %s', str(e))

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        encoding='utf-8',
                        format='%(asctime)s |  %(levelname)s | %(message)s')

    first = Runner('Вася', 10)
    second = Runner('Илья', 5)
    third = Runner('Арсен', 10)

    t = Tournament(101, first, second)
    print(t.start())

    test = RunnerTest()
    test.test_walk()
    test.test_run()