from tkinter import *


def summa ():
    a = EntryA.get ()
    a = float(a)

    b = EntryB.get ()
    b = float(b)

    result = str ((0.5*1-(1**3 * (0.5**3 - (a * 0.1) / b))**(1/3)) * 1000)
    EntryC.delete (0, END)
    EntryC.insert (0, result)

root=Tk ()

root.title ('Прогнозирование толщины стенки микросфер')
root.geometry ("300x200")

Label (root, text= 'Введите плотность раствора').pack ()
EntryA=Entry(root,width=10, font='Arial 16')
EntryA.pack()

Label (root, text= 'Введите плотность растворенного ве-ва').pack ()
EntryB=Entry(root,width=10, font='Arial 16')
EntryB.pack()

Label(root, text= 'Для вычисления  нажмите кнопку').pack ()
but = Button(root, text= 'Вычислить', command=summa)
but.pack()

EntryC=Entry(root,width=10, font= 'Arial 16')
EntryC.pack()

root.mainloop()
