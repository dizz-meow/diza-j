from collections import deque


def numSquares(n):
  q = deque([n])
  visited = set([n])
  squares = [i * i for i in range(1, int(n**0.5) + 1)]
  level = 0
  while q:
    level += 1
    for _ in range(len(q)):
      curr = q.popleft()
      for s in squares:
        remainder = curr - s
        if remainder == 0:
          return level
        if remainder > 0 and remainder not in visited:
          visited.add(remainder)
          q.append(remainder)
  return level
