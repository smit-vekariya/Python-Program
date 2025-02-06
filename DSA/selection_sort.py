unsort = [2, 4, 6, 1, 34, 45, 22, 2, 1]
print("Unsorted:", unsort)

for index, data in enumerate(unsort):
    min = unsort[index]
    for i in range(index+1, len(unsort), 1):
        if unsort[index] > unsort[i]:
            unsort[index],  unsort[i]= unsort[i], unsort[index]
        
print("Sorted:", unsort)

# selection sort for singly linked list

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeKLists(self, node):
        
#         print("Before sort:")
#         currentNode1 = node
#         while currentNode1:
#             print(currentNode1.val ,end=", ")
#             currentNode1 = currentNode1.next
            
#         currentNode2 = node
#         while currentNode2:
#             min_node = currentNode2
#             next_node = currentNode2.next
            
#             while next_node:
#                 if min_node.val > next_node.val:
#                     next_node.val ,min_node.val= min_node.val, next_node.val
#                 next_node = next_node.next
            
#             currentNode2.val ,min_node.val= min_node.val, currentNode2.val
#             currentNode2 = currentNode2.next
        
#         print("\nAfter sort:")
#         currentNode3 = node
#         while currentNode3:
#             print(currentNode3.val ,end=", ")
#             currentNode3 = currentNode3.next
        
# obj = Solution()
# list = ListNode(1, ListNode(4, ListNode(5, ListNode(1, ListNode(3, ListNode(4, ListNode(2, ListNode(6))))))))
# obj.mergeKLists(list)
