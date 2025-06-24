# This is the look up table for calculating the orbital energies based
# on the atomic number and effective nuclear charges

import json
import matplotlib.pyplot as plt
import numpy as np

element_symbols = [
    'X',  # Ghost
    'H' , 'He', 'Li', 'Be', 'B' , 'C' , 'N' , 'O' , 'F' , 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P' , 'S' , 'Cl', 'Ar', 'K' , 'Ca',
    'Sc', 'Ti', 'V' , 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y' , 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'Te', 'I' , 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W' , 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U' , 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
]

au2eV = 27.21139

def _get_atomic_number(symbol):
    """
    Get the atomic number of an element given its symbol.
    """
    try:
        return element_symbols.index(symbol)
    except ValueError:
        raise ValueError(f"Element symbol '{symbol}' not found in the list.")
    
def get_l(l):
    '''
    l = s, p, d, f, g
    '''
    return {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g':4,}.get(l, "l value is not valid")

def get_n_l(orb):
    assert len(str(orb)) >= 2
    n = int(orb[0])
    l = get_l(str(orb[1]))
    return n, l

def giveorbitalenergy(ele, orb):
    with open('./orbitalenergy.json', 'r') as f: #Assign this path properly, once we are finalized with the structure of code.
        data = json.load(f)
    try:
        orbenegele = data[ele]
        del data
    except KeyError:
        raise KeyError("Element symbol not found")
    n, l = get_n_l(orb)
    cbenergy = orbenegele[str(l)][n-l-1]
    cbenergy *= au2eV
    #print(f"{ele}: {orb} orbital energy is {cbenergy} eV")
    return cbenergy

if __name__ == '__main__':
    # Example to show how to obtain the orbital energies out of the look-up table obtained
    # from the CASSCF/CASPT2 model-Fock matrix eigenvalues calculated at ANO-RCC-VTZP basis set.
    ele, orb = 'C 1s'.split()
    be = giveorbitalenergy(ele, orb)
    print("Core-binding energy for C 1s:", be, 'eV')
    
    ele, orb = 'Al 2p1/2'.split()
    be = giveorbitalenergy(ele, orb)
    print("Core-binding energy for Al 2p:", be, 'eV')
