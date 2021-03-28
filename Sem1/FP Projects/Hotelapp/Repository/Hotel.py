from Entities.Gast import *
from Entities.Zimmer import *
from Entities.Reservierung import *
import datetime
from  tkinter import filedialog

class Hotel:  # lucrez cu lista de clienti + lista de camere

    def __init__(self, file3=r'C:\Users\Daria\OneDrive\Desktop\Res.txt', file1=r'C:\Users\Daria\OneDrive\Desktop\Gaste.txt', file2=r'C:\Users\Daria\OneDrive\Desktop\Zimmer.txt'):
        self.__file1_name = file1
        self.__file2_name = file2
        self.__file3_name = file3
        self.__lst_gaste = []
        self.__lst_zim = []
        self.__lst_res = []
        self.load_from_file_gaste()
        self.load_from_file_zim()
        self.load_from_file_res()



    def pick_file(self, file_name):
        return filedialog.askopenfilename(initialdir=r"C:\Users\Daria\OneDrive\Desktop",
                               title=f'Select the input file for {file_name}', filetype=
                               (("Text files", "*.txt"),
                                ("All files", "*.*")))

    def store_to_file(self, lst, file_name):

        file = open(file_name, "w")

        for el in lst:  #  self.__lst_gaste:
            file.write(str(el) + "\n")


    def load_from_file_gaste(self):  # din fisier pun ori in lista de musafiri ori in cea de camere

        lst = []
        file = open(self.__file1_name, "r")
        for line in file:

            if line != "\n":
                data = line.strip().split(';')
                gast = Gast(data[0], data[1].strip())

                lst_res = data[2].replace(']', '').replace('[', '').replace('(', '').replace(')', '').split(',')

                for info in range(0, len(lst_res)-3, 4):

                    checkin = datetime.datetime.strptime(lst_res[info + 2].strip(), "%Y-%m-%d")
                    checkout = datetime.datetime.strptime(lst_res[info+3].strip(), "%Y-%m-%d")
                    res = Reservierung(int(lst_res[info]), int(lst_res[info+1]),
                                       checkin.date(),
                                       checkout.date())
                    gast.add_reservierung(res)
                # print(gast)
                lst.append(gast)

        file.close()
        self.__lst_gaste = lst

    def load_from_file_zim(self):  #din fisier pun ori in lista de musafiri ori in cea de camere
        lst = []
        file = open(self.__file2_name, "r")
        for line in file:
            data = line.strip().split(',')  # data = [lst_gaste, lst_zimm]
            zim = Zimmer(int(data[0]), int(data[1]), int(data[2].replace('$', "").strip()), data[3].strip(), bool(data[4]), bool(data[5]))
            lst.append(zim)

        file.close()
        self.__lst_zim = lst


    def load_from_file_res(self):  # din fisier pun ori in lista de musafiri ori in cea de camere

        lst = []
        file = open(self.__file3_name, "r")
        for line in file:

            if line != "\n":
                data = line.strip().split(',')

                res = Reservierung(int(data[0]), int(data[1]), datetime.datetime.strptime(data[2].strip(), '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(data[3].strip(), '%Y-%m-%d').date())
                lst.append(res)
        self.__lst_res = lst
        file.close()

    def find(self, lst, gast):
        for e in lst:
            if gast == e:
                return e

        return None

    def add_gast(self, gast):
            self.__lst_gaste.append(gast)
            self.store_to_file(self.__lst_gaste, self.__file1_name)

    def akt_nachname(self, oldgast, newgast):

        el = self.find(self.__lst_gaste, oldgast)

        if el is None:
            print("false")
        else:
            idx = self.__lst_gaste.index(el)
            self.__lst_gaste.pop(idx)
            # self.__data.remove(el)

            self.__lst_gaste.insert(idx, newgast)
            # self.__data.insert(-1, uni)

            self.store_to_file(self.__lst_gaste, self.__file1_name)

    def losche_gast(self, gast_zum_loschen):

        for gast in self.__lst_gaste:

            if gast_zum_loschen.vorname == gast.vorname and gast_zum_loschen.nachname == gast.nachname:

                self.__lst_gaste.remove(gast)
                if gast.liste_res:
                    for reserv in range(len(gast.liste_res)):

                        for r in range(len(self.__lst_res)):

                            if gast.liste_res[reserv] == self.__lst_res[r]:
                                self.__lst_res.pop(r)
                                break

        self.store_to_file(self.__lst_gaste, self.__file1_name)
        self.store_to_file(self.__lst_res, self.__file3_name)

    def show_list_gaste(self):

        return self.__lst_gaste
    # ------------------------------------------------------------------------------------------------------------------

    def add_zim(self, zim):
        self.__lst_zim.append(Zimmer(zim.nummer, zim.max_anz, zim.preis, zim.farbe, zim.meerblick, zim.frei))

        self.store_to_file(self.__lst_zim, self.__file2_name)

    def show_list_zim(self):

        return self.__lst_zim

    def losche_zim(self, zim_zum_loschen):

        for zim in self.__lst_zim:

            if zim.nummer == int(zim_zum_loschen):

                self.__lst_zim.remove(zim)
                for reserv in range(len(self.__lst_res)):

                    if int(zim_zum_loschen) == self.__lst_res[reserv].zimmer:

                        self.__lst_res.pop(reserv)
                        break

        self.store_to_file(self.__lst_zim, self.__file2_name)

    def aktualisiere_preis(self, nr, newpreis):

        found = False
        for zim in self.__lst_zim:
            if zim.nummer == int(nr):
                found = True
                el = zim
                break
        if not found:
            pass
        else:
            idx = self.__lst_zim.index(el)
            self.__lst_zim[idx].preis = int(newpreis)
            self.store_to_file(self.__lst_zim, self.__file2_name)
# ----------------------------------------------------------------------------------------------------------------------

    def mach_res(self, gast, nr_gaste, check_in, check_out):
        made = False
        nr_ok = False
        period_ok = True
        check_in = datetime.datetime.strptime(check_in.strip(), '%Y-%d-%m').date()
        check_out = datetime.datetime.strptime(check_out.strip(), '%Y-%d-%m').date()

        for zim in range(len(self.__lst_zim)):
            # caut in lista de camere o camera libera pe perioada check_in - check_out pt gast

            if int(nr_gaste) <= int(self.__lst_zim[zim].max_anz):  # trebuie sa fie si destul de incapatoare camera
                nr_ok = True

                if not self.__lst_res:  # nu este nici o rezervare facuta ==> se face o rezervare instant

                    neue_res = Reservierung(nr_gaste, self.__lst_zim[zim].nummer, check_in, check_out)
                    # print(neue_res)
                    self.__lst_res.append(neue_res)
                    made = True
                    break

                else:
                    period_ok = False  # presupunem ca pe perioada dorita nu e libera camera
                    found = False  # se testeaza cazul cand lista de rezervari nu e goala dar nici camera
                    # aleasa pe criteriul de capacitate nu e in lista de rezervari
                    for r in range(len(self.__lst_res)):
                        # in lista de rezervari verificam daca pe perioada dorita
                        # este sau nu vreo rezervare facuta pe camera self.__lst_zim[zim]

                        if self.__lst_res[r].zimmer == self.__lst_zim[zim].nummer:
                            # print('ci= ',check_in,' sco= ' ,self.__lst_res[r].check_out,' co= ', check_out,' sci=' ,self.__lst_res[r].check_in)
                            if (check_in >= self.__lst_res[r].check_out) or (check_out <= self.__lst_res[r].check_in):
                                # print('jaaa')
                                neue_res = Reservierung(nr_gaste, self.__lst_zim[zim].nummer,
                                                        check_in,
                                                        check_out)
                                self.__lst_res.append(neue_res)
                                period_ok = True  # daca se poate face rezervarea atunci camera e libera pe perioada data
                                made = True
                            found = True
                            break

                    if not found:
                        neue_res = Reservierung(nr_gaste, self.__lst_zim[zim].nummer, check_in, check_out)

                        self.__lst_res.append(neue_res)
                        made = True
                        period_ok =True

                break

        if made:
            # daca se poate face rezervarea verificam daca gast este un client vechi sau unul nou

            # print(f"Reservierung für {gast.vorname, gast.nachname} gemacht")

            inlist = False

            for g in range(len(self.__lst_gaste)):

                if self.__lst_gaste[g] == gast:
                    self.__lst_gaste[g].add_reservierung(neue_res)

                    inlist = True
                    break

            if not inlist:

                gast.add_reservierung(neue_res)

                self.add_gast(gast)

        else:
            if not nr_ok:
                # print('Ihr seid leider zu viele, wir haben kein Zimmer mit so viele Platze')
                raise OverflowError('ihr seid leider zu viele://')


        self.store_to_file(self.__lst_gaste, self.__file1_name)
        self.store_to_file(self.__lst_res, self.__file3_name)

    def show_gaste_aktuell(self):

        heute = datetime.datetime.now()
        nr = 0
        l = []
        for gast in range(len(self.__lst_gaste)):

            if self.__lst_gaste[gast].liste_res:  # verificam daca un client "gast" are sau nu rezervari facute

                liste_r = self.__lst_gaste[gast].liste_res

                for r in range(len(liste_r)):  # cautam in lista lui de rezervari minim o rezervare actuala

                    if (heute.date() >= liste_r[r].check_in) and (heute.date() <= liste_r[r].check_out):
                        nr += 1
                        l.append(self.__lst_gaste[gast])
                        break

        return l

    def gefilterte_zim(self, meerblick, preis):
        lz = []
        mb = meerblick.lower()
      # doar daca e gasita o camera care sa indeplineasca criteriul de pret,
        # in caz ca utilizatorul vrea o camera cu meerblick, se intreaba utilizatorul daca ar fi posibil sa renunte
        # la meerblick

        ok = False
        while not ok:
            if mb == 'nein':
                mb = False
                ok = True
            elif mb == 'ja':
                mb = True
                ok = True
            else:
                break
        p = int(preis)
        for zimmer in self.__lst_zim:

            if zimmer.preis <= p:
                zpreis_found = True
                if zimmer.meerblick == mb:
                    lz.append(zimmer)
        return lz

    def zimmer_heute_frei(self):
        heute = datetime.datetime.now()
        l = []

        for zimmer in range(len(self.__lst_zim)):  # caut in lista de camere pe cele care sa fie libera azi

            inlist = False

            for r in range(len(self.__lst_res)):  # caut in lista de rezervari toate rezervarile pe camera
                # self.__lst_zim[zimmer]

                if self.__lst_res[r].zimmer == self.__lst_zim[zimmer].nummer:
                    inlist = True

                    if (heute.date() < self.__lst_res[r].check_in) or (heute.date() > self.__lst_res[r].check_out):
                        # daca pt o rezervare pe camera self.__lst_zim[zimmer] data de azi e mai mica decat data de
                        # checkin sau mai mare decat data de checkout atunci camera e azi libera
                        l.append(self.__lst_zim[zimmer])

                    else:
                        if self.__lst_zim[zimmer] in l:
                            while self.__lst_zim[zimmer] in l:
                                l.remove(self.__lst_zim[zimmer])
            if not inlist:
                l.append(self.__lst_zim[zimmer])

        return l

    def show_list_res(self):
        return self.__lst_res

    def __str__(self):
        return f'{self.__lst_gaste}, {self.__lst_zim}, {self.__lst_res}'

    def __repr(self):
        return f'{self.__lst_gaste}, {self.__lst_zim}, {self.__lst_res}'