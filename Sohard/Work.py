def main():
    word()
    sentense()
    coloum()
    package()

def word():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    words = infile.split()
    words = (len(words)-1)
    print(words)
    
def sentense():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    sentenses = infile.split('.')
    sentenses = (len(sentenses)-1)
    print(sentenses)

def coloum():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    col = infile.split('\n')
    col = (len(col)-1)
    print(col)

def package():
    alpha()
    upper()
    lower()
    special()

def alpha():
    outfile=open('read.txt',"r")
    infile=outfile.read()
    outfile.close()
    alp=0
    for i in infile:
        if i.isalpha() == True:
            alp = alp + 1
        else:
            pass
    print(alp)

def upper():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    up = 0
    for i in infile:
        if i.isupper() == True:
            up = up + 1
        else:
            pass
    print(up)

def lower():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    low = 0
    for i in infile:
        if i.islower() == True:
            low = low + 1
        else:
            pass
    print(low)

def special():
    outfile = open('read.txt','r')
    infile = outfile.read()
    outfile.close()
    spec = 0
    for i in infile:
        if i == "." or  i == "(" or i == ")" or i == ";" or i == "," or i == "/" :
            spec = spec + 1
        else:
            pass
    print(spec)


main()