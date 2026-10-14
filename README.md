
# Snake and Ladder Using BFS

## Aim
To implement the Snake and Ladder game using the Breadth-First Search (BFS) algorithm.

## Description
This project finds the minimum number of dice throws required to reach the final position in a Snake and Ladder game.

The board is represented as a graph. Each position is a node, and possible dice throws represent edges. Snakes move the player down, while ladders move the player up.

BFS explores positions level by level to find the minimum number of moves.

## Algorithm Used
Breadth-First Search (BFS)

## Data Structure Used
- Queue
- Set for visited positions

## Technologies Used
- Python 3

## How to Run
1. Install Python 3.
2. Save the code as main.py.
3. Run the command:

   python main.py

## Sample Output
Snake and Ladder Game
Board Size: 30
Minimum Dice Throws: 3

## Time Complexity
O(N), where N is the number of board positions.

## Conclusion
This project demonstrates how BFS can find the minimum number of dice throws needed to reach the destination in a Snake and Ladder game.
