class Zimmer:
    # Attr:Nummer, Anzahl von möglichen Gästen, Preis, Farbe, kann ein Mehrblick haben oder nicht, frei oder nicht
    # Man kann auch sehen,wenn es frei ist, Aktualisierung Preis

    def __init__(self, nummer, max_anz, preis, farbe, meerblick, frei):
        self.__nummer = nummer
        self.__max_anz = max_anz
        self.__preis = preis
        self.__farbe = farbe
        self.__meerblick = meerblick  # boolean
        self.__frei = frei  # boolean

    @property
    def nummer(self): return self.__nummer

    @property
    def max_anz(self): return self.__max_anz

    @property
    def preis(self): return self.__preis

    @property
    def farbe(self): return self.__farbe

    @property
    def meerblick(self): return self.__meerblick

    @property
    def frei(self): return self.__frei

    @nummer.setter
    def nummer(self, nr):
        self.__nummer = nr

    @max_anz.setter
    def max_anz(self, ma):
        self.__max_anz = ma

    @farbe.setter
    def farbe(self, f):
        self.__farbe = f

    @meerblick.setter
    def meerblick(self, mb):
        self.__meerblick = mb

    @preis.setter
    def preis(self, p):
        self.__preis = p
        if self.__meerblick:
            self.__preis += 100

    @frei.setter
    def set_frei(self, f):
        self.__frei = f

    def aktualisierung(self, p):
        self.__preis = p

    def __str__(self):
        return f"{self.__nummer}, {self.__max_anz}, {self.__preis} $, {self.__farbe}, {self.__meerblick}, {self.__frei}"

    def __repr__(self):
        return f"{self.__nummer}, {self.__max_anz}, {self.__preis} $, {self.__farbe}, {self.__meerblick}, {self.__frei}"


def main():
    z = Zimmer(109, 4, 100, "lila", False, False)
    print(z)
    l = []
    print(z)
    # zim1 = Zimmer(110, 2, 210, "roza", True, True)
    #zim2 = Zimmer(213, 3, 56, "bleu", False, True)
    #print(zim1)
    #print(zim2)

