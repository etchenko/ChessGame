import chess
from chessGame import chessGame
from human import human
from ai3 import ai3
from ai2 import ai2

import sys

human_player = ai2()
# Temporary
ai_player = ai3()

game = chessGame(True, human_player, ai_player)
game.runGame()
