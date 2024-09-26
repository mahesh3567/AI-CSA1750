from collections import deque
def print_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(map(str, row)))
    print()
def get_blank_position(puzzle):
    for i, row in enumerate(puzzle):
        if 0 in row:
            return i, row.index(0)
def get_possible_moves(blank_pos):
    x, y = blank_pos
    moves = []
    if x > 0: moves.append((-1, 0))  # Move up
    if x < 2: moves.append((1, 0))   # Move down
    if y > 0: moves.append((0, -1))  # Move left
    if y < 2: moves.append((0, 1))   # Move right
    return moves
def make_move(puzzle, blank_pos, move):
    x, y = blank_pos
    dx, dy = move
    new_x, new_y = x + dx, y + dy
    new_puzzle = [row[:] for row in puzzle]
    new_puzzle[x][y], new_puzzle[new_x][new_y] = new_puzzle[new_x][new_y], new_puzzle[x][y]
    return new_puzzle, (new_x, new_y)
def bfs(start, goal):
    queue = deque([(start, [], get_blank_position(start))])
    visited = set()
    while queue:
        current, path, blank_pos = queue.popleft()
        if current == goal:
            return path + [current]
        visited.add(tuple(map(tuple, current)))
        for move in get_possible_moves(blank_pos):
            next_puzzle, new_blank_pos = make_move(current, blank_pos, move)
            if tuple(map(tuple, next_puzzle)) not in visited:
                queue.append((next_puzzle, path + [current], new_blank_pos))
    return []
# Example usage
start_puzzle = [ [ 1, 2, 3 ], 
                 [ 5, 6, 0 ], 
                 [ 7, 8, 4 ] ]
goal_puzzle = [ [ 1, 2, 3 ], 
                [ 5, 8, 6 ], 
                [ 0, 7, 4 ] ]
solution = bfs(start_puzzle, goal_puzzle)
for step in solution:
    print_puzzle(step)