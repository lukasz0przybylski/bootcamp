import tkinter

root = tkinter.Tk()
def suma():
    print("nacisnieto przycisk")
    a = a_entry.get()



a_label = tkinter.Label(master=root, text="argument a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()


b_label = tkinter.Label(master=root, text="argument b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()


button = tkinter.Button(master=root, text="argumet a")

root.mainloop()