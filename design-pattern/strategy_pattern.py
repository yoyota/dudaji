import types


class StrategyPattern():
    def __init__(self, fn=None):
        self.name = "example"

        if fn is not None:
            self.excute = types.MethodType(fn, self)

    def excute(self):
        print(self.name + "  original")


def sample1(self):
    print(self.name + "sample1")


def sample2(self):
    print(self.name + "sample2")


strategy = StrategyPattern()
strategy1 = StrategyPattern(sample1)
strategy2 = StrategyPattern(sample2)

strategy.excute()
strategy1.excute()
strategy2.excute()



