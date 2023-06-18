class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2, carry=0):
    if not l1 and not l2 and carry == 0:
        return None

    sum = carry
    if l1:
        sum += l1.val
        l1 = l1.next
    if l2:
        sum += l2.val
        l2 = l2.next

    node = ListNode(sum % 10)
    carry = sum // 10
    node.next = addTwoNumbers(l1, l2, carry)

    return node

# Helper function to convert a list to a linked list
def createLinkedList(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to convert a linked list to a list
def convertLinkedListToList(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

# Testing the code with the provided examples
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(convertLinkedListToList(result))  

l1 = createLinkedList([0])
l2 = createLinkedList([0])
result = addTwoNumbers(l1, l2)
print(convertLinkedListToList(result)) 

l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = createLinkedList([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
print(convertLinkedListToList(result))  
