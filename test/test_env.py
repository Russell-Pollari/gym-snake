import gym
import gym_snake
import pygame
import numpy as np


actions_dict = {
    pygame.K_s     : 0,
    pygame.K_w     : 1,
    pygame.K_d     : 2,
    pygame.K_a     : 3,
    pygame.K_DOWN  : 0,
    pygame.K_UP    : 1,
    pygame.K_RIGHT : 2,
    pygame.K_LEFT  : 3,
}

env = gym.make('snake-v0')
env.reset()
env.render()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in actions_dict:
                env.step(actions_dict[event.key])
                env.render()
