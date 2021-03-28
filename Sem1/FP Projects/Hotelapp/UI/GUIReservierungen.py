from Entities.Gast import Gast
from tkinter import *
from tkinter import messagebox
import datetime

"""
Mach eine Reservierung•
Anzeige die Liste von Gästen, die aktuelle Reservierungen haben
•Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien 
Anzeige alle Zimmer, die heute frei sind"""


class Fourth:
    def __init__(self,  root_window, controller):
        self.__window = root_window
        self.__controller = controller

        self.__window.title = "Reservierungen Menu"
        self.__window.geometry("390x160")
        self.top = Frame(self.__window, bg='MistyRose2')
        self.top.pack(side=LEFT, fill=Y)

        self.btn = Button(self.top, text='Mach Reservierung', command=self.mach_res, bg='MistyRose2')
        self.btn.pack(fill=BOTH)

        self.btn1 = Button(self.top, text='Liste von Gästen mit aktuellen Reservierungen', command=self.show_gaste_aktuell, bg='MistyRose2')
        self.btn1.pack(fill=BOTH)

        self.btn2 = Button(self.top, text='Zeige alle Zimmer gefiltert mit meine Preis- und Meerblickkriterien',
                           command=self.filtere_zim, bg='MistyRose2')
        self.btn2.pack(fill=BOTH)

        self.btn3 = Button(self.top, text='Anzeige alle Zimmer, die heute frei sind', command=self.zim_heute_frei, bg='MistyRose2')
        self.btn3.pack(fill=BOTH)

        self.btn4 = Button(self.top, text='Siehe Liste von Reservierungen', command=self.show_list, bg='MistyRose2')
        self.btn4.pack(fill=BOTH)

        self.btn5 = Menubutton(self.top, text='File Menu', bg='light blue')
        self.btn5.menu = Menu(self.btn5, bg='light blue')
        self.btn5["menu"] = self.btn5.menu
        text ='Menu Res:\n\n' \
               ' 1.Du kannst dir eine Reservierung hier machen \n' \
               '2.Man kann alle Gaste mit aktuellen Reservierungen sehen\n' \
               '3.Man kann die Zimmer filtern mit Preis- und Meerblickkriterien \n' \
               '4.Man kann sehen welche Zimmer heute frei sind sehen' \
               '5.Du kannst auch meine Liste sehen wenn du auf "Siehe Liste von Reservierungen" druckst\n'
        self.btn5.menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', text))
        self.btn5.menu.add_command(label='Exit', command=self.__window.destroy)
        self.btn5.pack()

        self.text = Text(self.top)
        self.text.pack(fill=BOTH)
        self.top.pack()

    def save_and_delete_special(self, funct, l, frame):
        """die Funktion:
        -loscht alle Entry s aus einer Liste l
        -durch den Parameter 'funct' ruft sie eine andere Funktion auf
         - wird nur bei der Funkt "mach_res" benutzt und es zeigt dem Benutzer auch eine Nachricht"""
        for text_entry in l:
            text_entry.delete(0, 'end')

        messagebox.showinfo('ALLES GUT', 'Deine Reservierung wurde gemacht\n See you soon :)', parent=frame)


    def save_and_delete(self, funct, l):
        """die Funktion:
        -loscht alle Entry s aus einer Liste l
        -durch den Parameter 'funct' ruft sie eine andere Funktion auf """
        for text_entry in l:
            text_entry.delete(0, 'end')

    def error_spaces(self, l, frame):
        ok = True
        for text in l:
            if text.get() == '':
                messagebox.showerror('Error', 'Sie haben nicht alle Attribute geschrieben,'
                                              '\nBitte fühle alle Felder aus!!', parent=frame)
                # ok = False
                return False
        # if ok:
        #    if OverflowError('ihr seid leider zu viele://'):
        #        messagebox.showerror('Error', 'ihr seid leider zu viele', parent=frame)
        return True

    def gute_meerblickeingabe(self, meerblick_entry):

        if meerblick_entry.get().strip().lower() != 'ja' and meerblick_entry.get().strip().lower() != 'nein':
            messagebox.showerror('Ich verstehe nicht',
                                 'Leider verstehe ich dich nicht'
                                 '\nMerke, dass ich nur deutsch verstehe und die Antwort soll entweder "ja" oder "nein" sein',
                                 parent=self.newframe)
            return False
        return True

    def gute_zahleingabe(self, zahl_entry, name_entry):
        if not zahl_entry.get().isdigit():
            messagebox.showerror('NUR INTEGER', f'Das Feld "{name_entry}" soll eine Zahl sein', parent=self.newframe)
            return False
        return True

    def gute_data_eingabe(self, date_entry, entry_name):
        try:
            data = datetime.datetime.strptime(date_entry.get(), '%Y-%d-%m')
        except ValueError:
            messagebox.showerror('DATA TYPE', f'Das Feld "{entry_name}" muss der Art YYYY-DD-MM sein', parent=self.newframe)
            return False
        return True



    def mach_res(self):
        self.newwindow = Toplevel(bg='MistyRose2')
        self.newwindow.geometry('500x300')
        self.newwindow.title('MACH RESERVIERUNG')
        self.newframe = Frame(self.newwindow, bg='MistyRose2')
        self.newframe.pack()

        self.vorname_txt = Entry(self.newframe, width=50)
        self.nachname_txt = Entry(self.newframe, width=50)
        self.anz_pers_txt = Entry(self.newframe, width=50)
        self.checkin_txt = Entry(self.newframe, width=50)
        self.checkout_txt = Entry(self.newframe, width=50)

        Label(self.newframe, text='Schreibe hier deine Daten',  bg='MistyRose2').grid(column=1, row=0)
        Label(self.newframe, text='Vorname:',  bg='MistyRose2').grid(column=0, row=1)
        self.vorname_txt.grid(column=1, row=1)
        Label(self.newframe, text='Nachname:',  bg='MistyRose2').grid(column=0, row=2)
        self.nachname_txt.grid(column=1, row=2)
        Label(self.newframe, text='Wie viele seid ihr?:',  bg='MistyRose2').grid(column=0, row=3)
        self.anz_pers_txt.grid(column=1, row=3)
        Label(self.newframe, text='Check-in:',  bg='MistyRose2').grid(column=0, row=4)
        Label(self.newframe, text='(mit dem Format: YYYY-DD-MM)', fg='gray',  bg='MistyRose2').grid(column=0, row=5)
        self.checkin_txt.grid(column=1, row=4)
        Label(self.newframe, text='Check_out:',  bg='MistyRose2').grid(column=0, row=6)
        Label(self.newframe, text='(mit dem Format: YYYY-DD-MM)', fg='gray',  bg='MistyRose2').grid(column=0, row=7)
        self.checkout_txt.grid(column=1, row=6)

        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=8)
        l = [self.checkout_txt, self.checkin_txt, self.vorname_txt, self.nachname_txt, self.anz_pers_txt]
        btn1 = Button(self.newframe, text='mach Reservierung', command=lambda: self.save_and_delete_special(
            self.__controller.mach_reservierung(Gast(self.vorname_txt.get(), self.nachname_txt.get()),
                                                self.anz_pers_txt.get(), self.checkin_txt.get(),
                                                self.checkout_txt.get()), l, self.newframe)
        if self.error_spaces(l, self.newframe) and self.gute_zahleingabe(self.anz_pers_txt, 'Wie viele seid ihr?')
        and self.gute_data_eingabe(self.checkin_txt, "Checkin") and self.gute_data_eingabe(self.checkout_txt, "Checkout")
        else False)
        btn1.grid(column=1, row=7)

    def show_gaste_aktuell(self):
        self.newwindow = Toplevel(bg='MistyRose2')
        self.newwindow.geometry('500x300')
        self.newwindow.title('Gaste Aktuell')
        self.newframe = Frame(self.newwindow, bg='MistyRose2')
        self.newframe.pack()

        lst_aktuell = self.__controller.show_gaste_aktuell()
        if not lst_aktuell:
            Label(self.newframe, text='Heute sind keine Gaste bei uns untergebracht:/',  bg='MistyRose2').pack()
        else:
            for el in range(len(lst_aktuell)):
                Label(self.newframe, text=str(lst_aktuell[el]) + '\n', bg='MistyRose2').pack()

        btn = Button(self.newframe, text='Ok', command=self.newwindow.destroy)
        btn.pack()

    def filtere_zim(self):
        self.newwindow =Toplevel( bg='MistyRose2')
        self.newwindow.title('Filtere meine Zimmer')
        self.newwindow.geometry('500x200')
        self.newframe = Frame(self.newwindow, bg='MistyRose2')
        self.newframe.pack()

        self.meerblick_txt = Entry(self.newframe, width=50)
        self.preis_txt = Entry(self.newframe, width=50)
        Label(self.newframe, text='schreibe hier ob du Meerblick bei deinem Zimmer willst:',  bg='MistyRose2').pack()
        self.meerblick_txt.pack(pady=10)
        Label(self.newframe, text='schreibe hier der maximale Preis den das Zimmer haben kann:',  bg='MistyRose2').pack()
        self.preis_txt.pack()

        l = [self.meerblick_txt, self.preis_txt]

        btn1 = btn1 = Button(self.newframe, text='Filtere', command=lambda:
        self.save_and_delete(self.filter_away(self.meerblick_txt.get(), self.preis_txt.get()), l)
        if self.error_spaces(l, self.newframe) and self.gute_meerblickeingabe(self.meerblick_txt)
           and self.gute_zahleingabe(self.preis_txt, 'Preis') else False)
        btn1.pack()

        btn = btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.pack()

    def filter_away(self, entry_meerblick, entry_preis):

        lst_gefiltert = self.__controller.filtere_zimmer(entry_meerblick, entry_preis)
        if not lst_gefiltert:
            messagebox.showerror('No matches', 'wir haben keine solche zimmer', parent=self.newframe)
        else:
            self.newwindow_second = Toplevel( bg='MistyRose2')
            self.newframe_second = Frame(self.newwindow_second,  bg='MistyRose2')
            self.newframe_second.pack()
            self.newwindow_second.title('Gefilterte Zimmer')
            self.newwindow_second.geometry('600x400')
            numar = 1
            for el in range(len(lst_gefiltert)):
                Label(self.newframe_second, text=str(numar) + '.' + '\n' + 'Nummer:' + str(lst_gefiltert[el].nummer) +
                                          ', Max-Anz:' + str(lst_gefiltert[el].max_anz) + ', Preis:' + str(
                    lst_gefiltert[el].preis) + '$' +
                                          ', Farbe:' + str(lst_gefiltert[el].farbe) + ', Meerblick:' + str(lst_gefiltert[el].meerblick) +
                                          ', Freiheit:' + str(lst_gefiltert[el].frei),  bg='MistyRose2').pack()
                numar += 1

    def zim_heute_frei(self):
        lst_zim = self.__controller.zimmer_heute_frei()
        if not lst_zim:
            messagebox.showerror('No matches', 'wir haben heute keine freie Zimmer', parent=self.__window)
        else:
            self.newwindow = Toplevel(bg='MistyRose2')
            self.newframe = Frame(self.newwindow,  bg='MistyRose2')
            self.newframe.pack()
            self.newwindow.geometry('500x300')
            self.newwindow.title('Zimmer heute frei')
            num = 1
            for el in range(len(lst_zim)):
                Label(self.newframe, text= str(num)+'\n' + 'Nummer:' + str(lst_zim[el].nummer) +
                ', Max-Anz:' + str(lst_zim[el].max_anz) + ', Preis:' + str(
                    lst_zim[el].preis) + '$' +
                ', Farbe:' + str(lst_zim[el].farbe) + ', Meerblick:' + str(lst_zim[el].meerblick) +
                ', Freiheit:' + str(lst_zim[el].frei),  bg='MistyRose2').pack()
                num += 1

            btn = Button(self.newframe, text='Ok', command=self.newwindow.destroy)
            btn.pack()

    def show_list(self):
        self.newwindow = Toplevel(bg='MistyRose2')
        self.newwindow.geometry('600x300')
        self.newwindow.title('SHOW ODATA')
        self.newframe = Frame(self.newwindow,  bg='MistyRose2')
        self.newframe.pack()

        list = self.__controller.show_list_res()
        if not list:
            Label(self.newframe, text='keine Reservierungen wurden gemacht',  bg='MistyRose2').pack()
        else:
            numar = 1
            for el in range(len(list)):
                Label(self.newframe, text=str(numar) + '. ' + 'Anz Personen:' + str(list[el].anz_gaste) +
                                          ', Zimmernr:' + str(list[el].zimmer) + ', Checkin-date:'
                                          + str(list[el].check_in) + ', Checkout-date:'
                                          + str(list[el].check_out),  bg='MistyRose2').pack()
                numar += 1
        btn = Button(self.newframe, text='Ok', command=self.newwindow.destroy)
        btn.pack()
