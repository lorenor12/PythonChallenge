import urllib.request
import regex

s= "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

def url ():
    n = "12345"
    for i in range(0,400):
        s = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + n
        n = ""

        z = urllib.request.urlopen(s)
        n = n.join(regex.findall("[0-9]", str(z.read())))
        print(s)
    print(urllib.request.urlopen(s).read())


z = urllib.request.urlopen(s)

url()
print()