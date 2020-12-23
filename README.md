# ChessGame (In Progress)
The goal of this project is to create a Chess Engine (running on top of the python-chess package) which can play at a human-like level.

The engine currently works through the use of the minimax algorithm with alpha-beta pruning and limited quiescent searching.

## Requirements

You need to install the python-chess library in order to use this program:
 ```
 pip3 install python-chess
 ```
## Usage

To run this program, call the following command:
```
python runGame.py
```
The console will prompt you for a move, which should be entered in the UCI format, ex. a2a4, or b2c4 (In case of pawn promotion, type the lowercase letter of the piece you wish to promote to after the move (i.e. a7a8q for queen).

## Implementation

This progrm was built using python on top of the python-chess package. The chess engine uses a depth-3 minimax algorithm with alpha-beta pruning, with a max depth of 6 for quiescent searching. Although not currently implemented, there is a plan to expand the engine by adding a transposition table (Using Zobrist hashing), by using iterative deepening, and maybe by adding an opening book for the engien to pull from in the initial stages of the game. 

## Author
 
Elijah Tamarchenko
 
## License
 
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
