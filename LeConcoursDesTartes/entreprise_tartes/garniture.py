#=======================================================================
# fichier : garniture.py
# but     : la confection de la garniture d'une tarte aux fruits
# auteur  : 
# date    : 
#=======================================================================

######### Importations de modules ######################################
from garniture_fraise import garnir_fraise
from garniture_pomme import garnir_pomme
from garniture_rhubarbe import garnir_rhubarbe
from garniture_abricot import garnir_abricot
from garniture_noix import garnir_noix
from garniture_chocolat import garnir_chocolat

######### Variables ####################################################
garniture = {"fraise" : garnir_fraise, "pomme" : garnir_pomme, "rhubarbe" : garnir_rhubarbe,
          "abricot" : garnir_abricot, "noix" : garnir_noix , "chocolat" : garnir_chocolat}

######### La fonction à ne pas modifier ################################
def garnir(fruit):
    garniture[fruit]()

######### La fonction à compléter ######################################
# pour la garniture à rajouter sur la rhubarbe
def recouvrir_rhubarbe():
    # à compléter ; penser à enlever le pass
    pass
    

    

  
