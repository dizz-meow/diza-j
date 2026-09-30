from collections import deque


def openLock(deadends, target):
  dead = set(deadends)
  if "0000" in dead:
    return -1
  q = deque([("0000", 0)])
  visited = set(["0000"])

  def get_children(lock):
    res = []
    for i in range(4):
      digit = int(lock[i])
      for move in ((digit + 1) % 10, (digit - 1) % 10):
        res.append(lock[:i] + str(move) + lock[i + 1 :])
    return res

  while q:
    lock, turns = q.popleft()
    if lock == target:
      return turns
    for child in get_children(lock):
      if child not in visited and child not in dead:
        visited.add(child)
        q.append((child, turns + 1))
  return -1
