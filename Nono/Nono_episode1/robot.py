#=======================================================================
# fichier : robot.py
# but     : faire évoluer un robot dans un labyrinthe
# auteurs : Christine LE BIHAN et Jean Marc VAGINAY
# date    :
#=======================================================================

########################################################################
#                                                                      #
#                    NE RIEN MODIFIER DANS CE FICHIER                  #
#                                                                      #
########################################################################

######### Importations de modules ######################################
import pygame

######### Constantes ###################################################
#---- constantes générales ----
_PAUSE = 100   # pause en ms entre 2 déplacements du robot            

#---- le terrain ----
_NB_CASES    = (15,12)         # Nombres de cases en X et en Y
_TAILLE_CASE = 40              # taille d'une case en pixel
_CLR_FOND    = (255, 255, 255) # Couleur du fond
_CLR_GRILLE  = (0, 0, 0)       # couleur de la grille
_CLR_MUR     = (100, 50, 0)    # couleur des murs
_CLR_MARQUE  = (0,128,0)       # couleur des marques
# constantes définissant ce qu'il y a dans une case
_VIDE   = 0
_MUR    = 1
_MARQUE = 2

#---- la fenêtre ----
_LARGEUR = _NB_CASES[0] * _TAILLE_CASE # Largeur de la fenêtre en pixels
_HAUTEUR = _NB_CASES[1] * _TAILLE_CASE # hauteur de la fenêtre en pixels
_TEXTE   = 700
_TAILLE  = (_LARGEUR + _TEXTE, _HAUTEUR)

#---- le robot ----
_CLR_ROBOT = ((255,0,0), (0,0,0))

#---- le trésor ----
_CLR_TRESOR = (255,192,0)

######### Fonctions exportables ########################################
# fonctions_autorisées
good_fonct = {
    "mur_en_face": True,
    "sur_marque":True,
    "marque_en_face":True,
    "position":True,
}

def avancer():
    """
    Avance le robot d'une case en fonction de son cap
    """
    nono.avancer()
    _maj_fenetre()
    
def tourner_droite():
    """
    Le robot tourne de 90° à droite
    Cette fonction ne modifie que le cap du robot, le robot reste dans la même case
    """
    nono.tourner_droite()
    _maj_fenetre()
    
def tourner_gauche():
    """
    Le robot tourne de 90° à gauche
    Cette fonction ne modifie que le cap du robot, le robot reste dans la même case
    """
    nono.tourner_gauche()
    _maj_fenetre()

def mur_en_face():
    """
    Retourne True s'il y a un mur (ou le bord de la fenêtre) devant le robot
             False sinon, dans ce cas le robot peut avancer
    """
    assert good_fonct["mur_en_face"], "Fonction mur_en_face() interdite !!!"
    x, y = nono.get_pos_devant()
    return terrain.get_case(x,y) == _MUR

def marquer():
    """
    Marque la case occupée par le robot
    """
    pos = nono.get_pos()
    terrain.marquer(pos)
    _maj_fenetre()

def effacer_marque():
    """
    Efface la marque de la case occupée par le robot (si la case est marquée)
    """
    pos = nono.get_pos()
    terrain.effacer_marque(pos)
    _maj_fenetre()

def sur_marque():
    """
    retourne True si le robot est sur une marque
            False sinon
    """
    assert good_fonct["sur_marque"], "Fonction sur_marque() interdite !!!"
    x, y = nono.get_pos()
    return terrain.get_case(x,y) == _MARQUE

def marque_en_face():
    """
    Retourne True s'il y a une marque devant le robot
             False sinon
    """
    assert good_fonct["marque_en_face"], "Fonction marque_en_face() interdite !!!"
    x, y = nono.get_pos_devant()
    return terrain.get_case(x,y) == _MARQUE

def sur_tresor():
    """
    retourne True si le robot est sur le trésor
            False sinon
    """
    return nono.get_pos() == tresor.get_pos()
    
def position():
    assert good_fonct["position"], "Fonction position() interdite !!!"
    return nono.get_pos()

      
######### Classes internes (non exportables) ##########################
class _Terrain:
    def __init__(self, fenetre, murs):
        self._fenetre = fenetre
        larg, haut = _NB_CASES
        self._grille = [[_VIDE for _ in range(larg)] for _ in range(haut)]
        # on place les murs
        haut = min(haut, len(murs))
        larg = min(larg, len(murs[0]))
        for y in range(haut):
            for x in range(larg):
                if murs[y][x]:
                    self._grille[y][x] = _MUR
    
        
    def marquer(self, pos):
        x, y = pos
        self._grille[y][x] = _MARQUE
        
    def effacer_marque(self, pos):
        x, y = pos
        self._grille[y][x] = _VIDE

    def dessiner(self):
        # le fond
        self._fenetre.fill(_CLR_FOND)
        # les lignes horizontales
        for i in range(1, _NB_CASES[0]):
            p1 = (0, i*_TAILLE_CASE)
            p2 = (_LARGEUR, i*_TAILLE_CASE)
            pygame.draw.line(self._fenetre, _CLR_GRILLE, p1, p2, 1)
        # les lignes verticales
        for i in range(1, _NB_CASES[0]+1):
            p1 = (i*_TAILLE_CASE, 0)
            p2 = (i*_TAILLE_CASE, _HAUTEUR)
            pygame.draw.line(self._fenetre, _CLR_GRILLE, p1, p2, 1)
        # les murs
        for y in range(_NB_CASES[1]):
            for x in range(_NB_CASES[0]):
                if self._grille[y][x] == _MUR:
                    rect = (x*_TAILLE_CASE, y*_TAILLE_CASE, _TAILLE_CASE, _TAILLE_CASE)
                    pygame.draw.rect(self._fenetre, _CLR_MUR, rect)
        # les marques
        for y in range(_NB_CASES[1]):
            for x in range(_NB_CASES[0]):
                if self._grille[y][x] == _MARQUE:
                    x1 = x*_TAILLE_CASE + 5
                    y1 = y*_TAILLE_CASE + 5
                    x2 = x1 + _TAILLE_CASE - 10
                    y2 = y1 + _TAILLE_CASE - 10
                    pygame.draw.line(self._fenetre, _CLR_MARQUE, (x1,y1), (x2,y2))
                    pygame.draw.line(self._fenetre, _CLR_MARQUE, (x1,y2), (x2,y1))
                    
    def get_case(self, x, y):
        """
        Retourne la valeur d'une case
        """
        if not (0 <= x < _NB_CASES[0]):
            return _MUR 
        if not (0 <= y < _NB_CASES[1]):
            return _MUR 
        return self._grille[y][x]
    
    def grille_marques(self):
        """
        Retourne la matrice des marques
        """
        larg, haut = _NB_CASES
        marques = [[(self._grille[y][x] == _MARQUE) for x in range(larg)] for y in range(haut)]
        return marques
        
