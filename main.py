
from collections import deque

def snake_and_ladder():
    board_size = 30

    # Snakes: key = head, value = tail
    snakes = {
        27: 5,
        21: 9,
        17: 4
    }

    # Ladders: key = bottom, value = top
    ladders = {
        3: 22,
        8: 26,
        20: 29
    }

    queue = deque([(1, 0)])
    visited = {1}

    while queue:
        position, moves = queue.popleft()

        if position == board_size:
            print("Snake and Ladder Game")
            print("Board Size:", board_size)
            print("Minimum Dice Throws:", moves)
            return

        for dice in range(1, 7):
            next_position = position + dice

            if next_position > board_size:
                continue

            if next_position in snakes:
                next_position = snakes[next_position]
            elif next_position in ladders:
                next_position = ladders[next_position]

            if next_position not in visited:
                visited.add(next_position)
                queue.append((next_position, moves + 1))

    print("Destination cannot be reached.")

snake_and_ladder()
