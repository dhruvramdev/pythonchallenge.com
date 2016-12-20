#look and say series


def lookandsay(number) :
    number = str(number)
    ans = ""
    
    temp = { number[0] : 1 }
    for i in number[1:] :
        if i in temp :
            temp[i] += 1
        else :
            var = temp.keys()[0]
            ans +=  str(temp[var]) + var 
            temp = { i : 1}

    var = temp.keys()[0]
    ans +=  str(temp[var]) + var
    return int(ans)

li = [1]
temp = 1
for i in range(30):
    temp = lookandsay(temp)
    li.append( len(str(temp)))

print li[30]
            
        
