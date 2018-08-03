f = open("Challenge2resource")
s = f.read()

def analyze(st):
    z = {}
    for i in st:
        if i in z:
            z[i] += 1
        else:
            z[i] = 1
    print(z)

analyze(s)