import tkinter as tk
from tkinter import ttk

# Dictionnaire des facteurs de conversion entre devises
conversion_factors = {
    "Euros": {
        "Dollars": 1.13,  # 1 Euro = 1.13 Dollars
        "Livres": 0.86,    # 1 Euro = 0.86 Livres
        "Yen": 129.29,     # 1 Euro = 129.29 Yen
        "Yuan": 7.29       # 1 Euro = 7.29 Yuan
    },
    "Dollars": {
        "Euros": 0.88,     # 1 Dollar = 0.88 Euros
        "Livres": 0.77,    # 1 Dollar = 0.77 Livres
        "Yen": 115.91,     # 1 Dollar = 115.91 Yen
        "Yuan": 6.50       # 1 Dollar = 6.50 Yuan
    },
    "Livres": {
        "Euros": 1.16,     # 1 Livre = 1.16 Euros
        "Dollars": 1.30,   # 1 Livre = 1.30 Dollars
        "Yen": 149.42,     # 1 Livre = 149.42 Yen
        "Yuan": 8.36       # 1 Livre = 8.36 Yuan
    },
    "Yen": {
        "Euros": 0.0077,   # 1 Yen = 0.0077 Euros
        "Dollars": 0.0086, # 1 Yen = 0.0086 Dollars
        "Livres": 0.0067,  # 1 Yen = 0.0067 Livres
        "Yuan": 0.056      # 1 Yen = 0.056 Yuan
    },
    "Yuan": {
        "Euros": 0.14,     # 1 Yuan = 0.14 Euros
        "Dollars": 0.15,   # 1 Yuan = 0.15 Dollars
        "Livres": 0.12,    # 1 Yuan = 0.12 Livres
        "Yen": 17.78       # 1 Yuan = 17.78 Yen
    }
}

def convert_action():
    selected_value_to = combo_box_to.get()
    selected_value_what = combo_box_what.get()
    value_what = entry_what.get()
    output_value.config(state=tk.NORMAL)
    try:
        value_to = float(value_what) * float(conversion_factors[selected_value_what][selected_value_to])
    except KeyError:
        value_to = float(value_what)
    except ValueError:
        value_to = "NULL"
    if type(value_to) == float:
        output_value.replace(1.0, tk.END, value_to)
    output_value.config(state=tk.DISABLED)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Liste déroulante")
root.geometry("300x300")

# Création d'une liste de choix
options = ["Euros", "Dollars", "Livres", "Yen", "Yuan"]

# Création de la combobox
combo_box_what = ttk.Combobox(root, values=options)
combo_box_what.pack(pady = 10)
combo_box_what.bind("<<ComboboxSelected>>")

entry_what = tk.Entry(root)
entry_what.pack()

# Création de la combobox
combo_box_to = ttk.Combobox(root, values=options)
combo_box_to.pack(pady=10)
combo_box_to.bind("<<ComboboxSelected>>")

convert_button = tk.Button(root, text="Convert", command=convert_action)
convert_button.pack(pady=10)  # Placer le bouton Convert en dessous du champ d'entrée

output_value = tk.Text(root)
output_value.config(state=tk.DISABLED)
output_value.pack()

# Lancement de la boucle principale de l'interface graphique
root.mainloop()
