
class Control:
    def __init__(self, Hotel):
        self.__Hotel = Hotel

    def add_gast(self, gast):
        self.__Hotel.add_gast(gast)

    def akt_nachname(self, gast, newname):
        self.__Hotel.akt_nachname(gast, newname)

    def losche_gast(self, gast):
        self.__Hotel.losche_gast(gast)

    def show_list_gaste(self):
        return self.__Hotel.show_list_gaste()

    def show_list_zim(self):
        return self.__Hotel.show_list_zim()

    def add_zim(self, zim):
        self.__Hotel.add_zim(zim)

    def akt_preis(self, zim_nr, newpreis):
        self.__Hotel.aktualisiere_preis(zim_nr, newpreis)

    def losche_zim(self, zim):
        self.__Hotel.losche_zim(zim)

    def mach_reservierung(self, gast, nr_gaste, check_in, check_out):
        self.__Hotel.mach_res(gast, nr_gaste, check_in, check_out)

    def show_gaste_aktuell(self):
        return self.__Hotel.show_gaste_aktuell()

    def filtere_zimmer(self, meerblick, preis):
        return self.__Hotel.gefilterte_zim(meerblick, preis)

    def zimmer_heute_frei(self):
        return self.__Hotel.zimmer_heute_frei()

    def show_list_res(self):
        return self.__Hotel.show_list_res()