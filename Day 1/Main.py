liste = open('Day 1/input.txt', 'r')

somme_liste = [0]
indice_somme = 0
for i in liste.readlines():
    if i.strip() == '':
        print(i)
        indice_somme += 1
        somme_liste.append(0)
    else:
        print(i)
        somme_liste[indice_somme] += int(i.strip())
        
# Affiche la sommes des trois Elfs ayant le plus de Calories dans leurs Sac
print(sorted(somme_liste)[-1]+sorted(somme_liste)[-2]+sorted(somme_liste)[-3])