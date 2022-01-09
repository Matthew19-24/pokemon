import tkinter as tk

username = None


# Function returns names entered
def get_name():
    window = tk.Tk()
    window.title("Name")
    window.geometry("200x100")
    name = tk.StringVar()

    def btn_get_name():
        window.destroy()

    tk.Label(text="Enter name").pack()
    tk.Entry(window, textvariable=name).pack()
    tk.Button(window, text="Ok", command=btn_get_name).pack()

    window.mainloop()
    return name.get()


# Function prints an ID card for Pokémon chosen
def id_card(poke):
    window = tk.Tk()
    window.title(poke.name)

    frame1 = tk.Frame(master=window, width=100, height=100)
    frame1.pack(side=tk.LEFT)

    frame2 = tk.Frame(master=window, width=100, height=100)
    frame2.pack(side=tk.RIGHT)

    img = tk.PhotoImage(file=poke.image)
    tk.Label(
        frame1,
        image=img
    ).pack()

    stats = tk.Label(master=frame2, text="Type: " + poke.type +
                                         "\nNature: " + poke.nature +
                                         "\nLevel: " + str(poke.lvl) +
                                         "\nHP: " + str(poke.hp_stat) +
                                         "\nAttack: " + str(poke.atk_stat) +
                                         "\nDefense: " + str(poke.def_stat) +
                                         "\nSpeed: " + str(poke.spd_stat) +
                                         "\nSpecial Attack: " + str(poke.sp_atk_stat) +
                                         "\nSpecial Defense: " + str(poke.sp_def_stat)
                     )
    stats.pack()

    window.mainloop()
