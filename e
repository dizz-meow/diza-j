class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        # Initialize an array of size k with None values
        self.queue = [None] * k
        self.max_size = k
        self.head = 0
        self.tail = 0
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        # Insert value at the tail pointer
        self.queue[self.tail] = value
        # Move tail forward circularly
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1
        return True

    def deQueue(self):
        """
        :type : bool
        """
        if self.isEmpty():
            return False
        
        # Remove value by resetting it to None (optional but good practice)
        self.queue[self.head] = None
        # Move head forward circularly
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        """
        :type : int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        :type : int
        """
        if self.isEmpty():
            return -1
        # The rear element is always 1 step behind the tail pointer circularly
        return self.queue[(self.tail - 1 + self.max_size) % self.max_size]

    def isEmpty(self):
        """
        :type : bool
        """
        return self.size == 0

    def isFull(self):
        """
        :type : bool
        """
        return self.size == self.max_size

