# Tic-Tac-Toe AI

A terminal Tic-Tac-Toe game where you play against an unbeatable computer opponent powered by the Minimax algorithm.

## Features
- Board stored as a list of 9 cells
- Legal move generation and input validation
- Win and draw detection using the 8 winning lines
- Minimax AI that plays optimally
- Live result display: win, loss or draw
- Choose who goes first, and play again without restarting

## Run
    python tic_tac_toe.py

## How the AI works
1. `legal_moves()` lists every empty cell
2. `minimax()` tries every possible continuation, assuming both sides play their best
3. A win for the AI scores +10, a loss -10, a draw 0 (adjusted by depth, so it prefers quicker wins)
4. `best_move()` picks the move with the highest score

## Limitations and future improvements
- The AI is perfect, so the best a human can do is draw
- Could add alpha-beta pruning, difficulty levels, or a GUI