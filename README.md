# ChessGame (In Progress)
The goal of this project is to create a Chess Engine (running on top of the python-chess package) which can play at a human-like level

The specific implementation of the chess engine has yet to be decided

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
The console will prompt you for a move, which should be entered in the UCI format, ex. a2a4, or b2c4 (In case of pawn promotion, type the lowercase letter of the piece you which to promote to after the move (i.e. a7a8q for queen)

## Implementation

The specific implementation has yet to be chosen, but will probably by a minimax algorithm with alpha-beta pruning

## Author
 
Elijah Tamarchenko
 
## License
 
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) fiel for details
 
## Acknowledgments
