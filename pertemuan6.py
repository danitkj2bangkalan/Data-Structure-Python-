#rekursif
#def fakto(angka):
#    bilangan = angka+1
#    for i in range(bilangan):
#        i=i*(angka+1)
#        print(i,end = "x")

#fakto(5)

#def factrec(n):
#    if n<=1:
#        return(1)
#    else:
#        temp = n * factrec(n-1)
#        return(temp)

#data=factrec(4)
#print(data)

#triangular number

#def triangularNumbers(n):
    #if n==1:
    #    return(1)
    #else:
    #    return(n + triangularNumbers(n-1))
#triangularNumbers(4)

#def kon(n):
#    temp=[]
#    if n==0:
#        return('1')
#    elif n == 1:
#        return('0')
#    else:
#        b=n//2
#        sisa=str(n%2)
#        temp=kon(b)+sisa
#        return(temp)
#print(kon(4))

#def towers(n,awal,bantuan,tujuan):
#    if n==1:
#        print('piringan -1 ',awal,'ke ',tujuan)
#    else:
#        towers(n-1,awal,tujuan,bantuan)
#        print('piringan =',n,'dari-',awal,'ke-',tujuan)
#        towers(n-1,bantuan,awal,tujuan)
#towers(4,'A','B','C')

#!tugas conver bilanga ke hex dan octal
# buat knapsack dengan rekursif

def  binkeocta(n):
    tujuh = '111'
    enam = '110'
    lima = '101'
    empat = '010'
    tiga = '011'
    dua = '010'
    satu = '001'
    nol = '000'
    temp=[]
    if len(temp) == 0:
        if n == 1:
            return('1')
        elif n == 0:
            return('0')
        else:
            b=n//2
            sisa=str(n%2)
            temp=binkeocta(b)+sisa
            return(temp)
    else:
        if temp == tujuh:
            print('7')
        elif temp == enam:
            print('6')
        elif temp == lima:
            print('5')
        elif temp == empat:
            print('4')
        elif temp == tiga:
            print('3')
        elif temp == dua:
            print('2')
        elif temp == satu:
            print('1')
        elif temp == nol:
            print('0')


print(binkeocta(8))