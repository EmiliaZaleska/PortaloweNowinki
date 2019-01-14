import tkinter as tk
import sys
# import czytanie_plotek
# import czytanie_plotek2
# Test lists/dictionaries below, to be replaced


def test_lista():
    nowe_slowa = ["Nazwisko1", "Nazwisko2", "Nazwisko3", "Nazwisko4", "Nazwisko5"]
    print(nowe_slowa)


def test_lista2():
    nowe_slowa_portale = ["Nazwisko10", "Nazwisko20", "Nazwisko30"]
    print(nowe_slowa_portale)


def test_slownik():
    wystapienia = {"Portal1": "20.01.2018", "Portal2": "21.01.2018"}
    print(wystapienia)

def test_z_argumentem(str):
    print(str)

def test_przekazania_zmiennej(arg):
    if arg == "Nazwisko1":
        print("Portal1 - 15.01.2019")
    elif arg == "Nazwisko2":
        print("Portal3 - 20.01.2019")
    else:
        print("Nie znaleziono")

# Creating main window
main_window = tk.Tk()
main_window.title("Portalowe Nowinki")
topFrame = tk.Frame(main_window)
topFrame.grid()
bottomFrame = tk.Frame(main_window)
bottomFrame.grid()


# Printing console output in UI
def redirector(inputStr):
    textbox.insert(tk.INSERT, inputStr)


sys.stdout.write = redirector

# Top frame - labels and buttons
label_1 = tk.Label(topFrame, text="Informacje o nowościach")
label_1.grid(row=0, columnspan=2)

button_1 = tk.Button(topFrame, text="Nowe słowa", bg="black", fg="red", command=lambda: test_z_argumentem("Testowo"))
button_1.grid(row=1, columnspan=2)

button_2 = tk.Button(topFrame, text="Słowa na innych portalach", bg="black", fg="red", command=test_lista2)
button_2.grid(row=2, columnspan=2)

label_2 = tk.Label(topFrame, text="\nSzukaj wystąpień")
label_2.grid(row=3, columnspan=2)

nazwisko = tk.StringVar()
entry_1 = tk.Entry(topFrame, textvariable=nazwisko)
entry_1.grid(row=4, column=0)

button_3 = tk.Button(topFrame, text="Szukaj", bg="black", fg="red", command=lambda: test_przekazania_zmiennej(nazwisko.get()))
button_3.grid(row=4, column=1)

# Bottom frame - label and textbox
label_3 = tk.Label(bottomFrame, text="\nRezultaty:")
label_3.grid(row=5, columnspan=2)

textbox = tk.Text(bottomFrame)
textbox.grid(row=6)

main_window.mainloop()

