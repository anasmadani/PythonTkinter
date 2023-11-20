import tkinter
import math
from tkinter import *
import numpy as np
from tkinter import filedialog
from tkinter import messagebox

"""
 Équations de la cinématique (accélération constante)
 d = vi*t + 1/2 * a * t^2
 vf = vi + a*t
 vf^2 = vi^2 + 2 * a * d
 d = (vi + vf)/2 * t

"""

racine = Tk()
racine.title('Resolution des equations de cinematique du point')
var = IntVar()

resultats_string = StringVar()
resultats_string.set("Résultats")

for i in range(9):  # on nbr colonnes = 6 , et nbr lignes = 9
    if i < 6:
        Grid.columnconfigure(racine, i, weight=1)
        Grid.rowconfigure(racine, i, weight=1)
    else:
        Grid.rowconfigure(racine, i, weight=1)


# def reinitialiser_interface():
#     # Réinitialisez les valeurs
#     d.delete(0, END)
#     t.delete(0, END)
#     vi.delete(0, END)
#     vf.delete(0, END)
#     a.delete(0, END)
#
#     # Réinitialisez la taille des boutons
#     bouton_effacer.config(width=15)
#     d_bouton.config(width=15)
#     t_bouton.config(width=15)
#     vi_bouton.config(width=15)
#     vf_bouton.config(width=15)
#     a_bouton.config(width=15)
#
#     # Supprimez le graphique
#     graph_canvas.delete("all")

def dark_mode():
    if var.get() == 1:
        # Dark mode
        racine.config(bg='black')
        label1.config(bg='black', fg='white')
        label2.config(bg='black', fg='white')

        d_label.config(bg='black', fg='white')
        vi_label.config(bg='black', fg='white')
        vf_label.config(bg='black', fg='white')
        a_label.config(bg='black', fg='white')
        t_label.config(bg='black', fg='white')
        graph_canvas.config(bg='black', highlightbackground='white', highlightcolor='white', highlightthickness=1)

        vi.config(bg='black', fg='white')
        vf.config(bg='black', fg='white')
        t.config(bg='black', fg='white')
        a.config(bg='black', fg='white')
        d.config(bg='black', fg='white') 

        d_bouton.config(bg='black', fg='white')
        a_bouton.config(bg='black', fg='white')
        vi_bouton.config(bg='black', fg='white')
        vf_bouton.config(bg='black', fg='white')
        t_bouton.config(bg='black', fg='white')

        bouton_effacer.config(bg='black', fg='white')
        export_button.config(bg='black', fg='white')
        plot_button.config(bg='black', fg='white')

        mode_sombre.config(bg='black', fg='white')

        
    else:
        # Light mode
        # racine.config(bg='white')
        # label.config(bg='white', fg='black')
        # canvas.config(bg='white', highlightbackground='black', highlightcolor='black', highlightthickness=1)
        # entry_velocity.config(bg='white', fg='black')
        # entry_time.config(bg='white', fg='black')
        # entry_acceleration.config(bg='white', fg='black')
        # button_calculate.config(bg='lightgrey', fg='black')
        racine.config(bg='lightgray')
        label1.config(bg='lightgray', fg='black')
        label2.config(bg='lightgray', fg='black')

        d_label.config(bg='lightgray', fg='black')
        vi_label.config(bg='lightgray', fg='black')
        vf_label.config(bg='lightgray', fg='black')
        a_label.config(bg='lightgray', fg='black')
        t_label.config(bg='lightgray', fg='black')

        graph_canvas.config(bg='lightgray', highlightbackground='black', highlightcolor='white', highlightthickness=1)

        vi.config(bg='lightgray', fg='black')
        vf.config(bg='lightgray', fg='black')
        t.config(bg='lightgray', fg='black')
        a.config(bg='lightgray', fg='black')
        d.config(bg='lightgray', fg='black')

        d_bouton.config(bg='lightgray', fg='black')
        a_bouton.config(bg='lightgray', fg='black')
        vi_bouton.config(bg='lightgray', fg='black')
        vf_bouton.config(bg='lightgray', fg='black')
        t_bouton.config(bg='lightgray', fg='black')

        bouton_effacer.config(bg='lightgray', fg='black')
        export_button.config(bg='lightgray', fg='black')
        plot_button.config(bg='lightgray', fg='black')
        mode_sombre.config(bg='lightgray', fg='black')

