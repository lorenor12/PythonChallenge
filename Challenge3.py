import re
f = open("Challenge3resource")
s = f.read()




def sda ():
    l = ""
    for i in re.findall("[^A-Z][A-Z]{3,3}[a-z][A-Z]{3,3}[^A-Z]", s):
            l = l + i[4]
    print(l)
sda()
