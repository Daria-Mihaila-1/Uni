class Gast:
    # Attr: jeder hat Vorname, Nachname, Liste von Reservierungen
    # Methoden: Gaste einfugen, Aktualisierung der Nachname eines Gastes, Löschung eines Gastes,

    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__liste_res = []

    @property
    def vorname(self): return self.__vorname

    @property
    def nachname(self): return self.__nachname

    @property
    def liste_res(self): return self.__liste_res

    @vorname.setter
    def vorname(self, vn):
        self.__vorname = vn

    @nachname.setter
    def nachname(self, nn):
        self.__nachname = nn

    def aktualisiere_nachname(self, newname):
        self.__nachname = newname

    def add_reservierung(self, r):
        self.__liste_res.append(r)

    def __str__(self):
        return f"{self.__vorname}; {self.__nachname}; {self.__liste_res}"

    def __repr__(self):
        return f"({self.__vorname}; {self.__nachname}; {self.__liste_res})"

    def __eq__(self, other):
        if self.__vorname == other.__vorname and self.__nachname == other.__nachname:
            return True
        else:
            return False



