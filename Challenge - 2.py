file = open('2.txt' , 'r')

abc = file.readlines()

h = dict()

for i in abc :
    for j in i :
        if h.has_key(j) == True :
            h[j] += 1
        else :
            h[j] = 1
            print j

print h
