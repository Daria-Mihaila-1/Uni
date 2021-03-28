from UI.GUIGaste import *
from UI.GUIZimmer import *
from UI.GUIReservierungen import *
from tkinter import messagebox

class GUIG:
    def __init__(self, root_window, controller):
        self.__controller = controller
        self.__window = root_window

    def draw_window(self, title, dim):
        self.__window.title(title)
        self.__window.geometry(dim)

    def create_gastemenu(self):
        self.second_window = Toplevel(self.__window)
        self.second_window.title('Gaste Menu')
        self.second = Second(self.second_window, self.__controller)

    def create_zimmenu(self):
            self.third_window = Toplevel(self.__window)
            self.third_window.title('Zimmer Menu')
            self.third = Third(self.third_window, self.__controller)

    def create_resmenu(self):
            self.fourth_window = Toplevel(self.__window)
            self.fourth_window.title('Zimmer Menu')
            self.fourth = Fourth(self.fourth_window, self.__controller)

    def exit_app(self):
        antwort_exit = messagebox.askquestion('EXIT APP', 'Bist du sicher, dass du mich schliessen willst?')
        if antwort_exit == 'yes':
            self.__window.destroy()
        else:
            messagebox.showinfo('Return', 'Du wirst jetzt wieder zum Homescreen gefuhrt')

    def create_mainmenu(self): #, lst_zim, lst_res):

        self.draw_window("Main Menu", "500x500")

        my_menu = Menu(self.__window)


        my_menu.add_command(label="Menu Gaste", command=self.create_gastemenu)
        my_menu.add_command(label='Menu Zimmer', command=self.create_zimmenu)
        my_menu.add_command(label='Menu Reservierungen', command=self.create_resmenu)

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="File Menu", menu=file_menu)

        file_menu.add_command(label='Exit', command=self.exit_app)
        file_menu.add_separator()

        text = '      Wilkommen zu meiner Hotelapp!\n\nHier hast du drei Menus:\n\n' \
            '-Menu Gaste:\n mit dem du meine Liste von Gasten bearbeiten kannst \n\n' \
            '-Menu Zimmer:\nmit dem du meine Liste von Zimmer bearbeiten kannst \n\n' \
            '-Menu Reserierungen:\nwo du dir auch eine Reservierung machen und noch andere Sachen sehen kannst' \
                '\n\nDie File Menus enthalten einen Help- und einen Exitknopf'

        file_menu.add_command(label='Help', command= lambda: messagebox.showinfo('HELP ME!', text)),  # command=ceva
        self.__window.config(menu=my_menu)






