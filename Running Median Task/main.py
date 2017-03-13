# This code has been written entirely by Tushar Gupta (tushar13113@iiitd.ac.in) to solve the running
# median problem for the Physical Web Project GSoC task. This uses the heapq library to solve the
# given problem in O(nlogn) time.

import heapq

number_of_commands = int(raw_input())

stream = []
right_min_heap = []
left_max_heap = []
heapq.heapify(right_min_heap)  # min heap
# min heap -- can be used as a max heap by inserting negative of all elements
heapq.heapify(left_max_heap)

left_size = 0
right_size = 0

for i in range(0, number_of_commands):
    new_number = float(raw_input())
    stream.append(new_number)

    if len(stream) == 1:
        print new_number
    elif len(stream) == 2:
        heapq.heappush(left_max_heap, -1 * min(stream))
        left_size += 1
        heapq.heappush(right_min_heap, max(stream))
        right_size += 1
        median = sum(stream) / 2
        print median
    else:
        if new_number < -1 * left_max_heap[0]:
            heapq.heappush(left_max_heap, -1 * new_number)
            left_size += 1
        else:
            heapq.heappush(right_min_heap, new_number)
            right_size += 1

        # maintaining heap sizes by moving elements between the two heaps if number of elements differs by
        # more than 1
        if left_size - right_size > 1:
            heapq.heappush(right_min_heap, -1 * heapq.heappop(left_max_heap))
            left_size -= 1
            right_size += 1

        if right_size - left_size > 1:
            heapq.heappush(left_max_heap, -1 * heapq.heappop(right_min_heap))
            right_size -= 1
            left_size += 1

        # finding and printing the median after insertion
        if right_size == left_size:
            median = (-1 * left_max_heap[0] + right_min_heap[0]) / 2
        else:
            if left_size > right_size:
                median = -1 * left_max_heap[0]
            else:
                median = right_min_heap[0]

        print median
