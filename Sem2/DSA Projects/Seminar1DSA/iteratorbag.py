from bag import bag
class iterator:
    def __init__(self, bag):
        self.__bag = bag
        self.__i = 0
    @property
    def bag(self): return self.__bag

    @property
    def i(self): return self.__i

    def valid(self):
        if self.__i < self.__bag.size():
            return True
        return False

    def first(self):
        if self.__bag:
            self.__i = 0
        else:
            return False

    def next(self):
        try:
            self.__i += 1
        except self.valid():
            print("am iesit din lista")
            raise IndexError

    def getCurrent(self, e):
        try:
            return self.__bag[self.__i]
        except not self.valid():
            print("am iesit din lista")
            raise IndexError()


    def __repr__(self):
        return f"{self.__i}"

