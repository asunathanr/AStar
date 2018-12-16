from HashHeap import HashHeap
import unittest


class HashHeapTest(unittest.TestCase):
    def setUp(self):
        self.hash_heap = HashHeap()

    def test_add_item(self):
        self.hash_heap.add(1, 2)
        self.assertEqual(2, self.hash_heap.find(1))

    def test_pop(self):
        self.hash_heap.add(1, 2)
        key, value = self.hash_heap.pop()
        self.assertEqual(1, key)
        self.assertEqual(2, value)
        self.assertIsNone(self.hash_heap.find(1))
