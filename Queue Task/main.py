# A very basic version of a Queue has been implemented here without the use of lists for the Physical
# Web Project Test for GSoC 2017. The code has been written entirely by
# Tushar Gupta (tushar13113@iiitd.ac.in).

from myQueue.myQueue import MyQueue, Node

new_queue = MyQueue()
number_of_commands = int(raw_input())

for i in range(0, number_of_commands):
    inp = raw_input()
    if inp[0] == '1':
        value = int(inp.split()[1])
        new_queue.put(value)
    elif inp[0] == '2':
        popped_element = new_queue.pop()
    else:
        print new_queue.peek()
