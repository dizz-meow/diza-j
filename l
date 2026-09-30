class MyCircularQueue:

  def __init__(self, k: int):
    self.capacity = k
    self.queue = [0] * k
    self.head = -1
    self.tail = -1

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False
    if self.isEmpty():
      self.head = 0
    self.tail = (self.tail + 1) % self.capacity
    self.queue[self.tail] = value
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    if self.head == self.tail:
      self.head = -1
      self.tail = -1
      return True
    self.head = (self.head + 1) % self.capacity
    return True

  def Front(self) -> int:
    return -1 if self.isEmpty() else self.queue[self.head]

  def Rear(self) -> int:
    return -1 if self.isEmpty() else self.queue[self.tail]

  def isEmpty(self) -> bool:
    return self.head == -1

  def isFull(self) -> bool:
    return (self.tail + 1) % self.capacity == self.head