class _Robot:
    def __init__(self, fenetre, terrain, x, y, cap):
        self._fenetre = fenetre
        self._terrain = terrain
        self._x = x
        self._y = y
        self._cap = cap
        self._pos_initiale = (x,y,cap)
    
    def get_pos(self):
        return (self._x, self._y)
    
    def get_cap(self):
        return self._cap
    
    def get_pos_initiale(self):
        return self._pos_initiale
    
    def get_pos_devant(self):
        """
        retourne la position de la case devant le robot
        """
        if self._cap == "E": return (self._x+1, self._y)
        if self._cap == "W": return (self._x-1, self._y)
        if self._cap == "S": return (self._x, self._y+1)
        if self._cap == "N": return (self._x, self._y-1)
        
    def avancer(self):
        x,y = self.get_pos_devant()
        if terrain.get_case(x,y) != _MUR:
            self._x, self._y = x, y

    def tourner_droite(self):
        if self._cap == "E": self._cap = "S"
        elif self._cap == "W": self._cap = "N"
        elif self._cap == "S": self._cap = "W"
        elif self._cap == "N": self._cap = "E"

    def tourner_gauche(self):
        if self._cap == "E": self._cap = "N"
        elif self._cap == "W": self._cap = "S"
        elif self._cap == "S": self._cap = "E"
        elif self._cap == "N": self._cap = "W"

    def dessiner(self):
        rayon = int(_TAILLE_CASE * 0.4)
        xc = int(_TAILLE_CASE * (self._x + 0.5))
        yc = int(_TAILLE_CASE * (self._y + 0.5))
        xd, yd = xc, yc
        if self._cap == "E": xd += rayon
        if self._cap == "W": xd -= rayon
        if self._cap == "S": yd += rayon
        if self._cap == "N": yd -= rayon
        pygame.draw.circle(self._fenetre, _CLR_ROBOT[0], (xc,yc), rayon)
        pygame.draw.line(self._fenetre, _CLR_ROBOT[1], (xc,yc), (xd,yd), 3)

class _Tresor:
    def __init__(self, fenetre, x, y):
        self._fenetre = fenetre
        self._x = x
        self._y = y
    
    def dessiner(self):
        rayon = int(_TAILLE_CASE * 0.5)
        xc = int(_TAILLE_CASE * (self._x + 0.5))
        yc = int(_TAILLE_CASE * (self._y + 0.5))
        pygame.draw.circle(self._fenetre, _CLR_TRESOR, (xc,yc), rayon)
        
    def get_pos(self):
        return (self._x, self._y)

class _Message:
    def __init__(self, fenetre, texte):
        self._fenetre = fenetre
        self._txt = " " + texte + " "
    
    def dessiner(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(self._txt, True, (0,0,0), (255,255,0))
        rect = text.get_rect()
        rect.center = (_LARGEUR + _TEXTE//2, _HAUTEUR // 4)
        fenetre.blit(text, rect)
        
        
######### Fonctions internes (non exportables) #########################
def _demarrer_prog(p_robot, p_tresor, murs, texte):
    """
    Fonction à appeler par demarrer() du module exerciceN au début du programme
    Initialise la fenêtre, le terrain, ...
    """
    pygame.init()
    pygame.font.init()
    #---- la fenetre ----
    global fenetre
    fenetre = pygame.display.set_mode(_TAILLE)
    pygame.display.set_caption("Nono le robot")
    #---- le terrain ----
    global terrain
    terrain = _Terrain(fenetre, murs)
    #---- le robot ----
    global nono
    x,y,cap = p_robot
    nono = _Robot(fenetre, terrain, x, y, cap)
    #---- le trésor ----
    global tresor
    x,y = p_tresor
    tresor = _Tresor(fenetre, x, y)
    #---- le message de la mission ----
    global message
    message = _Message(fenetre, texte)
    # dessiner la fenetre
    _maj_fenetre()
    pygame.time.wait(_PAUSE)

def _afficher_message(txt):
    txt = " " + txt + " "
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render(txt, True, (0,0,0), (255,128,0))
    rect = text.get_rect()
    rect.center = (_LARGEUR + _TEXTE//2, _HAUTEUR * 3 // 4)
    fenetre.blit(text, rect)
    pygame.display.update()
    
def _maj_fenetre():
    terrain.dessiner()
    message.dessiner()
    tresor.dessiner()
    nono.dessiner() 
    pygame.display.update()
    pygame.time.wait(_PAUSE)




