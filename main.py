import os
from core import install, browse_func, get_versions, Attributes

if os.path.exists("inst000-config.yml"):
    pass
else:
    from tkinter import Tk, Entry, Button, ttk

    Attributes.app = Tk()
    Attributes.app.title("Select your Path and Version")
    Attributes.app.geometry("500x75")
    Attributes.inst = Button(Attributes.app, text="Install", command=install)
    Attributes.entry = Entry(Attributes.app, width=57)
    Attributes.entry.insert(0, "C:/Program Files/EazyGames")  # os.getcwd().replace("\\", "/")
    Attributes.browse = Button(Attributes.app, text="Browse", command=browse_func)
    Attributes.combobox = ttk.Combobox(Attributes.app, width=54, values=get_versions())
    Attributes.combobox.current(0)

    Attributes.entry.place(relx=0.02, rely=0.3, anchor="w")
    Attributes.combobox.place(relx=0.02, rely=0.7, anchor="w")
    Attributes.inst.place(relx=0.98, rely=0.5, anchor="e")
    Attributes.browse.place(relx=0.87, rely=0.5, anchor="e")

    Attributes.app.mainloop()
