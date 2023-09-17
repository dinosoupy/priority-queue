import unittest
from pqueue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue((3, 1, 2))
        pq.enqueue((1, 2, 3))
        pq.enqueue((2, 3, 4))

        self.assertEqual(pq.queue, [(3, 1, 2), (1, 2, 3), (2, 3, 4)])

    def test_dequeue(self):
        pq = PriorityQueue()
        pq.enqueue((3, 1, 2))
        pq.enqueue((1, 2, 3))
        pq.enqueue((2, 3, 4))

        self.assertEqual(pq.dequeue(), (3, 1, 2))
        self.assertEqual(pq.dequeue(), (2, 3, 4))

    def test_peek(self):
        pq = PriorityQueue()
        pq.enqueue((3, 1, 2))
        pq.enqueue((1, 2, 3))
        pq.enqueue((2, 3, 4))

        self.assertEqual(pq.peek(), (3, 1, 2))

if __name__ == '__main__':
    unittest.main()
