#!/usr/bin/env python3

import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Maze settings
CELL_SIZE = 40
maze_width = SCREEN_WIDTH // CELL_SIZE
maze_height = SCREEN_HEIGHT // CELL_SIZE

# Load images
pacman_image = pygame.image.load('packman.png').convert_alpha()
ghost_image = pygame.image.load('ghost.png').convert_alpha()

# Resize images to fit the cell size
pacman_image = pygame.transform.scale(pacman_image, (CELL_SIZE, CELL_SIZE))
ghost_image = pygame.transform.scale(ghost_image, (CELL_SIZE, CELL_SIZE))

# Pacman settings
pacman_col, pacman_row = 1, 1
pacman_direction = 'right'  # Initial direction

# Ghost settings
ghost_col, ghost_row = maze_width - 2, maze_height - 2
ghost_direction = random.choice(["up", "down", "left", "right"])

# Movement delay
pacman_move_delay = 100
ghost_move_delay = 150
last_pacman_move = pygame.time.get_ticks()
last_ghost_move = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.SysFont(None, 36)


def draw_maze(maze):
    """Draw the maze walls and dots."""
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            x = col_index * CELL_SIZE
            y = row_index * CELL_SIZE
            if cell == "#":
                pygame.draw.rect(screen, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE))
            elif cell == ".":
                pygame.draw.circle(screen, (255, 255, 255), (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 5)


def draw_pacman(col, row, direction):
    """Draw Pacman centered in its cell."""
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    # Reverse flipping logic
    if direction == 'right':
        image = pygame.transform.flip(pacman_image, True, False)
    else:
        image = pacman_image  # Default facing left

    screen.blit(image, (x, y))


def draw_ghost(col, row, direction):
    """Draw Ghost centered in its cell."""
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    # Reverse flipping logic for the ghost
    if direction == 'right':
        image = pygame.transform.flip(ghost_image, True, False)
    else:
        image = ghost_image  # Default facing left

    screen.blit(image, (x, y))


def can_move_to(maze, col, row):
    """Check if a cell is walkable."""
    if 0 <= col < maze_width and 0 <= row < maze_height:
        return maze[row][col] != "#"
    return False


def move_ghost_smart(maze, ghost_col, ghost_row, pacman_col, pacman_row):
    """Move the ghost intelligently toward Pacman."""
    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    # Calculate Manhattan distance to Pacman
    def manhattan_distance(col, row):
        return abs(col - pacman_col) + abs(row - pacman_row)

    # Evaluate possible moves
    best_moves = []
    min_distance = float('inf')

    for direction, (dc, dr) in directions.items():
        new_col = ghost_col + dc
        new_row = ghost_row + dr

        if can_move_to(maze, new_col, new_row):
            distance = manhattan_distance(new_col, new_row)
            if distance < min_distance:
                min_distance = distance
                best_moves = [(new_col, new_row, direction)]
            elif distance == min_distance:
                best_moves.append((new_col, new_row, direction))

    # Randomly choose among the best moves
    if best_moves:
        new_col, new_row, new_direction = random.choice(best_moves)
        return new_col, new_row, new_direction

    # If no valid moves, stay in place
    return ghost_col, ghost_row, ghost_direction


def display_score(current_score):
    """Display the player's score."""
    score_text = font.render(f"Score: {current_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def generate_random_maze(width, height):
    """Generate a random maze using Recursive Backtracking."""
    maze = [["#"] * width for _ in range(height)]
    stack = [(1, 1)]

    # Directions for moving (left, right, up, down)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    # Mark the starting cell as open
    maze[1][1] = "."

    while stack:
        current = stack[-1]
        col, row = current
        random.shuffle(directions)
        found_next = False

        for dc, dr in directions:
            new_col, new_row = col + dc, row + dr
            if 1 <= new_col < width - 1 and 1 <= new_row < height - 1:
                if maze[new_row][new_col] == "#":
                    # Break the wall
                    maze[row + dr // 2][col + dc // 2] = "."
                    # Mark the new cell as open
                    maze[new_row][new_col] = "."
                    # Add the new cell to the stack
                    stack.append((new_col, new_row))
                    found_next = True
                    break

        if not found_next:
            stack.pop()

    # Ensure the starting and ending cells are open
    maze[1][1] = "."
    maze[height - 2][width - 2] = "."

    return maze


# Generate a random maze
maze = generate_random_maze(maze_width, maze_height)


# Main game loop
def main():
    global pacman_col, pacman_row
    global ghost_col, ghost_row, ghost_direction
    global last_pacman_move, last_ghost_move, score
    global pacman_direction

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()

        # Pacman movement
        keys = pygame.key.get_pressed()
        if current_time - last_pacman_move > pacman_move_delay:
            moved = False
            if keys[pygame.K_UP] and can_move_to(maze, pacman_col, pacman_row - 1):
                pacman_row -= 1
                pacman_direction = 'up'
                moved = True
            elif keys[pygame.K_DOWN] and can_move_to(maze, pacman_col, pacman_row + 1):
                pacman_row += 1
                pacman_direction = 'down'
                moved = True
            elif keys[pygame.K_LEFT] and can_move_to(maze, pacman_col - 1, pacman_row):
                pacman_col -= 1
                pacman_direction = 'left'
                moved = True
            elif keys[pygame.K_RIGHT] and can_move_to(maze, pacman_col + 1, pacman_row):
                pacman_col += 1
                pacman_direction = 'right'
                moved = True
            if moved:
                last_pacman_move = current_time

        # Ghost movement
        if current_time - last_ghost_move > ghost_move_delay:
            ghost_col, ghost_row, ghost_direction = move_ghost_smart(maze, ghost_col, ghost_row, pacman_col, pacman_row)
            last_ghost_move = current_time

        # Check collisions
        if maze[pacman_row][pacman_col] == ".":
            maze[pacman_row][pacman_col] = " "  # Replace dot with space
            score += 10

        if pacman_col == ghost_col and pacman_row == ghost_row:
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Render
        screen.fill((0, 0, 0))
        draw_maze(maze)
        draw_pacman(pacman_col, pacman_row, pacman_direction)
        draw_ghost(ghost_col, ghost_row, ghost_direction)
        display_score(score)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
