import tkinter as tk
import request
from tkinter import ttk

# Dictionnaire des facteurs de conversion entre devises
conversion_factors = {
    "Euros": {
        "Dollars": request.exchange_rates_euro['USD'],  
        "Livres": request.exchange_rates_euro['GBP'],   
        "Yen": request.exchange_rates_euro['JPY'],      
        "Yuan": request.exchange_rates_euro['CNY']      
    },
    "Dollars": {
        "Euros": request.exchange_rates_dollar['EUR'],  
        "Livres": request.exchange_rates_dollar['GBP'],  
        "Yen": request.exchange_rates_dollar['JPY'],     
        "Yuan": request.exchange_rates_dollar['CNY']     
    },
    "Livres": {
        "Euros": request.exchange_rates_livres['EUR'],  
        "Dollars": request.exchange_rates_livres['USD'], 
        "Yen": request.exchange_rates_livres['JPY'],    
        "Yuan": request.exchange_rates_livres['CNY']     
    },
    "Yen": {
        "Euros": request.exchange_rates_yen['EUR'],    
        "Dollars": request.exchange_rates_yen['USD'],  
        "Livres": request.exchange_rates_yen['GBP'],   
        "Yuan": request.exchange_rates_yen['CNY']      
    },
    "Yuan": {
        "Euros": request.exchange_rates_yuan['EUR'],   
        "Dollars": request.exchange_rates_yuan['USD'], 
        "Livres": request.exchange_rates_yuan['GBP'],  
        "Yen": request.exchange_rates_yuan['JPY']      
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
