from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        if index > self.length():
			return "ERROR : index out of range!"
		elif index == self.length():
			self.append(data)
			return "Node Added"
		new_node = node(data)
		idx = 0
		cur = self.head
		while cur.next != None:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = new_node
				new_node.next = cur
				return "Node Added"
			idx += 1

    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        elements = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elements.append(cur.data)
		return elements


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        if first_list is None:
            first_list = 0
        else:
            first_list = first.data
        if second_list is None:
            secondData = 0
        else:
            secondData = second.data
        Sum = carry
        Sum += firstData
        Sum += secondData
        if Sum >= 10:
            carry = 1
        else:
            carry = 0
        Sum %= 10
        temp = Node(Sum)
        if self.head is None:
            self.head = temp
        else:
            prev.next = temp
        prev = temp
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next
    if carry > 0:
        temp.next = Node(carry)
        
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