def effacer_valeurs():  # fonction pour vider les champs deja remplis
    # reinitialiser_interface()
    global graph_canvas
    d.delete(0, END)
    t.delete(0, END)
    vi.delete(0, END)
    vf.delete(0, END)
    a.delete(0, END)
    for item in graph_canvas.find_all():  #effacer le graphe
        graph_canvas.delete(item)



#fonction pour dessiner un graphique
def plot_trajectory():
    global graph_canvas
    # effacer_valeurs()

    var_connues = obtenir_var_connues()
    if 't' in var_connues and 'vi' in var_connues and 'a' in var_connues:
        t_values = np.linspace(0, var_connues['t'], 100)
        vi = var_connues['vi']
        a = var_connues['a']
        d_values = vi * t_values + 0.5 * a * t_values**2

        # Création du graphique avec tkinter
        graph_canvas = Canvas(racine, width=400, height=300)
        graph_canvas.grid(row=10, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')

        # Dessiner la trajectoire sur le graphique
        for i in range(len(t_values) - 1):
            x1, y1 = (t_values[i] / var_connues['t']) * 400, 300 - (d_values[i] / max(d_values)) * 300
            x2, y2 = (t_values[i + 1] / var_connues['t']) * 400, 300 - (d_values[i + 1] / max(d_values)) * 300
            graph_canvas.create_line(x1, y1, x2, y2, fill='blue')

        graph_canvas.create_text(200, 280, text='Trajectoire vs Temps', font='bold')


def obtenir_var_connues():
    var_connues = {}
    if d.get() != '':
        d1 = float(d.get())
        var_connues.update({'d': d1})
    if t.get() != '':
        t1 = float(t.get())
        var_connues.update({'t': t1})
    if vi.get() != '':
        vi1 = float(vi.get())
        var_connues.update({'vi': vi1})
    if vf.get() != '':
        vf1 = float(vf.get())
        var_connues.update({'vf': vf1})
    if a.get() != '':
        a1 = float(a.get())
        var_connues.update({'a': a1})
    return var_connues


def calc_d():  # fonction pour calculer la distance d
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'd' in var_connues:
        d2 = var_connues['d']
        work = 'd = d...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        d2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 't' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'a' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        d2 = vi2 * t2 + (0.5 * a2 * t2 ** 2)
        work = 'd = vi*t + 1/2*a*t^2'
    elif formule == 2:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        d2 = (vf2 ** 2 - vi2 ** 2) / (2 * a2)
        work = 'd = (vf^2-vi^2)/2a'
    elif formule == 3:
        vf2 = var_connues['vf']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        d2 = (vi2 + vf2) * t2 / 2
        work = 'd = (vi + vf)/2 * t'
    elif formule == 4:
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        t2 = var_connues['t']
        vi2 = vf2 - a2 * t2
        d2 = (vi2 + vf2) * t2 / 2
        work = f'vi = vf - a*t\nvi = {vi2} m/s\nd = (vi + vf)/2 * t '
    resultats_string.set(f'{work}\n distance: {round(d2, 2)} m')

def txt_d():  # fonction pour calculer la distance d
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'd' in var_connues:
        d2 = var_connues['d']
        work = 'd = d...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        d2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 't' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'a' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        d2 = vi2 * t2 + (0.5 * a2 * t2 ** 2)
        work = 'd = vi*t + 1/2*a*t^2'
    elif formule == 2:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        d2 = (vf2 ** 2 - vi2 ** 2) / (2 * a2)
        work = 'd = (vf^2-vi^2)/2a'
    elif formule == 3:
        vf2 = var_connues['vf']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        d2 = (vi2 + vf2) * t2 / 2
        work = 'd = (vi + vf)/2 * t'
    elif formule == 4:
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        t2 = var_connues['t']
        vi2 = vf2 - a2 * t2
        d2 = (vi2 + vf2) * t2 / 2
        work = f'vi = vf - a*t\nvi = {vi2} m/s\nd = (vi + vf)/2 * t '
    return round(d2,2)


def calc_t():  # fonction pour calculer le temps t
    global resultats_string
    var_connues = obtenir_var_connues()
    if 't' in var_connues:
        t2 = var_connues['t']
        work = 't = t...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        t2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 'd' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 'a' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        d2 = var_connues['d']
        t_plus = (-vi2 + math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        t_minus = (-vi2 - math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        if t_plus >= 0:
            t2 = t_plus
        else:
            t2 = t_minus
        work = '1/2*a*t^2 + vi*t - d = 0\néquation quadratique : x = (-b +/- sqrt(b^2 - 4ac))/2a\n' \
            't = valeur positive de (-vi +/- sqrt(vi^2 - 2ad))/a'

    elif formule == 2:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        t2 = (vf2 - vi2) / a2
        work = 't = (vf-vi)/a'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        t2 = (2 * d2) / (vi2 - vf2)
        work = 't = 2d/(vi-vf)'
    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        t2 = (2 * d2) / (vi2 - vf2)
        work = f'vi = sqrt(vf^2 - 2*a*d)\nvi = {vi2} m/s\nt = 2d/(vi-vf) '
    resultats_string.set(f'{work}\n temps: {round(t2, 2)} s')


def txt_t():  # fonction pour calculer le temps t
    global resultats_string
    var_connues = obtenir_var_connues()
    if 't' in var_connues:
        t2 = var_connues['t']
        work = 't = t...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        t2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 'd' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 'a' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        d2 = var_connues['d']
        t_plus = (-vi2 + math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        t_minus = (-vi2 - math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        if t_plus >= 0:
            t2 = t_plus
        else:
            t2 = t_minus
        work = '1/2*a*t^2 + vi*t - d = 0\néquation quadratique : x = (-b +/- sqrt(b^2 - 4ac))/2a\n' \
            't = valeur positive de (-vi +/- sqrt(vi^2 - 2ad))/a'

    elif formule == 2:
        a2 = var_connues['a']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        t2 = (vf2 - vi2) / a2
        work = 't = (vf-vi)/a'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        t2 = (2 * d2) / (vi2 - vf2)
        work = 't = 2d/(vi-vf)'
    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        t2 = (2 * d2) / (vi2 - vf2)
        work = f'vi = sqrt(vf^2 - 2*a*d)\nvi = {vi2} m/s\nt = 2d/(vi-vf) '
    return round(t2,2)



def calc_vi():  # fonction pour calculer la vitesse initiale
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'vi' in var_connues:
        vi2 = var_connues['vi']
        work = 'vi = vi...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        vi2 = 0.0
    elif 'a' in var_connues:
        if 'd' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 't' in var_connues and 'vf' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        d2 = var_connues['d']
        a2 = var_connues['a']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        work = 'vi = (d - (1/2*a*t^2))/t'
    elif formule == 2:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        work = 'vi = sqrt(vf^2 - 2*a*d)'
    elif formule == 3:
        a2 = var_connues['a']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = vf2 - (a2 * t2)
        work = 'vi = vf - a*t'

    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = (d2 / t2) * 2 - vf2
        work = 'vi = 2*d/t - vf'
    resultats_string.set(f'{work}\n vitesse initiale: {round(vi2, 2)} m/s')


def txt_vi():  # fonction pour calculer la vitesse initiale
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'vi' in var_connues:
        vi2 = var_connues['vi']
        work = 'vi = vi...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        vi2 = 0.0
    elif 'a' in var_connues:
        if 'd' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'vf' in var_connues:
                formule = 2
        elif 't' in var_connues and 'vf' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        d2 = var_connues['d']
        a2 = var_connues['a']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        work = 'vi = (d - (1/2*a*t^2))/t'
    elif formule == 2:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        a2 = var_connues['a']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        work = 'vi = sqrt(vf^2 - 2*a*d)'
    elif formule == 3:
        a2 = var_connues['a']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = vf2 - (a2 * t2)
        work = 'vi = vf - a*t'

    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = (d2 / t2) * 2 - vf2
        work = 'vi = 2*d/t - vf'
    return round(vi2,2)


def calc_vf():  # fonction pour calculer la vitesse finale
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'vf' in var_connues:
        vf2 = var_connues['vf']
        work = 'vf = vf...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        vf2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'd' in var_connues:
                formule = 2
        elif 't' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'a' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        vf2 = vi2 + (a2 * t2)
        work = 'vf = vi + (a*t)'
    elif formule == 2:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        vf2 = math.sqrt(vi2 ** 2 + 2 * a2 * d2)
        work = 'vf = sqrt(vi^2 + 2*a*d)'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        vf2 = ((d2 / t2) * 2) - vi2
        work = 'vf = 2d/t - vi'
    elif formule == 4:
        d2 = var_connues['d']
        a2 = var_connues['a']
        t2 = var_connues['t']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        vf2 = vi2 + a2 * t2
        work = f'vi = (d - (1/2*a*t^2))/t\nvi = {vi2} m/s\nvf = vi + a*t '
    resultats_string.set(f'{work}\n vitesse finale: {round(vf2, 2)} m/s')

def txt_vf():  # fonction pour calculer la vitesse finale
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'vf' in var_connues:
        vf2 = var_connues['vf']
        work = 'vf = vf...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        vf2 = 0.0
    elif 'vi' in var_connues:
        if 'a' in var_connues:
            if 't' in var_connues:
                formule = 1
            elif 'd' in var_connues:
                formule = 2
        elif 't' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'a' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        vf2 = vi2 + (a2 * t2)
        work = 'vf = vi + (a*t)'
    elif formule == 2:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        a2 = var_connues['a']
        vf2 = math.sqrt(vi2 ** 2 + 2 * a2 * d2)
        work = 'vf = sqrt(vi^2 + 2*a*d)'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        vf2 = ((d2 / t2) * 2) - vi2
        work = 'vf = 2d/t - vi'
    elif formule == 4:
        d2 = var_connues['d']
        a2 = var_connues['a']
        t2 = var_connues['t']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        vf2 = vi2 + a2 * t2
        work = f'vi = (d - (1/2*a*t^2))/t\nvi = {vi2} m/s\nvf = vi + a*t '
    return round(vf2,2)


def calc_a():  # calculer l'acceleration
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'a' in var_connues:
        a2 = var_connues['a']
        work = 'a = a...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        a2 = 0.0
    elif 'vi' in var_connues:
        if 't' in var_connues:
            if 'vf' in var_connues:
                formule = 1
            elif 'd' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        a2 = (vi2 - vf2) / t2
        work = ('a = (vi - vf) / t')
    elif formule == 2:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        a2 = 2 * (d2 - (vi2 * t2)) / (t2 ** 2)
        work = 'a = 2*(d - (vi*t))/t^2'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        a2 = (vf2 ** 2 - vi2 ** 2) / 2 * d2
        work = 'a = (vf^2 - vi^2)/2*d'
    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = ((d2 / t2) * 2) - vf2
        a2 = (vf2 - vi2) / t2
        work = f'vi = 2d/t - vf\n vi = {vi2} m/s \n a = (vf-vi)/t '
    resultats_string.set(f'{work}\n acceleration: {round(a2, 2)} m/s^2')


def txt_a():  # calculer l'acceleration
    global resultats_string
    var_connues = obtenir_var_connues()
    if 'a' in var_connues:
        a2 = var_connues['a']
        work = 'a = a...'
        formule = 5
    elif len(var_connues) < 3:
        formule = 0
        work = "Besoin d'au moins 3 valeurs connues pour résoudre ! Problème non résolu !"
        a2 = 0.0
    elif 'vi' in var_connues:
        if 't' in var_connues:
            if 'vf' in var_connues:
                formule = 1
            elif 'd' in var_connues:
                formule = 2
        elif 'vf' in var_connues and 'd' in var_connues:
            formule = 3
    elif 'vf' in var_connues and 'd' in var_connues and 't' in var_connues:
        formule = 4
    else:
        print("Que se passe-t-il ?")
    if formule == 1:
        t2 = var_connues['t']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        a2 = (vi2 - vf2) / t2
        work = ('a = (vi - vf) / t')
    elif formule == 2:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        t2 = var_connues['t']
        a2 = 2 * (d2 - (vi2 * t2)) / (t2 ** 2)
        work = 'a = 2*(d - (vi*t))/t^2'
    elif formule == 3:
        d2 = var_connues['d']
        vi2 = var_connues['vi']
        vf2 = var_connues['vf']
        a2 = (vf2 ** 2 - vi2 ** 2) / 2 * d2
        work = 'a = (vf^2 - vi^2)/2*d'
    elif formule == 4:
        d2 = var_connues['d']
        vf2 = var_connues['vf']
        t2 = var_connues['t']
        vi2 = ((d2 / t2) * 2) - vf2
        a2 = (vf2 - vi2) / t2
        work = f'vi = 2d/t - vf\n vi = {vi2} m/s \n a = (vf-vi)/t '
    return round(a2,2)


def export_to_txt(): #exporter les donnees de la trajectoire dans un fichier txt
    var_connues = obtenir_var_connues()

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write("Variables connues :\n")
            for key, value in var_connues.items():
                file.write(f"{key}: {value}\n")

            file.write("\nRésultats:\n")
            file.write(f"Distance (d): {str(txt_d())}\n")
            file.write(f"Temps (t): {str(txt_t())}\n")
            file.write(f"Vitesse initiale (vi): {str(vi.get())}\n")
            file.write(f"Vitesse finale (vf): {str(txt_vf())}\n")
            file.write(f"Accélération (a): {str(txt_a())}\n")

        print(f"Données exportées avec succès vers {file_path}")




label1 = Label(racine, text='saisir les variables connues', font='bold')
label1.grid(row=0, columnspan=6, padx=10, pady=10,
            sticky='NESW')  # sticky pour resizing widgets quand on zoom in ou zoom out

# cette partie pour l'etiquette du deplacement (m)
d_label = Label(racine, text='d-Déplacement (mètres)')
d_label.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
d = Entry(racine, borderwidth=5)
d.grid(row=1, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')

# cette partie pour l'etiquette du temps (s)
t_label = Label(racine, text='t-Temps (seconds)')
t_label.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
t = Entry(racine, borderwidth=5)
t.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')

# pour la vitesse initiale
vi_label = Label(racine, text='vi-Vitesse initiale (m/s)')
vi_label.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
vi = Entry(racine, borderwidth=5)
vi.grid(row=3, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')

# pour la vitesse finale
vf_label = Label(racine, text='vf-Vitesse finale (m/s)')
vf_label.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
vf = Entry(racine, borderwidth=5)
vf.grid(row=4, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')

# pour l'acceleration
a_label = Label(racine, text='a-Acceleration (m/s^2)')
a_label.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
a = Entry(racine, borderwidth=5)
a.grid(row=5, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')

# cette partie indique le variable qu'on savoir sa valeur
label2 = Label(racine, text='Sélectionnez ce que vous souhaitez résoudre pour.', font='bold')
label2.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
bouton_effacer = Button(racine, text='Effacer les valeurs', command=effacer_valeurs, font='bold')
bouton_effacer.grid(row=7, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
d_bouton = Button(racine, text='d', command=calc_d, font='bold')
d_bouton.grid(row=7, column=1, columnspan=1, padx=10, pady=10, sticky='NESW')
t_bouton = Button(racine, text='t', command=calc_t, font='bold')
t_bouton.grid(row=7, column=2, columnspan=1, padx=10, pady=10, sticky='NESW')
vi_bouton = Button(racine, text='vi', command=calc_vi, font='bold')
vi_bouton.grid(row=7, column=3, columnspan=1, padx=10, pady=10, sticky='NESW')
vf_bouton = Button(racine, text='vf', command=calc_vf, font='bold')
vf_bouton.grid(row=7, column=4, columnspan=1, padx=10, pady=10, sticky='NESW')
a_bouton = Button(racine, text='a', command=calc_a, font='bold')
a_bouton.grid(row=7, column=5, columnspan=1, padx=10, pady=10, sticky='NESW')
resultats = Label(racine, textvariable=resultats_string, font='bold')
resultats.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')

graph_canvas = Canvas(racine, width=40, height=30, bg='white')
graph_canvas.grid(row=9, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
plot_button = Button(racine, text='Tracer la trajectoire (il faut donner t , vi , a)', command=plot_trajectory, font='bold')
plot_button.grid(row=10, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')

export_button = Button(racine, text='Exporter vers TXT (il faut donner au moins 3 variables connues)', command=export_to_txt, font='bold')
export_button.grid(row=9, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
messagebox.showinfo("showinfo", "Welcome to the app of Abir the pricess")
mode_sombre = Checkbutton(racine, text="Sombre/Light mode",variable=var ,onvalue=1,offvalue=0,   command=dark_mode)
mode_sombre.grid(row=11, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
scale = Scale(racine, from_=0, to=100, orient=HORIZONTAL)
scale.grid(row=12, column=0, columnspan=6, padx=10, pady=10,  sticky='NESW')
top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text = "Toplevel widget")
l2.pack()
racine.mainloop()
