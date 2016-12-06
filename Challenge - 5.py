url = "http://www.pythonchallenge.com/pc/def/banner.p"

import requests , pickle ,sys

res = requests.get(url)
file = open("banner.p"  , 'wb')

for i in res.iter_content(100):
    file.write(i)

file.close()

file = open("banner.p" , 'rb' )

l = pickle.load(file)

for i in l :
    for j in i :
        for k in range(int(j[1])):
            sys.stdout.write(j[0])
    print "\t"
