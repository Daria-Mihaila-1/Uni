class bag:
    def __init__(self):
        self.__l = []

    @property
    def l(self): return self.l

    def add(self, e):
        self.__l.append(e)

    def remove(self, e):
        for i in self.__l:
            if i == e:
                self.__l.remove(e)
                return True

        return False

    def search(self, e):
        for i in self.__l:
            if i == e:
                return True
        return False

    def size(self): return len(self.__l)

    def nrOccurrences(self, e):
        contor = 0
        for i in self.__l:
            if i == e:
                contor += 1
        return contor

    def __repr__(self):
        return f"{self.__l}"

