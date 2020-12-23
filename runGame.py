import chess
from chessGame import chessGame
from human import human
from ai2 import ai2

import sys

human_player = human()
# Temporary
ai_player = ai2()

game = chessGame(human_player.white, human_player, ai_player)
game.runGame()
