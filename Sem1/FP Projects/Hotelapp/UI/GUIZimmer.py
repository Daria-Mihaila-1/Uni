from Entities.Zimmer import Zimmer
from tkinter import *
from tkinter import messagebox


class Third:
    def __init__(self, root_window, controller):
        self.__window = root_window
        self.__controller = controller

        self.__window.title = "Zimmer Menu"
        self.__window.geometry("300x133")
        self.top = Frame(self.__window, bg='light gray')
        self.top.pack(side=LEFT, fill=Y)

        self.btn = Button(self.top, text='Add Zimmer', command=self.add_zim, bg='light gray')
        self.btn.pack(fill=BOTH)

        self.btn1 = Button(self.top, text='Aktualisiere Preis', command=self.akt, bg='light gray')
        self.btn1.pack(fill=BOTH)

        self.btn2 = Button(self.top, text='Losche Zimmer', command=self.losche, bg='light gray')
        self.btn2.pack(fill=BOTH)

        self.btn3 = Button(self.top, text='Siehe Liste von Zimmern', command=self.show_list, bg='light gray')
        self.btn3.pack(fill=BOTH)

        self.btn4 = Menubutton(self.top, text='File Menu', bg='light blue')
        self.btn4.menu = Menu(self.btn4, bg='light blue')
        self.btn4["menu"] = self.btn4.menu
        text ='Menu Zimmer:\n\n' \
               '1.Man kann ein Zimmer in meiner Liste einfugen \n' \
               '2.Man kann den Preis eines Gastes verandern\n' \
               '3.Man kann ein Zimmer loschen\n' \
               '4.Du kannst auch meine Liste sehen wenn du auf "Siehe Liste von Zimmern" druckst'
        self.btn4.menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', text))
        self.btn4.menu.add_command(label='Exit', command=self.__window.destroy)
        self.btn4.pack()

        self.text = Text(self.top)
        self.text.pack(fill=BOTH)
        self.top.pack()

    def save_and_delete(self, funct, l, frame):
        """die Funktion:
        -loscht alle Entry s aus einer Liste l
        -durch den Parameter 'funct' ruft sie eine andere Funktion auf """
        for text_entry in l:
            text_entry.delete(0, 'end')
        messagebox.showinfo('ALLES GUT', 'Die Anderungen wurden gespeichert', parent=frame)

    def error_spaces(self, l, frame):
        for text in l:
            if text.get() == '':
                messagebox.showerror('Error', 'Sie haben nicht alle Attribute geschrieben,'
                                              '\nBitte fühle alle Felder aus!!', parent=frame)
                return False
        return True

    def gute_zahleingabe(self, zahl_entry, entry_name):
        if not zahl_entry.get().isdigit():
            messagebox.showerror('NUR INTEGER', f'Das Feld "{entry_name}" soll eine Zahl sein', parent=self.newframe)
            return False
        return True
    def gute_booleingabe(self, bool_entry, entry_name):
        if bool_entry.get() != 'True' and bool_entry.get() != 'False':
            messagebox.showerror('NICHT BOOLEAN', f'Die Eingaben fur das Feld "{entry_name}" '
                                                  f'soll entweder "True" oder "False" sein', parent=self.newframe)
            return False
        return True
    def add_zim(self):
        self.newwindow = Toplevel(self.top, bg='light gray')
        self.newframe = Frame(self.newwindow, bg='light gray')
        self.newwindow.title('Add Zimmer')
        self.newframe.pack(side=LEFT,  expand=1)

        Label(self.newframe, text='schreibe hier die Eigenschaften des Zimmers', bg='light gray').grid(column=1, row=0)

        self.zim_nr_txt = Entry(self.newframe, width=50)
        self.zim_max_anz_txt = Entry(self.newframe, width=50)
        self.zim_preis_txt = Entry(self.newframe, width=50)
        self.zim_farbe_txt = Entry(self.newframe, width=50)
        self.zim_meerblick_txt = Entry(self.newframe, width=50)
        self.zim_frei_txt = Entry(self.newframe, width=50)

        l = [self.zim_nr_txt, self.zim_max_anz_txt, self.zim_preis_txt, self.zim_farbe_txt, self.zim_meerblick_txt,
             self.zim_frei_txt]

        Label(self.newframe, text='Nummer:', bg='light gray').grid(column=0, row=1)
        self.zim_nr_txt.grid(column=1, row=1)
        Label(self.newframe, text='Max Anz Pers:', bg='light gray').grid(column=0, row=2)
        self.zim_max_anz_txt.grid(column=1, row=2)
        Label(self.newframe, text='Preis:\n(Die Default-Wahrung ist $)', bg='light gray').grid(column=0, row=3)
        self.zim_preis_txt.grid(column=1, row=3)
        Label(self.newframe, text='Farbe:', bg='light gray').grid(column=0, row=4)
        self.zim_farbe_txt.grid(column=1, row=4)
        Label(self.newframe, text='Meerblick(True or False):', bg='light gray').grid(column=0, row=5)
        self.zim_meerblick_txt.grid(column=1, row=5)
        Label(self.newframe, text='Freiheit(True or False):', bg='light gray').grid(column=0, row=6)
        self.zim_frei_txt.grid(column=1, row=6)

        btn1 = Button(self.newframe, text='save changes',
                          command=lambda: self.save_and_delete(self.__controller.add_zim(Zimmer(self.zim_nr_txt.get(),
                                    self.zim_max_anz_txt.get(), self.zim_preis_txt.get(), self.zim_farbe_txt.get(),
                                    self.zim_meerblick_txt.get(), self.zim_frei_txt.get())), l, self.newframe)
                          if self.error_spaces(l, self.newframe) and self.gute_zahleingabe(self.zim_nr_txt, 'Nummer')
                          and self.gute_zahleingabe(self.zim_max_anz_txt, 'Max Anz Pers')
                          and self.gute_zahleingabe(self.zim_preis_txt, 'Preis')
                          and self.gute_booleingabe(self.zim_meerblick_txt, 'Meerblick')
                          and self.gute_booleingabe(self.zim_frei_txt, 'Freiheit')else False)

        btn1.grid(column=1, row=8)
        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=9)

    def show_list(self):
        self.newwindow = Toplevel(bg='light gray')
        self.newwindow.geometry('500x300')
        self.newwindow.title('SHOW ODATA')
        self.newframe = Frame(self.newwindow, bg='light gray')
        self.newframe.pack()

        list = self.__controller.show_list_zim()
        numar = 1
        for el in range(len(list)):
            Label(self.newframe, text='Zimmer #' + str(numar) + '\n' + 'Nummer:' + str(list[el].nummer) +
                                      ', Max-Anz:' + str(list[el].max_anz) + ', Preis:' + str(list[el].preis) + '$' +
                                      ', Farbe:' + str(list[el].farbe) + ', Meerblick:' + str(list[el].meerblick) +
                                                                            ', Freiheit:' + str(list[el].frei),
                  bg='light gray').pack()
            numar += 1
        btn = Button(self.newframe, text='Ok', command=self.newwindow.destroy)
        btn.pack()

    def losche(self):

        self.newwindow = Toplevel(bg='light gray')
        self.newwindow.title('LOSCHE ODATA')
        self.newframe = Frame(self.newwindow, bg='light gray')
        self.newframe.pack()

        Label(self.newframe, text='schreibe hier die Nummer des Zimmers das du loschen willst',
              bg='light gray').grid(column=1, row=0)

        self.zim_nr_txt = Entry(self.newframe, width=50)

        Label(self.newframe, text='Nummer:', bg='light gray').grid(column=0, row=1)
        self.zim_nr_txt.grid(column=1, row=1)
        l = [self.zim_nr_txt]
        btn1 = Button(self.newframe, text='remove',
                      command=lambda: self.save_and_delete(self.__controller.losche_zim(
                            self.zim_nr_txt.get()), l, self.newframe) if self.error_spaces(l, self.newframe) else False)
        btn1.grid(column=1, row=2)
        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=3)

    def aktualisiere_preis(self, window2):
        self.newwindow = Toplevel(window2, bg='light gray')
        self.newwindow.title('AKTUALISIERE ODATA')
        self.newframe_main = Frame(self.newwindow, bg='light gray')
        self.newframe_main.pack()
        Label(self.newframe_main,
              text='schreibe hier die Nummer des Zimmers dessen Preis du aktualisieren willst und danach den neuen Preis'
              , bg='light gray').grid(column=1, row=0)

        self.zim_nr_txt = Entry(self.newframe_main, width=50)
        self.newpreis_txt = Entry(self.newframe_main, width=50)
        Label(self.newframe_main, text='Nummer:', bg='light gray').grid(column=0, row=1)
        self.zim_nr_txt.grid(column=1, row=1)
        Label(self.newframe_main, text='Neuer Preis:', bg='light gray').grid(column=0, row=2)
        self.newpreis_txt.grid(column=1, row=2)

        l = [self.zim_nr_txt, self.newpreis_txt]

        btn1 = Button(self.newframe_main, text='aktualisiere Preis', command=lambda: self.save_and_delete(
            self.__controller.akt_preis(self.zim_nr_txt.get(), self.newpreis_txt.get()), l, self.newframe_main)
        if self.error_spaces(l, self.newframe_main) else False)
        btn1.grid(column=1, row=3)

        btn = Button(self.newframe_main, text='zuruck', command=window2.destroy)
        btn.grid(column=1, row=4)

    def akt(self):
        self.window_to_show_zim = Toplevel(bg='light gray')
        self.newframe_second = Frame(self.window_to_show_zim, bg='light gray')
        self.newframe_second.pack()

        Label(self.newframe_second, text='Hier kannst du dir noch einmal alle Zimmern mit ihren Preisen anschauen\n'
                                            'wahle dir das Zimmer dessen Nummer du andern willst und drucke danach '
                                            'auf weiter:)', bg='light gray').pack(side=TOP)

        list = self.__controller.show_list_zim()
        numar = 1
        for el in range(len(list)):
            Label(self.newframe_second, text=str(numar) + '.' + 'Nummer:' + str(list[el].nummer) +
                                      ', Max-Anz:' + str(list[el].max_anz) + ', Preis:' + str(list[el].preis) + '$' +
                                      ', Farbe:' + str(list[el].farbe) + ', Meerblick:' + str(list[el].meerblick) +
                                      ', Freiheit:' + str(list[el].frei),
                  bg='light gray').pack()
            numar += 1

        btn_weiter = Button(self.newframe_second, text="weiter", command=lambda:
        self.aktualisiere_preis(self.window_to_show_zim))
        btn_weiter.pack()

        btn_escape = Button(self.newframe_second, text='zuruck', command=self.window_to_show_zim.destroy)
        btn_escape.pack()