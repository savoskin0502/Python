class RangeIterator:
    def __init__(self, start=0, top=0):
        self.top = top
        self.current = start if start else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            self.current = 0
            raise StopIteration
        current = self.current
        self.current = self.current + 1
        return current


if __name__ == "__main__":
    for i in RangeIterator(2, 3):
        print(i)
