# Pacman Maze Game

Welcome to the **Pacman Maze Game**, a Python-based game built using `pygame`! Navigate through a randomly generated maze, collect dots, and avoid the ghost as it chases you intelligently.

---

## Features

- **Random Maze Generation**:
  - Each game starts with a unique maze generated using the Recursive Backtracking algorithm.
- **Smarter Ghost AI**:
  - The ghost uses a greedy pathfinding algorithm to chase Pacman based on Manhattan distance.
- **Interactive Gameplay**:
  - Move Pacman using arrow keys.
  - Collect dots to score points.
  - Avoid the ghost to stay alive.
- **Animated Characters**:
  - Both Pacman and the ghost are represented by animated images.
  - Directional flipping for realistic movements.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `pygame` library

To install `pygame`, run:
```bash
pip install pygame
```

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Briqo-org/pacman.git
   cd pacman
   ```

2. Place the following files in the project directory:
   - `packman.png`: The image for Pacman (default facing left).
   - `ghost.png`: The image for the ghost (default facing left).

3. Run the game:
   ```bash
   python pacman_game.py
   ```

---

## Controls

- **Arrow Keys**: Move Pacman in the maze.

---

## Game Rules

1. **Objective**:
   - Collect all the dots to increase your score.
   - Avoid the ghost.

2. **Game Over**:
   - The game ends if Pacman and the ghost occupy the same cell.

---

## Code Overview

### Files:
- `pacman_game.py`:
  - Contains the main game logic, including:
    - Random maze generation
    - Pacman and ghost movement
    - Collision detection
    - Score tracking

### Key Features:
1. **Random Maze Generation**:
   - Uses Recursive Backtracking to generate fully connected mazes.

2. **Smarter Ghost AI**:
   - Implements a greedy pathfinding algorithm to chase Pacman dynamically.

3. **Graphics and Animation**:
   - Characters are displayed with images (`packman.png` and `ghost.png`) and flipped based on direction.

---

## Future Enhancements

1. **Multiple Ghosts**:
   - Add more ghosts with varying difficulty levels.

2. **Power-Ups**:
   - Include power-ups that allow Pacman to eat ghosts temporarily.

3. **Levels**:
   - Add progressive difficulty with more complex mazes and faster ghosts.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## Acknowledgments

- Inspired by the classic Pacman game.
- Built with ❤️ using Python and `pygame`.

