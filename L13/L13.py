import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
multicall = xmlrpclib.MultiCall(proxy)

multicall.phone("Bert")
print tuple(multicall())[0]

#Answer is ITALY
