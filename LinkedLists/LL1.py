"""
Programs on Linked Lists

1- Python Linked Lists stores value at random locations but are linked to pointers to next element
2- Order is O(1) for inserting/deleting element at Start of LL
3- Order is O(n) for inserting/deleting element at end of LL
4- No pre-allocated space
5- LL traversal = O(n)
5- Accessing element by value = O(n)

Geometric progression based allocation of memory for Python Lists

https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4

Check for Double LL and Circular LL
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for items in data_list:
            self.insert_at_end(items)

    def __str__(self):
        if self.head is None:
            return "LL is empty!!!"

        itr = self.head
        ll_str = ""
        while itr:
            ll_str += str(itr.data) + "--->"
            itr = itr.next
        return ll_str

    def __len__(self):
        if self.head is None:
            return "List is empty..."
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter


if __name__ == "__main__":
    ll = LinkedList()
    print("Initial...")
    print(ll)  # LL is empty!!!
    print("### Inserting values at the beginning ###")
    ll.insert_at_beginning(55)
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(-100)
    print(ll)  # -100--->2--->9--->55--->
    print("### Insert element at the end ###")
    del ll  # Delete the object created so that previous list is destroyed
    ll = LinkedList()
    ll.insert_at_end(99)
    ll.insert_at_end(999)
    ll.insert_at_end(111)
    print(ll)  # 99--->999--->111--->
    print("### Inserting all the values present in list into a Linked List ###")
    ll.insert_values(["Banana", "Mango", "Grapes", "Orange"])
    print(ll)  # Banana--->Mango--->Grapes--->Orange--->
    print("### Length of Linked List created ###")
    print(f"Length: {len(ll)}")  # 4
