# Sprint Challenge Python 1

# CRITICAL INFORMATION
Due to a bug in pygame, *Mac users* _MUST_ install pygame globally and run this program
outside of the virtual environment:

DO NOT DO `pipenv install` or `pipenv shell`

Instead:
Install pygame globally with `pip3 install pygame`
Run the game with `python3 src/draw.py`

*PC Users*:  A pipfile is not included with this project.  Please create a virtual environment with pipenv, install pygame, and proceed as usual.  

# Overview

https://en.wikipedia.org/wiki/Breakout_(video_game)

Breakout is a classic game that was released by Atari in 1976.  It spawned dozens of
similar clones, including Brickout and Arkanoid.  Versions are also found as Easter Eggs in many games, including the Sonic the Hedgehog series.

Breakout is a single player game similar to pong.  The player controls a rectangular paddle located on the bottom of the screen, and uses it to bounce a moving ball and keep it in play.  This paddle may only move left and right and the player loses if the ball passes the paddle and hits the bottom of the screen.  

Opposite the paddle are a series of blocks.  These blocks break, or vanish, when the ball comes in contact with them.  Normally, the player gains points for breaking blocks and wins when there are no more blocks present.

Commonly, there are many levels with different types and patterns of blocks.

# Specification

Create a clone of Breakout with the following features:

1.  A paddle at the bottom of the screen that is controlled by the player.
2.  An array of blocks at the top of the screen, of the types and properties listed below
3.  A ball that bounces around the play area, bounces off blocks, and the paddle
4.  A play area/screen that is 400 pixels wide and 800 pixels tall
5.  A consequence if the ball hits the bottom of the screen (exiting the program is fine)
6.  A reward if the ball hits the top of the screen (exiting the program is fine)

You must implement the following types of blocks.  Use different colors to distinguish types of block:
1.  A block that the ball bounces off of, that vanishes after the ball touches it
2.  A block that requires multiple hits before it vanishes, changing color with each hit.

# Tips
Use GameBall for your game.

The different types of blocks, and the paddle, can be made by creating classes that inherit from KineticBlock and override the functions in Block.

#Stretch Goals
1.  Add a block that cannot be destroyed.  Exclude this from calculations to determine if the game should end.
2.  A block that the ball _does not_ bounce off of, that vanishes when the ball touches it.  (This may require modifications to the ball)
3.  Add scoring
4.  Add multiple lives
5.  Add multiple levels
6.  Add additional features, such as varieties of blocks, powerups such as multiball, and anything else you can think of!

