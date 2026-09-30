from collections import deque


def orangesRotting(grid):
  q, fresh, time = deque(), 0, 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 2:
        q.append((r, c))
      elif grid[r][c] == 1:
        fresh += 1

  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  while q and fresh > 0:
    for _ in range(len(q)):
      r, c = q.popleft()
      for dr, dc in directions:
        row, col = r + dr, c + dc
        if (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and grid[row][col] == 1
        ):
          grid[row][col] = 2
          q.append((row, col))
          fresh -= 1
    time += 1
  return time if fresh == 0 else -1
