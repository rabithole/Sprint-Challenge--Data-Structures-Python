class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity # clarify how this works!
        self.cur = 0

    def append(self, item):
        # add new item to front of buffer for it's specified size. 
        self.data[self.cur] = item
        self.cur += 1
        if self.cur == self.capacity:
            self.cur = 0

    def get(self):
        # creates a list from the buffer
        filtered_data = [element for element in self.data if element is not None]
        print(self.data)
        return filtered_data



buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')
buffer.append('l')
buffer.append('m')


buffer.get()