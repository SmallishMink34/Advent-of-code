liste = open('Day 4/index.txt', 'r')

input = liste.readlines()


def contains(sa, sb):
    if int(sa.split('-')[0]) <= int(sb.split('-')[0]) and int(sa.split('-')[1]) >= int(sb.split('-')[1]):
        return True
    elif int(sa.split('-')[0]) >= int(sb.split('-')[0]) and int(sa.split('-')[1]) <= int(sb.split('-')[1]):
        return True
    else:
        return False
    
conteur = 0
for i in range(len(input)):
        
    section_a = input[i].split(",")[0]
    section_b = input[i].split(",")[1]

    print(section_a, section_b)
    print(contains(section_a, section_b))

    if contains(section_a, section_b):

        conteur += 1
   
    
print(conteur)
