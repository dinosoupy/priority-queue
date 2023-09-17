class PriorityQueue:

	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		# print(f"enqueueing {item}")
		self.queue.append(item)
		self.siftUp(len(self.queue)-1)

	def dequeue(self):
		
		if len(self.queue) == 0:
			return None
		if len(self.queue) == 1:
			root = self.queue.pop()
			# print(f"dequeueing {root}")
			return root


		root = self.queue[0]
		self.queue[0] = self.queue.pop()
		self.siftDown(0)
		# print(f"dequeueing {root}")
		return root

	def peek(self):

		if len(self.queue) == 0:
			return None
		else:
			# print(f"peeking {self.queue[0]}")
			return self.queue[0]

	def add_wait(self):
		for i in range(len(self.queue)):
			priority, arrival_time, service_time = self.queue[i]
			self.queue[i] = (priority, arrival_time + 0.1, service_time)

	def siftUp(self, index):
		parent = (index - 1) // 2
		if index > 0 and self.queue[parent][0] < self.queue[index][0]:
			self.queue[parent], self.queue[index] = self.queue[index], self.queue[parent]
			self.siftUp(parent)
		return

	def siftDown(self, index):
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

		return
