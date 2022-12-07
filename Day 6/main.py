input = open("Day 6\input.txt", "r")
liste = input.read()
save = -1
print(len(liste))

def ishere(x, tab):
    reponse = True
    tab = list(tab)
    for i in range(len(tab)):
        if x == tab[i]:
            reponse = False
    return not reponse

print(ishere("d", "abc"))

save = 0
counter = 0


for i in range(len(liste)):
    #print(i, liste[i], liste[i+1: i+14])
    if ishere(liste[i], liste[i+1: i+14-counter]):
        counter = 0
        print(i,'dommage')
    else:
        counter += 1
        save = i+1

    
    if counter == 14:
        #print("here")
        break


                
print(save)

