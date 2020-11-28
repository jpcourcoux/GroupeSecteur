#=======================================================================
# fichier : tartes.py
# but     : le programme principal pour une recette de tarte aux fruits
# auteur  : Mme Le Bihan
# date    : 14/11/20
#=======================================================================

######### Importations de modules ######################################
from confection import confectionner_tarte

######### Variables ####################################################
# les fruits disponibles
fruits = ["pomme", "noix", "chocolat","rhubarbe", "fraise", "abricot"]


######### PROGRAMME PRINCIPAL ##########################################        
print("Choisir un fruit parmi :",fruits)
fruit=""
while fruit not in fruits:
    fruit = input("Vous choisissez : ")
confectionner_tarte(fruit)
        
        
        
        
    