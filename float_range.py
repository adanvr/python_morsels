class float_range:
    def __init__(self, start, stop, step):
        if stop == None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        x = self.start
        if self.step > 0:
            while x < self.stop:
                yield x
                x += self.step
        else:
            while x > self.stop:
                yield x
                x += self.step
    def __len__(self):
        diff = self.stop-self.start
        if diff*self.step < 0:
            return 0
        div = diff // self.step
        mod = diff % self.step
        if mod == 0:
            return int(div)
        else:
            return int(div + 1)
    def __reversed__(self):
        i = self.start + (len(self)-1)*self.step
        for _ in range(len(self)):
            yield i
            i -= self.step
