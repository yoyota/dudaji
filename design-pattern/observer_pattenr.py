class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer, modifier=None):
        if observer != modifier:
            try:
                self.observers.remove(observer)
            except ValueError:
                pass

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)


class Data(Subject):

    def __init__(self):
        Subject.__init__(self)
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        self.notify(self._data)


class BinaryPrint:

    def update(self, data):
        print(bin(data))


class DecimalPrint:

    def update(self, data):
        print(data)


subject = Data()
observer1 = BinaryPrint()
observer2 = DecimalPrint()

subject.attach(observer1)
subject.attach(observer2)
subject.data = 2
subject.detach(observer2)
subject.data = 1
subject.detach(observer1)
subject.data = 3
