#=======================================================================
# fichier : exercice1.py
# but     : un exercice pour Nono
# auteurs : Christine LE BIHAN et Jean Marc VAGINAY
# date    :
#=======================================================================
from random import randint
import robot

def demarrer(no_exo):
    largeur, hauteur = robot._NB_CASES
    assert 1 <= no_exo <= 6, "NUM_EXO a une valeur incorrecte."
    # paramètres du robot (x, y, cap)
    p_robot = (0, 0, 'E')
    
    # paramètres du téseor (x, y). Mettre des valeurs hors terrain pour
    # ne pas afficher le trésor, exemple (-2,-2)
    pos = (
        (10,0),
        (0,8),
        (6, 9),
        (randint(1,largeur-1),0),
        (0, randint(1,hauteur-1)),
        (randint(1,largeur-1), randint(1,hauteur-1))
    )
    p_tresor = pos[no_exo-1]
    
    # les murs : une liste de listes (DOIT ETRE UNE MATRICE)
    murs = [[]]
    
    # le message pour la mission
    texte = "Nono doit se placer sur le trésor."
    
    robot._demarrer_prog(p_robot, p_tresor, murs, texte)

def verifier(no_exo):
    if robot.nono.get_pos() == robot.tresor.get_pos():
        txt = "Gagné !"
    else:
        txt = "Perdu, revoir le code."
    robot._afficher_message(txt)

