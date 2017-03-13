# A very basic version of a Queue has been implemented here without the use of lists for the Physical
# Web Project Test for GSoC 2017. The code has been written entirely by
# Tushar Gupta (tushar13113@iiitd.ac.in).

class MyQueue:

    def __init__(self):  # object initializer to set attributes (fields)
        self.number_of_elements = 0
        self.front = None
        self.end = None

    def put(self, val):
        # add a new element to the end of the queue
        new_node = Node(val)
        if self.number_of_elements == 0:
            self.end = new_node
            self.front = self.end
        else:
            self.end.next_node = new_node
        self.number_of_elements += 1

    def pop(self):
        # remove the element from the front of the queue and return it
        if not self.front:
            return -1
        popped_element = self.front.value
        self.front = self.front.next_node
        self.number_of_elements -= 1
        return popped_element

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return -1
        # returns the element at the head of the queue, without removing it.


class Node:

    def __init__(self, val):  # object initializer to set attributes (fields)
        self.value = val
        self.next_node = None
