# Missionaries and Cannibals Game

## Overview

The Missionaries and Cannibals game is a classic river-crossing puzzle. The objective is to move all the missionaries and cannibals from the right side of the river to the left side using a boat. The boat can hold up to two people at a time, and there are specific rules to follow to avoid losing the game.

## Game Rules

1. You can move 1 or 2 individuals (missionaries or cannibals) in the boat at a time.
2. You lose the game if, at any point, the number of cannibals on either side exceeds the number of missionaries on that side (unless there are no missionaries on that side).
3. You win the game when all the missionaries and cannibals are on the left side of the river.

## Game Instructions

1. The game starts with all 3 missionaries and 3 cannibals on the right side of the river.
2. The boat is initially on the right side.
3. The player inputs the number of missionaries and cannibals to move in the boat.
4. The boat then moves to the opposite side.
5. The game continues until the player wins by moving all individuals to the left side or loses by breaking the rules.

## How to Play

1. Run the game script.
2. Follow the prompts to input the number of missionaries and cannibals to move.
3. The game will update and display the current state of both sides of the river after each move.
4. The game will notify you if a move is invalid, if you lose, or if you win.

## Example

```
Missionaries= 0 Cannibals= 0 |-----B| Missionaries= 3 Cannibals= 3
No of Missionaries or Enter 10 to quit : 1
No.of Cannibals : 1
Missionaries= 1 Cannibals= 1 |B-----| Missionaries= 2 Cannibals= 2
No of Missionaries or Enter 10 to quit : 2
Invalid Move
No of Missionaries or Enter 10 to quit : 0
No.of Cannibals : 1
Missionaries= 1 Cannibals= 0 |-----B| Missionaries= 2 Cannibals= 3
You Lose
```

## Additional Notes

- Make sure the input values are within valid ranges as per the game rules.
- The game continues until either all individuals are moved to the left side or an invalid move is made resulting in loss.
- The player can choose to quit the game by entering `10` when prompted for the number of missionaries.
