#class and object

#class BilanganKompleks:
#    def __init__(self,a,b):
#        self.real=a
#        self.im=b
#    def display(self):
#        print(self.real,'+',self.im,'i')
#    def __str__(self):
#        return str(self.real)+"+"+str(self.im)+"i"
#    def jumlah(self,obj):
#        return str(self.real+obj.real)+"+"+str(self.im+obj.im)+"i"
#    def jumlah1(self,obj):
#        self.real=self.real+obj.real
#        self.im=self.im+obj.im
#    def __add__(self,data):
#        temp1=self.real+data.real
#        temp2=self.im+data.im
#        return BilanganKompleks(temp1,temp2)
    #def __div__(self,data):
    #    temp1=self.real/data.real
    #    temp2=self.im/data.im
        #return BilanganKompleks(temp1,temp2)
    #def __mul__(self,data):
    #    temp1=self.real*data.real
    #    temp2=self.im*data.im
    #    return BilanganKompleks(temp1,temp2)
    #def __reduce__(self,data):
    #    temp1=self.real-data.real
    #    temp2=self.im-data.im
    #    return BilanganKompleks(temp1,temp2)
#data1=BilanganKompleks(4,5)
#data2=BilanganKompleks(3,5)
#data1.jumlah1(data2)
#print(data1)
#d=data1+data2
#e=data1*data2
#print(d)
#print(e)

#buat overrading pengurangan dan perkalian dan pembagian

#linked list
#Node ada dua informasi yaitu, data dan next(pointer)

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,new_data):
        self.data = new_data
    def setNext(self,new_next):
        self.next = new_next
 #temp adalah object
#temp=Node(93)
#print(temp.getData())
#print(temp.getNext())

#num=Node(56)
#print(num.getData())
#print(num.getNext())

#temp.setNext(num)
#print(temp.getNext().data)
#untuk mengarahkan ke node selanjutnya

#link list
class Linkedlist:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    #digunakan unutk mengubah head dengan data yang baru
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        jumlah=0
        while current != None and not found:
            jumlah +=1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                return None
        return jumlah
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def remove(self,item):
        current = self.head
        previous= None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current =current.getNext()
        if previous == None:
            self.head = current.getNext()
        else :
            previous.setNext(current.getNext())
mylist=Linkedlist()
mylist.add(45)
mylist.add(34)
mylist.add(70)
print(mylist.head.data)
print(mylist.search(70))
#buat method insertNext dan insertPrevious dan insertLast 

#order linked list
class OrderLinkedlist:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
    def add(self,item):
        current= self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp= Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

#
    
