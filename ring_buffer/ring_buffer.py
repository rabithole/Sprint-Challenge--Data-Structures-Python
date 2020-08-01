class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        # self.data.append(item)
        if len(self.data) <= self.capacity:
        	self.data.append(item)
        if len(self.data) == self.capacity + 1:
        	# self.data.append(item)
        	self.data.pop(0)
        print('append', self.data)

    def get(self):
        while self.data:
        	print('I got', self.data)
        	return self.data



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