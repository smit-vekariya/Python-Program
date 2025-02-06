# https://www.w3schools.com/dsa/dsa_theory_linkedlists_memory.php
# https://www.w3schools.com/dsa/dsa_data_linkedlists_types.php

# =============================== EX: 1
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

node1 = Node(4)
node2 = Node(3)
node3 = Node(2)
node4 = Node(1)

node4.next = node3 
node3.next = node2  
node2.next = node1  
# node1.next = node4 #(this going to loop and also called circuler singly linked list)

print("EX 1")
currentNode = node4
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.next
print("null")


# ============================ EX: 2
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(1)

node4.next = node1  #data = 1, next data =2
node1.next = node2  #data = 2, next data = 3
node2.next = node3  #data = 3, next data =4
# node3.next = node4 #data = 4, next data=1 #(this going to loop and also called circuler singly linked list)

print("EX 2")
currentNode = node4
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.next
print("null")