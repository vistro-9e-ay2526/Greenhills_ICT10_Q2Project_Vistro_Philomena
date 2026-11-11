#Element Finder
from pyscript import display, document

def search_element(e):
    document.getElementById('output').innerHTML = ''

    elements = {
        'h': {'Element Symbol':'H', 'Element Name': 'Hydrogen', 'Atomic Number': 1, 'Atomic Mass': 1.008},
        'he': {'Element Symbol':'He', 'Element Name': 'Helium', 'Atomic Number': 2, 'Atomic Mass': 4.0026},
        'c': {'Element Symbol':'C', 'Element Name': 'Carbon', 'Atomic Number': 6, 'Atomic Mass': 12.01},
        'n': {'Element Symbol':'N','Element Name': 'Nitrogen', 'Atomic Number': 7, 'Atomic Mass': 14.01},
        'o': {'Element Symbol':'O', 'Element Name': 'Oxygen', 'Atomic Number': 8, 'Atomic Mass': 16.00},
        'f': {'Element Symbol':'F', 'Element Name': 'Fluorine', 'Atomic Number': 9, 'Atomic Mass': 18.998},
        'ne': {'Element Symbol':'Ne', 'Element Name': 'Neon', 'Atomic Number': 10, 'Atomic Mass': 20.180},
        'p': {'Element Symbol':'P', 'Element Name': 'Phosphorus', 'Atomic Number': 15, 'Atomic Mass': 30.97},
        's': {'Element Symbol':'S', 'Element Name': 'Sulfur', 'Atomic Number': 16, 'Atomic Mass': 32.06},
        'cl': {'Element Symbol':'Cl', 'Element Name': 'Chlorine', 'Atomic Number': 17, 'Atomic Mass': 35.45},
        'ar': {'Element Symbol':'Ar', 'Element Name': 'Argon', 'Atomic Number': 18, 'Atomic Mass': 39.948},
        'se': {'Element Symbol':'Se', 'Element Name': 'Selenium', 'Atomic Number': 34, 'Atomic Mass': 78.971},
        'br': {'Element Symbol':'Br', 'Element Name': 'Bromine', 'Atomic Number': 35, 'Atomic Mass': 79.904},
        'kr': {'Element Symbol':'Kr', 'Element Name': 'Krypton', 'Atomic Number': 36, 'Atomic Mass': 83.798},
        'i': {'Element Symbol':'I', 'Element Name': 'Iodine', 'Atomic Number': 53, 'Atomic Mass': 126.90},
        'xe': {'Element Symbol':'Xe', 'Element Name': 'Xenon', 'Atomic Number': 54, 'Atomic Mass': 131.29},
        'rn': {'Element Symbol':'Rn', 'Element Name': 'Radon', 'Atomic Number': 86, 'Atomic Mass': 222},
    }

    symbol = document.getElementById('input').value.lower()

    info = elements.get(symbol, {'Element Symbol': symbol.title(), 'Element Name': 'Unlisted', 'Atomic Number': '--', 'Atomic Mass': '--'})

    display(info, target='output')

    output = (
             f"Element Symbol: {symbol.title()}<br>"
            f"Element Name: {info['Element Name']}<br>"
            f"Atomic Number: {info['Atomic Number']}<br>"
            f"Atomic Mass: {info['Atomic Mass']}"
        )
    
    document.getElementById('output').innerHTML = output