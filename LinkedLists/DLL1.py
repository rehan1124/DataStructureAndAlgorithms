"""
Implementation of Doubly Linked List
"""


class Node:
    def __init__(self, data=None, next=None, prev=None):
        """
        Node creation
        :param data: Data to be added in Double Linked List
        :type data:
        :param next: Pointer to next Node
        :type next:
        :param prev: Pointer to previous Node
        :type prev:
        """
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        pass

    def insert_at_end(self, data):
        """
        Append data to Double Linked List
        :param data: Data to be added
        :type data:
        :return:
        :rtype:
        """
        # If Double Linked List is empty or have not been created, then create a new
        # one.
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = new_node
            return

        # If Double Linked List is not empty, then append data to it.
        itr = self.head
        while itr.next:  # Check if reached last Node.
            itr = itr.next  # Keep iterating till we reach the end.

        # Once we reach the end of Double Linked List, create a new Node and append.
        itr.next = Node(data, None, itr)
        return

    def print_forward(self):
        dl_str = ""
        itr = self.head
        while itr:
            dl_str += str(itr.data) + "-->"
            itr = itr.next
        print(dl_str)


if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.insert_at_end(10)
    dl.insert_at_end(9)
    dl.insert_at_end(15)
    dl.insert_at_end(20)
    dl.insert_at_end(1)
    dl.print_forward()  # 10-->9-->15-->20-->1-->
