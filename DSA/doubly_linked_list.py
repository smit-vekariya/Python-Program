# https://www.w3schools.com/dsa/dsa_data_linkedlists_types.php

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

node1= Node(4)
node2= Node(1)
node3= Node(2)
node4= Node(5)
node5= Node(3)

node2.next = node3
# node2.pre = node4 #(this is going to loop and also called circuler dubly linked list for backword list)

node3.next = node5
node3.pre = node2

node5.next = node1
node5.pre = node3

node1.next = node4
node1.pre = node5

# node4.next = node2 #(this is going to loop and also called circuler dubly linked list for forward list)
node4.pre = node1

# forward list
currentNode = node2
while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
print("null")

#backword list
currentNode= node4
while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.pre
print("null")