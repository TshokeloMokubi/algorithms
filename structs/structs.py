class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        n = 0
        cur = self.head
        while cur.next != None:
            n+=1
            cur = cur.next
        return n

    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            elements.append(cur.next.data) # the chained cur.next.data is my own thing it worked 
            cur = cur.next
        print(elements)
            
    def get(self,index):
        if index >=self.length():
            print('error')
            return None
        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index:
                print(cur.data)
                return cur.data
            cur_idx +=1
            
    def erase(self,index):
        if index>=self.length():
            return 'error'
        cur_node = self.head
        cur_idx = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return None 
            cur_idx += 1

ll = linked_list()
ll.append(32)
ll.append(53)
ll.append(756)
ll.append(8567)

ll.display()
ll.get(2)
ll.erase(2)
ll.display()
