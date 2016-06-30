import unittest
import random

def insertion_sort(seq):
    for index in xrange(len(seq)):
        position = index
        while ( position > 0 and seq[position] < seq[position-1] ):
            seq[position], seq[position-1] = seq[position-1], seq[position]
            position -= 1

    return seq

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.input = range(10)
        random.shuffle(self.input)
        self.correct = range(10)

    def insertion_sort_test(self):
        self.output = insertion_sort(self.input)
        assertEquals(self.output, self.correct)

if __name__ == "__main__":
    unittest.main()
