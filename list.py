class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
self.next = new_next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
return None

def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                return current
            prev = current
            current = current.get_next()
        return None

    def print(self):
        lst = []
        current = self.head
        while current:
            lst.append(str(current.get_data()))
            current = current.get_next()
print('->'.join(lst))

# merge sort 12-17-2018
def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
return merge(a,b)

# add by miami on 12-17-2017
class myStack:
     def __init__(self):
         self.container = []  

     def isEmpty(self):
         return self.size() == 0   
     def push(self, item):
         self.container.append(item)  

     def pop(self):
         return self.container.pop()  

     def size(self):
         return len(self.container)  

