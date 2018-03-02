# OpenAI gym snake environment

An environment for OpenAI gym emulating the classic Snake game

Observation state is NxN matrix
 0 = empty cell
 1 = snake
 2 = fruit

+1 reward for every fruit eaten

snake grows in length when fruit is eaten

episode is done when snake hits wall or itself

actions:
down  = 0
up    = 1
right = 2
left  = 3


## TODO

- Fix collision detection system
- should actions be [ left, right, continue] ?
- timestep between actions?
- add multiple snakes

