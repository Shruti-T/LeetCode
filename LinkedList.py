# ---------------------------------- simple linked list based code ----------------------------------------
# class Node:
#     def __init__(self,data):
#         self.data = data;
#         self.next = None;

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp=temp.next

# llist = LinkedList()
# llist.head = Node(1)
# second = Node(2)
# third = Node(3)
# llist.head.next = second
# second.next = third
# llist.printList()

# ---------------------------------- user defined elements added --------------------------------------------
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

def pointerEle(old):
    if(x==1):
        llist.head.next = ele
    else:
        old.next = ele

totalEle = input("enter no.of elements to be added to linked list: " )
arr = []
print('Enter elements: ')
for i in range(0,int(totalEle)):
    x = int(input())
    arr.append(x)

llist = LinkedList()
x = 0
old = llist
for j in range(0,int(totalEle)):
    if(llist.head == None):
        llist.head = Node(arr[j])
        x=1
    else:
        ele = Node(arr[j])
        pointerEle(old)
        old = ele
        x=0

print('linked list:')
llist.printList()