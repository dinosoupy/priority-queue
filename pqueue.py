# Copyright (c) 2023 Anish Basu
# This code is licensed under the MIT License.

class PriorityQueue:
    """
    This class implements a priority queue using a heap data structure.
    """

    def __init__(self):
        """
        Initializes an empty priority queue.
        """
        self.queue = []

    def enqueue(self, item):
        """
        Inserts an item into the priority queue.

        Args:
            item: A tuple representing (priority, data).
        """
        self.queue.append(item)
        self.siftUp(len(self.queue)-1)

    def dequeue(self):
        """
        Removes and returns the item with the highest priority from the queue.
        Returns None if the queue is empty.

        Returns:
            A tuple representing (priority, data).
        """
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            return self.queue.pop()

        root = self.queue[0]
        self.queue[0] = self.queue.pop()
        self.siftDown(0)
        return root

    def peek(self):
        """
        Returns the item with the highest priority without removing it from the queue.
        Returns None if the queue is empty.

        Returns:
            A tuple representing (priority, data).
        """
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def siftUp(self, index):
        """
        Moves the item at index up the heap to maintain the heap property.

        Args:
            index: The index of the item to be moved up.
        """
        parent = (index - 1) // 2
        if index > 0 and self.queue[parent][0] < self.queue[index][0]:
            self.queue[parent], self.queue[index] = self.queue[index], self.queue[parent]
            self.siftUp(parent)

    def siftDown(self, index):
        """
        Moves the item at index down the heap to maintain the heap property.

        Args:
            index: The index of the item to be moved down.
        """
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.queue) and self.queue[left][0] > self.queue[largest][0]:
            largest = left
        if right < len(self.queue) and self.queue[right][0] > self.queue[largest][0]:
            largest = right

        if largest != index:
            self.queue[largest], self.queue[index] = self.queue[index], self.queue[largest]
            self.siftDown(largest)

