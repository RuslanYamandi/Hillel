class frange:
    def __init__(self, left=0, right=None, step=1):
        self._left = left
        self._right = right
        self._step = step
        if self._right is None:
            self._left, self._right = 0, self._left

    def __next__(self):
        step = 0 if isinstance(self._step, float) else self._step
        if self._step >= 0:
            if self._left + step > self._right:
                raise StopIteration
        else:
            if self._left + step < self._right:
                raise StopIteration
        result = self._left
        self._left += self._step
        return result

    def __iter__(self):
        return self


def my_assert(a, b):
    print(a)
    assert a == b


my_assert(list(frange(5)), [0, 1, 2, 3, 4])
my_assert(list(frange(2, 5)), [2, 3, 4])
my_assert(list(frange(2, 10, 2)), [2, 4, 6, 8])
my_assert(list(frange(10, 2, -2)), [10, 8, 6, 4])
my_assert(list(frange(2, 5.5, 1.5)), [2, 3.5, 5])
my_assert(list(frange(1, 5)), [1, 2, 3, 4])
my_assert(list(frange(0, 5)), [0, 1, 2, 3, 4])
my_assert(list(frange(0, 0)), [])
my_assert(list(frange(100, 0)), [])

print('SUCCESS!')
