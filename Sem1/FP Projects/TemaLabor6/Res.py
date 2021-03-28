class Reservierung:
    #  Attr: Gäste, ein Zimmer, ein Zeitraum
    # Methoden : Add Gast, Drucken der Liste von Gaste
    def __init__(self, anz_gaste, zimmer, check_in, check_out):
        self.__anz_gaste = anz_gaste
        self.__zimmer = zimmer
        self.__check_in = check_in
        self.__check_out = check_out

    @property
    def anz_gaste(self): return self.__anz_gaste

    @property
    def zimmer(self): return self.__zimmer

    @property
    def check_in(self): return self.__check_in

    @property
    def check_out(self): return self.__check_out

    def __str__(self):
        return f"{self.__anz_gaste}, {self.__zimmer}, {self.__check_in}, {self.__check_out}"

    def __repr__(self):
        return f"{self.__anz_gaste}, {self.__zimmer}, {self.__check_in}, {self.__check_out}"
