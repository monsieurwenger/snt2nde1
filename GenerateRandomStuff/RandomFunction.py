#Generates random values for a function

from random import randint, sample 
from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from datetime import datetime
import os
import subprocess

def latex_compile(tex_file, output_filename=None, output_folder=None):
    command=["rubber -d"]
    if output_folder is not None:
        command+=[f"--into {output_folder}"]
    if output_filename is not None:
        command+=[f"--jobname {output_filename}"]
    command+=[tex_file]

    print("Command to run", " ".join(command))
    process=subprocess.Popen(" ".join(command), shell=True)
    stdout, stderr = process.communicate()
    

#OK j'ai besoin :
#3 entiers x où je vais demander l'image de x
#1 entier y qui n'a pas d'antécédent
#1

def Randomvalues(liste_antecedents, valeur_min, valeur_max):
    return [randint(valeur_min,valeur_max) for _ in liste_antecedents]


def gen_random_xy(valmin=-7, valmax=7, nb_points_interm=5, maximage=7, minimage=-2, buffer=1, show=True):
    nbgen=0
    while True:
        tbase=[valmin,valmax]
        Autresvalues = sample(list(range(valmin+1,valmax)),nb_points_interm)
        tbase=sorted(tbase+Autresvalues)
        nbgen+=1
        values=Randomvalues(tbase,minimage+buffer, maximage-buffer)
        x = np.array(tbase)
        y= np.array(values)
        poly = lagrange(x,y)
       # print(Polynomial(poly.coef[::-1]).coef)
        delta = 0
        epsilon = 0.01
        dt = 0.1
        x_new = np.arange(valmin-delta, valmax+delta + epsilon, dt)
        y_new=Polynomial(poly.coef[::-1])(x_new)
        #print(values, max(abs(y_new)))
        if max(y_new)<=maximage and min(y_new)>=minimage:
            break
    if show==True:
        plt.scatter(x, y, label='data')
        plt.plot(x_new, y_new, label='Polynomial')
        plt.legend()
        plt.show()
    return {"x":x_new, "y":y_new,"x_key":tbase, "y_key":values, "nb_tries":nbgen}

def dict_to_graph(d):
    Textcoords=[f"({d['x'][k]:.5f},{d['y'][k]:.6f})" for k in range(len(d["x"]))]
    return("\n".join(Textcoords))


def dict_to_xlist(d):
    text=" & ".join([f"${str(_)}$" for _ in d["x_key"]])
    return text






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

def random_truefalse(nb_select=4):
    listquestions=[]
    listquestions+=[("Un nombre peut avoir plusieurs images par une fonction", "Un nombre a au maximum une image par une fonction")]
    listquestions+=[("Un nombre peut avoir plusieurs antécédents par une fonction", "Un nombre a au maximum un antécédent par une fonction")]
    listquestions+=[("L'image d'un nombre $x$ par la fonction $g$ est $g(x)$","L'antécédent d'un nombre $x$ par la fonction $g$ est $g(x)$")]
    a,b=sample(list(range(0,10)),2)
    listquestions+=[(f"Si l'image de ${a}$ par la fonction $h$ est ${b}$, alors ${b}$ est un antécédent de ${a}$ par la fonction $h$",
                    f"Si l'image de ${a}$ par la fonction $h$ est ${b}$, alors ${a}$ est un antécédent de ${b}$ par la fonction $h$")]
    a,b=sample(list(range(0,10)),2)
    listquestions+=[(f"Si l'image de ${a}$ par la fonction $h$ est ${b}$, alors $h({b})={a}$",
                    f"Si l'image de ${a}$ par la fonction $h$ est ${b}$,  alors $h({a})={b}$")]
    #Choisir nb_select questions parmi la liste
    if nb_select is not None:
        preselection=sample(listquestions,nb_select)
        selection=[q[randint(0,1)] for q in preselection]
    if nb_select is None:
        preselection = listquestions[:]
        selection = []
        for k in preselection:
            selection+=[k[0],k[1]]
    return r"\item " + "\n \\item ".join(selection)

texte_individuel=open("Individual_ToRandomize.tex").read()

nb_a_produire=36
bodies=[]


"""for i in range(1):
    d=gen_random_xy(show=False)
    print(dict_to_coords(d))
    print(dict_to_xlist(d))"""


for k in range(nb_a_produire):
    dico_random=gen_random_xy(show=False)
    print(f"Generated rand values. {dico_random['nb_tries']=}")
    a_inserer=texte_individuel
    a_inserer=a_inserer.replace("{w_coords}",dict_to_graph(dico_random))
    a_inserer=a_inserer.replace("{w_xcoords}",dict_to_xlist(dico_random))
    a_inserer=a_inserer.replace("{w_questions}",random_truefalse(nb_select=4 if  nb_a_produire!= 1 else None))
    print(len(a_inserer), len(texte_individuel))
    bodies+=[a_inserer]


texte_template=open("TemplateAround.tex").read()

texte_final=texte_template.replace("{w_body}", "\n \\newpage \n".join(bodies))

nom_fichier_output = f"Output_{nb_a_produire}_{datetime.now().isoformat()}.tex"


doss_a_creer = nom_fichier_output.split(".")[0]
os.mkdir(doss_a_creer)

nom_fichier_output = doss_a_creer+"/"+"Output_genere.tex"
f = open(nom_fichier_output, "w+")
f.write(texte_final)
f.close()


latex_compile(nom_fichier_output, output_folder=doss_a_creer)