import os

input = open("Day 7\input.txt", "r")
liste = input.readlines()

path = 'Day 7/C'

dico = {}
path = [] # Path en temps réel
total = 0

for line in liste:
    words = line.strip().split()
    if words[1] == 'cd': # Changement de dossier
        if words[2] == '..': # Retourne en arrière
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls': #Inutile 
        pass
    elif words[0] == 'dir':
        pass
    else:
        taille = int(words[0]) # Taille du fichier
        total += taille #Total sur le disque
        print(taille)
        for i in range(1, len(path)+1): #Parcours le fil d'ariane 
            try:
                dico['/'.join(path[:i])] += taille #join concatener les listes
                
            except KeyError:
                dico['/'.join(path[:i])] = taille
            
for i in dico.keys():
    print(i, dico[i])
    
espace =30000000-( 70000000  - total) # Espace necessare
u = 0 # Taille des fichiers inferieur a 100000
v = 100000000000000 #Valeur extremement grande pour etre superieur a la taille total
for i in dico.keys():
    if dico[i] <= 100000:
        u += dico[i]
    if dico[i] >= espace:
        v = min(v, dico[i])

print(u)
print(v) # Taille des fichiers superieur a l'espace necessaire