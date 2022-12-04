liste = open('Day 4/input.txt', 'r')

input = liste.readlines()


def contains(sa, sb):
    number = [i for i in range(int(sa.split('-')[0]), int(sa.split('-')[1])+1)]
    number2 = [i2 for i2 in range(int(sb.split('-')[0]), int(sb.split('-')[1])+1)]
    
    return True if len(list(set(number) & set(number2))) != 0 else False


conteur = 0
for i in range(len(input)):
    section_a = input[i].split(",")[0]
    section_b = input[i].split(",")[1]
    
    if contains(section_a, section_b):
        conteur += 1

   
    
print(conteur)
