file = open('3.txt' , 'r')

abc = file.readlines()

for i in abc :
    for j in range(len(i)):
        if i[j].islower() == True :
            flag = False
            try:
                if (i[j-3:j].isupper() and i[j+1:j+4].isupper()):
                    if (i[j-4].islower() and i[j+4].islower()) :
                        temp  =i[j-3:j+4]
                        print temp,
            except :
                pass
