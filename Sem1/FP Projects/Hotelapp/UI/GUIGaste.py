from tkinter import *
from tkinter import messagebox
from Repository.Hotel import *



class Second:

    def __init__(self, window, controller):
        self.__controller = controller
        self.__window = window
        self.__window.geometry('300x133')

        self.top = Frame(self.__window, bg='light goldenrod')
        self.top.pack(side=LEFT, fill=Y)
        # my_menu = Menu(self.top)

        self.btn = Button(self.top, text='Add Gast', command=self.add_gast, bg='light goldenrod')
        self.btn.pack(fill=BOTH)

        self.btn1 = Button(self.top, text='Aktualisiere Nachname', command=self.akt_nachname, bg='light goldenrod')
        self.btn1.pack(fill=BOTH)

        self.btn2 = Button(self.top, text='Losche Gast', command=self.losche_gast, bg='light goldenrod')
        self.btn2.pack(fill=BOTH)

        self.btn3 = Button(self.top, text='Siehe Liste Von Gaste', command=self.show_list, bg='light goldenrod')
        self.btn3.pack(fill=BOTH)

        self.btn4 = Menubutton(self.top, text='File Menu', bg='light blue')
        self.btn4.menu = Menu(self.btn4, bg='light blue')
        self.btn4["menu"] = self.btn4.menu
        text = 'Menu Gaste:\n\n' \
               '1.Man kann einen Gast in meiner Liste einfugen \n' \
               '2.Man kann den Nachnamen eines Gastes verandern\n' \
               '3.Man kann einen Gast loschen\n' \
               '4.Du kannst auch meine Liste sehen wenn du auf "Siehe Liste Von Gaste" druckst'
        self.btn4.menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', text))
        self.btn4.menu.add_command(label='Exit', command=self.__window.destroy)
        self.btn4.pack()

        self.text = Text(self.top)
        self.text.pack(fill=BOTH)
        self.top.pack()

    def error_spaces(self, l):
        for text in l:
            if text.get() == '':
                messagebox.showerror('Error', 'Sie haben nicht den ganzen Namen geschrieben,'
                                              '\nBitte fühle alle Felder aus!!', parent=self.newframe)
                return False
        return True

    def save_and_delete(self, funct, l):
        for text_entry in l:
            text_entry.delete(0, 'end')

        messagebox.showinfo('ALLES GUT', 'die eingegebenen Daten wurden verarbeitet', parent=self.newframe)

    def add_gast(self):
        self.newwindow = Toplevel(self.__window, bg='light goldenrod')
        self.newwindow.title('ADD ODATA')
        self.newframe = Frame(self.newwindow, bg='light goldenrod')
        self.newframe.pack(side=LEFT, fill=Y, expand=1)

        Label(self.newframe, text='schreibe hier den Namen des neuen Gastes', bg='light goldenrod').grid(column=1, row=0)

        self.gast_vorname_txt = Entry(self.newframe, width=50)
        self.gast_nachname_txt = Entry(self.newframe, width=50)


        Label(self.newframe, text='Vorname:', bg='light goldenrod').grid(column=0, row=1)
        self.gast_vorname_txt.grid(column=1, row=1)
        Label(self.newframe, text='Nachname:', bg='light goldenrod').grid(column=0, row=2)
        self.gast_nachname_txt.grid(column=1, row=2)

        # wir stellen alle Werte der input Felder in einer Liste um die Liste zu durchqueren und zu sehen wenn die
        # Felder nicht ausgefullt wurden
        l = [self.gast_nachname_txt, self.gast_vorname_txt]

        gast = Gast(self.gast_vorname_txt.get(), self.gast_nachname_txt.get())

        btn1 = Button(self.newframe, text='save changes', command=lambda:
        self.save_and_delete(self.__controller.add_gast
        (Gast(self.gast_vorname_txt.get(), self.gast_nachname_txt.get())), l)
        if self.error_spaces(l) else False)
        btn1.grid(column=1, row=3)
        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=4)


    def akt_nachname(self):

        self.newwindow = Toplevel(self.__window, bg='light goldenrod')
        self.newwindow.title('AKTUALISIERE')
        self.newframe = Frame(self.newwindow, bg='light goldenrod')
        self.newframe.pack()

        Label(self.newframe, text='schreibe hier den aktuellen Namen des Gastes', bg='light goldenrod').grid(column=1, row=0)
        self.gast_vorname_txt = Entry(self.newframe, width=50)
        self.gast_nachname_txt = Entry(self.newframe, width=50)

        l = [self.gast_nachname_txt.get(), self.gast_vorname_txt.get]

        Label(self.newframe, text='Vorname:', bg='light goldenrod').grid(column=0, row=1)
        self.gast_vorname_txt.grid(column=1, row=1)
        Label(self.newframe, text='Nachname:', bg='light goldenrod').grid(column=0, row=2)
        self.gast_nachname_txt.grid(column=1, row=2)

        Label(self.newframe, text='neuer Nachname des Gastes', bg='light goldenrod').grid(column=0, row=3)

        self.gast_newname_txt = Entry(self.newframe, width=50)
        self.gast_newname_txt.grid(column=1, row=3)

        l = [self.gast_nachname_txt, self.gast_vorname_txt, self.gast_newname_txt]

        btn1 = Button(self.newframe, text='update name', command=lambda:
        self.save_and_delete(self.__controller.akt_nachname(Gast(self.gast_vorname_txt.get(),
        self.gast_nachname_txt.get()), Gast(self.gast_vorname_txt.get(), self.gast_newname_txt.get())), l)
        if self.error_spaces(l) else False)
        btn1.grid(column=1, row=4)

        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=5)

    def losche_gast(self):

        self.newwindow = Toplevel(bg='light goldenrod')
        self.newwindow.title('LOSCHE ODATA')
        self.newframe = Frame(self.newwindow, bg='light goldenrod')
        self.newframe.pack()

        Label(self.newframe, text='schreibe hier den Vornamen und danach den Nachnamen des Gastes den du loschen '
                                  'willst', bg='light goldenrod').grid(column=1, row=0)

        self.gast_vorname_txt = Entry(self.newframe, width=50)
        # gast_vorname_txt.insert(0, "Vorname hier")

        self.gast_nachname_txt = Entry(self.newframe, width=50)
        # gast_nachname_txt.insert(0, "Nachname hier")

        Label(self.newframe, text='Vorname:', bg='light goldenrod').grid(column=0, row=1)
        self.gast_vorname_txt.grid(column=1, row=1)
        Label(self.newframe, text='Nachname:', bg='light goldenrod').grid(column=0, row=2)
        self.gast_nachname_txt.grid(column=1, row=2)

        l = [self.gast_nachname_txt, self.gast_vorname_txt]

        gast = Gast(self.gast_vorname_txt.get(), self.gast_nachname_txt.get())
        btn1 = Button(self.newframe, text='remove',
                      command=lambda: self.save_and_delete(self.__controller.losche_gast(Gast(self.gast_vorname_txt.get(), self.gast_nachname_txt.get())), l)
                      if self.error_spaces(l) else False)
        btn1.grid(column=1, row=3)
        btn = Button(self.newframe, text='zuruck', command=self.newwindow.destroy)
        btn.grid(column=1, row=4)

    def show_list(self):
        self.newwindow = Toplevel(bg='light goldenrod')
        self.newwindow.title('SHOW ODATA')
        self.newframe = Frame(self.newwindow, bg='light goldenrod')
        self.newframe.pack()
        self.newwindow.geometry('500x500')

        list = self.__controller.show_list_gaste()
        numar = 1
        for el in range(len(list)):
            Label(self.newframe, text=str(numar) + '. ' + 'Vorname:' + str(list[el].vorname) +
                                      ', Nachname:' + str(list[el].nachname), bg='light goldenrod').pack()
            numar += 1

        btn = Button(self.newframe, text='Ok', command=self.newwindow.destroy)
        btn.pack()
