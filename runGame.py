import chess
from chessGame import chessGame
from human import human
#from ai import ai

import sys

human_player = human()
# Temporary
ai_player = human()

game = chessGame(human_player.white, human_player, ai_player)
game.runGame()
