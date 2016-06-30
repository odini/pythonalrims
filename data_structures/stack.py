"""
Implementing a basic Stack. The stack supports push, and pop with O(1). The
implementation is also extended to support min and max in O(1).
"""
class Stack(object):
    def __init__(self):
        self.items = []
        self._maxitems = []
        self._minitems = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        index = len(self.items) - 1
        if ( self._maxitems == [] or item >= self._maxitems[-1][1] ):
            self._maxitems.append((index, item))
        if ( self._minitems == [] or item <= self._minitems[-1][1] ):
            self._minitems.append((index, item))

    def pop(self):
        try:
            cur_pop = self.items.pop()
            if cur_pop == self._maxitems[-1][1]:
                self._maxitems.pop()
            if cur_pop == self._minitems[-1][1]:
                self._minitems.pop()
        except IndexError:
            print "Stack is empty"

    def size(self):
        return len(self.items)

    def max(self):
        cur_max = self._maxitems.pop()
        self.items.pop(cur_max[0])
        return cur_max[1]

    def min(self):
        cur_min = self._minitems.pop()
        self.items.pop(cur_min[0])
        return cur_min[1]
