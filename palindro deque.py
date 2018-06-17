#deque
def Deque():
    d=[]
    return(d)

def addfront(d,data):
    d.insert(0,data)
    return(d)

def addrear(d,data):
    d.append(data)
    return(d)

def removerear(d):
    data=d.pop()
    return(data)

def removefront():
    data=d.pop(0)
    return(data)


def isEmpty(d):
    return(d==[])

def size(d):
    return(len(d))



def palcek(kata):
    a = Deque()

    for i in kata:

        a.append(i)

        samadengan = True

        while len(a) > 1 and samadengan:
            pertama = a.pop(0)
            terakhir = a.pop()
            if pertama != terakhir:
                samadengan = False

    return samadengan

print(palcek('kamu'))
print(palcek('radar'))


