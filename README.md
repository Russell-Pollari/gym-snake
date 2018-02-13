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
down = 0  
up = 1  
left = 2  
right = 3


## TODO

- prevent snake from doing 180deg turns onto itself
- if no action, snake should continue in current direction
- create better render method
- allow for easy human play from keyboard
- add multiple snakes
