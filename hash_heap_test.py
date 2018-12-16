from HashHeap import HashHeap
import unittest


class HashHeapTest(unittest.TestCase):
    def setUp(self):
        self.hash_heap = HashHeap()

    def test_add_item(self):
        self.hash_heap.add(1, 2)
        self.assertEqual(2, self.hash_heap.find(1))