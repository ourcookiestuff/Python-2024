import tkinter as tk
import random


class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jednoręki Bandyta")
        # self.root.geometry("450x250")

        # Obrazki wykorzystywane w grze
        self.symbole = [tk.PhotoImage(file="arbuz.png"),
                        tk.PhotoImage(file="cytryna.png"),
                        tk.PhotoImage(file="koniczyna.png"),
                        tk.PhotoImage(file="sliwka.png"),
                        tk.PhotoImage(file="truskawka.png")]

        # Elementy interfejsu
        self.canvas = tk.Canvas(root, width=460, height=150, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.labels = [tk.Label(root, image="") for _ in range(3)]
        for i, label in enumerate(self.labels):
            label.grid(row=0, column=i, padx=10, pady=10)

        self.spin_button = tk.Button(root, text="Zakręć", command=self.spin)
        self.spin_button.grid(row=1, column=0, columnspan=3, pady=10)

        self.result_label = tk.Label(root, text="Powodzenia!", font=("Arial", 25))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10)

    def spin(self):
        # Wybieranie trzech symboli do każdej etykiety
        chosen_symbols = [random.choice(self.symbole) for _ in range(3)]
        for label, symbol in zip(self.labels, chosen_symbols):
            label.config(image=symbol)
            label.image = symbol

        # Sprawdzenie warunku wygranej
        if chosen_symbols[0] == chosen_symbols[1] == chosen_symbols[2]:
            self.result_label.config(text="Gratulacje! Wygrałeś!!!")
        else:
            self.result_label.config(text="Spróbuj ponownie")


if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
