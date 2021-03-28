from Controller.control import *
from UI.GUI_General import *
from Repository.Hotel import *
def main():
    r = Hotel()
    c = Control(r)
    root = Tk()
    creation = GUIG(root, c)
    creation.create_mainmenu()  # , lst_zim, lst_res
    bg = PhotoImage(file=r'C:\Users\Daria\OneDrive\Desktop\pic4.png')
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(root, text="Willkommen!", font="Times 30", fg='gold4', bg='light gray').pack()

    Label(root, text="clicke auf 'File Menu' um herauszufinden wie ich funktioniere",
          font="Times 12", fg='gold4', bg='gray10').pack(side=BOTTOM, pady=10)
    root.mainloop()


main()
