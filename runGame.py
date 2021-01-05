import chess
from chessGame import chessGame
from human import human
from ai3 import ai3
from ai2 import ai2
from aihash import aihash
from totalai import totalai

import sys

human_player = human()
# Temporary
ai_player = ai2(1)

game = chessGame(True, human_player, ai_player)
game.runGame()
