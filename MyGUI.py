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


def starter_pick():
    window = tk.Tk()
    window.title("Starter Pokémon")
    window.geometry("480x280")

    def close():
        window.destroy()

    starter_num = tk.IntVar()

    frame1 = tk.Frame()
    img1 = tk.PhotoImage(file="poke_pic/bulbasaur.png")
    checkbox1 = tk.Radiobutton(master=frame1, text="Bulbasaur", variable=starter_num, value=1)
    tk.Label(frame1, image=img1).pack()
    checkbox1.pack()
    frame1.pack(side=tk.LEFT)

    frame2 = tk.Frame()
    img2 = tk.PhotoImage(file="poke_pic/charmander.png")
    checkbox2 = tk.Radiobutton(master=frame2, text="Charmander", variable=starter_num, value=2)
    tk.Label(frame2, image=img2).pack()
    checkbox2.pack()
    frame2.pack(side=tk.LEFT)

    frame3 = tk.Frame()
    img3 = tk.PhotoImage(file="poke_pic/squirtle.png")
    checkbox3 = tk.Radiobutton(master=frame3, text="Squirtle", variable=starter_num, value=3)
    tk.Label(frame3, image=img3).pack()
    checkbox3.pack()
    frame3.pack(side=tk.LEFT)

    okay = tk.Button(frame2, text="Okay", command=close)
    okay.pack(side=tk.BOTTOM)

    window.mainloop()
    return starter_num.get()
