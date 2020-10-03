#SYSTEME D'EQUATION :
#
sys = [[100, 4, 51],[25, 2, 13]]
#
print('Avant : ' + str(sys))

"""
 Exemples :
- [[100, 4, 51],[25, 2, 13]]
- [[0,2, 1, 1, 11], [1,0, 4, 4, 22], [1,1,1,2,18],[1,2,0,0,18]]
- [[4,4,0,10],[2,1,1,6.5],[7,0,1,13]]
- PAS DE SOLUTION [[2,3,-5,17],[1,-1,1,0],[3,2,-4,7]]
- INFINITE DE SOLUTIONS [[3,-9,12,-9],[3,-7,8,-5],[0,3,-6,6]]
"""

# Cette fonction parcourt chaque indice de chaque ligne
def trouverIndicePivot():
    ligne = 0
    while(ligne < len(sys)):
        indice = 0
        max = len(sys[ligne])-1 # Indice du resultat
        while (sys[ligne][indice] == 0 and indice < max):
            indice += 1
        if(indice == max): # Si ligne de 0
            if sys[ligne][indice] == 0:
                sys.pop(ligne) # Suppression de la ligne
                print("Infinite de solutions")
            else: # Si ligne de 0 sauf resultat
                print('Pas de solution')
                return(-1) # Pas de solution
        else:
            return(indice) # L'indice du pivot
            ligne = len(sys)
        ligne+=1

def echanger(sys, a, b):
    sys[a],sys[b]=sys[b],sys[a]
    return(sys)

def calculTabSuivant(tab, indicePivot): # Cette fonction parcourt tout le tableau et en renvoie un autre sur lequel les calculs ont etes effectues
    TabSuivant = []
    TabSuivant.append(tab[0]) # ajout de la ligne du pivot
    indice=0
    ligne=1
    while ligne < len(tab):
        TabSuivant.append([])
        while indice < len(tab[ligne]):
            if (indice == indicePivot):
                TabSuivant[ligne].append(0) # 0 sur colonne du pivot
            else:
                TabSuivant[ligne].append((tab[0][indicePivot]*tab[ligne][indice])-
                 (tab[0][indice]*tab[ligne][indicePivot])) # Le produit en croix
            indice+=1
        indice = 0
        ligne+=1
    #print(TabSuivant) #-- DECOMMENTER POUR VOIR CHAQUES ETAPES
    return(TabSuivant)

def diviserContenu(ligne, div):
    i = 0
    while i < len(sys[ligne]):
        sys[ligne][i]/=div
        i+=1
    return(sys[ligne])

# BOUCLE PRINCIPALE

i = -1 # le -1 permet d'echanger la derniere et la premiere ligne
indicePivot = trouverIndicePivot()
while(i < len(sys)):
    sys = calculTabSuivant(sys, indicePivot) # calcul du prochain systeme
    echanger(sys, 0, i) # ligne sans pivot devient ligne de pivot
    i+=1
    indicePivot = trouverIndicePivot()
i = 0

# division de chaque ligne par la solution restante
ligne = 0
indice = 0
while(ligne < len(sys)):
    while(indice < len(sys[ligne])):
        if(sys[ligne][indice] != 0 and indice < len(sys[ligne])-1):
            sys[ligne] = diviserContenu(ligne, sys[ligne][indice])
        indice+=1
    indice=0
    ligne+=1

if indicePivot == -1: # Exception
    print('Pas de solution')
else: # Resultat
    print('Apres : ' + str(sys))
