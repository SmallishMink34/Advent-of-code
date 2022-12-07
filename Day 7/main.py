input = open("Day 7\input.txt", "r")
liste = input.readlines()

path = [] # Path en temps réel
dico = {} # Stocke l'arborecence
total = 0

# Partie 1
for ligne in liste:
    mots = ligne.strip().split() # Supprime les \n et les sépare
    if mots[1] == 'cd': # Changement de dossier
        if mots[2] == '..': # Retourne en arrière
            path.pop() # Supprime le dernier élément de la liste
        else:
            path.append(mots[2]) # Ajoute l'élément actuel à la liste
    elif mots[1] == 'ls' or mots[0] == 'dir': #Inutile 
        pass
    else:
        taille = int(mots[0]) # Taille du fichier
        total += taille #Total sur le disque
        print(taille)
        for i in range(1, len(path)+1): #Parcours le fil d'ariane 
            try:
                dico['/'.join(path[:i])] += taille #join : concatener les listes de str
                
            except KeyError:
                dico['/'.join(path[:i])] = taille # On evite l'erreur de dico vide

# Partie 2
   
for i in dico.keys(): # Affiche le dictionnaire
    print(i, dico[i])
    
espace = 30000000-( 70000000  - total) # Espace necessare
u = 0 # Taille des fichiers inferieur a 100000
v = 100000000000000 #Valeur extremement grande pour etre superieur à la taille total
for i in dico.keys():
    if dico[i] <= 100000:
        u += dico[i]
    if dico[i] >= espace:
        if v > dico[i]: # min
            v = dico[i]


print(u)
print(v) # Taille des fichiers superieur a l'espace necessaire