#Generates random values for a function

from random import randint, sample 
from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

#OK j'ai besoin :
#3 entiers x où je vais demander l'image de x
#1 entier y qui n'a pas d'antécédent
#1

def Randomvalues(liste_antecedents, valeur_min, valeur_max):
    return [randint(valeur_min,valeur_max) for _ in liste_antecedents]




def gen_random_xy(valmin=-7, valmax=7, nb_points_interm=5, maxabs=7, buffer=2, show=True):
    nbgen=0
    tbase=[valmin,valmax]
    Autresvalues=sample(list(range(valmin+1,valmax)),nb_points_interm)
    tbase=sorted(tbase+Autresvalues)
    while True:
        nbgen+=1
        values=Randomvalues(tbase,-maxabs+buffer, maxabs-buffer)
        x = np.array(tbase)
        y= np.array(values)
        poly = lagrange(x,y)
       # print(Polynomial(poly.coef[::-1]).coef)
        x_new = np.arange(valmin-0.1, valmax+0.11, 0.1)
        y_new=Polynomial(poly.coef[::-1])(x_new)
        #print(values, max(abs(y_new)))
        if max(y_new)<=maxabs and min(y_new)>=-maxabs:
            break
    if show==True:
        plt.scatter(x, y, label='data')
        plt.plot(x_new, y_new, label='Polynomial')
        plt.legend()
        print(nbgen)
        plt.show()
    return {"x":x_new, "y":y_new,"x_key":tbase, "y_key":values, "nb_tries":nbgen}

def dict_to_graph(d):
    text=r"""\begin{tikzpicture}
    \begin{axis}[
    axis lines=middle,
    grid=major,
    xmin=-7.1,
    xmax=7.1,
    ymin=-7.1,
    ymax=7.1,
    xlabel=$x$,
    ylabel=$y$,
    xtick={-7,-6,...,7},
    ytick={-7,-6,...,7},
    scale=2.2,
    transform shape,
    ticklabel style={
                fill=white
            },
    tick style={very thick},
    legend style={
    at={(rel axis cs:0,1)},
    anchor=north west,draw=none,inner sep=0pt,fill=gray!10}
    ]
    \addplot[color=red,no mark] coordinates {
        {My_Coords}
	};
    \end{axis}
\end{tikzpicture}"""
    Textcoords=[f"({d['x'][k]:.5f},{d['y'][k]:.6f})" for k in range(len(d["x"]))]
    text=text.replace("{My_Coords}", "\n".join(Textcoords))
    return(text)


def dict_to_tableau_valeurs(d):
    text=r"""\renewcommand{\arraystretch}{2}
\begin{tabular}{|c|*{7}{P{1cm}|}}
     \hline
     x& {MesCoords} \\
     \hline
     f(x)& & & & & & & \\
     \hline
\end{tabular}
    """.replace("{MesCoords}", " & ".join([str(_) for _ in d["x_key"]]))
    return text

for i in range(1):
    d=gen_random_xy(show=False)
    print(dict_to_graph(d))
    print(dict_to_tableau_valeurs(d))



# Un nombre peut avoir plusieurs images par une fonction
# Un nombre a au maximum une image par une fonction

# Un nombre peut avoir plusieurs antécédents par une fonction
# Un nombre a au maximum un antécédent par une fonction

# L'image d'un nombre x par la fonction g est g(x)
# L'antécédent d'un nombre x par la fonction g est g(x)

# Si l'image de 5 par la fonction h est 3, alors 3 est un antécédent de 5 par la fonction h
# Si l'image de 5 par la fonction h est 3, alors 5 est un antécédent de 3 par la fonction h

# Si l'image de 7 par la fonction g est 4, alors g(4)=7
# Si l'image de 7 par la fonction g est 4, alors g(7)=4
