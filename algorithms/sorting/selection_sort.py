import unittest
import random

def selection_sort(seq):
    for i in xrange(len(seq)):
        i_min = i
        for j in xrange(i+1, len(seq)):
            if seq[j] < seq[i_min]:
                i_min = j
        if i_min != i:
            seq[i], seq[i_min] = seq[i_min], seq[i]

    return seq

class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.input = range(10)
        random.shuffle(self.input)
        self.correct = range(10)

    def selection_sort_test(self):
        self.output = selection_sort(self.input)
        assertEquals(self.output, self.correct)

if __name__ == '__main__':
    unittest.main()
