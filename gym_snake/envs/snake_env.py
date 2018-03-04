import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np
import pygame
from enum import Enum

class Direction(Enum):
    START = -1
    DOWN  = 0
    UP    = 1
    RIGHT = 2
    LEFT  = 3

class SnakeEnv(gym.Env):
    metadata = { 'render.modes': ['human'] }

    def __init__(self, board_shape=(10, 10)):
        self.board_shape = board_shape
        self.board = np.zeros(board_shape, dtype=np.int32)
        self.info = {}
        self._reset()

        self.block_size = 50
        self.width = board_shape[0]  * self.block_size
        self.height = board_shape[1] * self.block_size

        pygame.init()
        pygame.display.set_caption('Snake')
        self.window = pygame.display.set_mode((self.width, self.height))

    def _reset(self):
        start_row = int(round(self.board_shape[0] / 2))
        self.snake = [[start_row, 2], [start_row, 1], [start_row, 0]]
        self.reward = 0
        self.done = False
        self.direction = Direction.START
        self._place_fruit()
        self._update_snake_position()
        return self.board

    def _place_fruit(self):
        valid_position = False
        while not valid_position:
            x = np.random.randint(0, self.board_shape[0] - 1)
            y = np.random.randint(0, self.board_shape[1] - 1)
            valid_position = self.board[x, y] != 1
        self.fruit_pos = [x, y]

    def _update_snake_position(self):
        self.board = np.zeros(self.board_shape, dtype=np.int32)
        (fruit_x, fruit_y) = self.fruit_pos
        self.board[fruit_x, fruit_y] = 2
        for x, y in self.snake:
            self.board[x, y] = 1

    def _step(self, action):

        # Convert int to enum
        action = Direction(action)

        # row -> vertical, column -> horizontal, therefore coordinates are [y, x]
        [y, x] = self.snake[0]

        if     (action == Direction.DOWN  and self.direction != Direction.UP)    \
            or (action == Direction.UP    and self.direction != Direction.DOWN)  \
            or (action == Direction.RIGHT and self.direction != Direction.LEFT)  \
            or (action == Direction.LEFT  and self.direction != Direction.RIGHT):
                self.direction = action
        else:
            # Illegal action, should not go here!
            # TODO: Decide how to handle it
            pass

        if self.direction == Direction.DOWN:
            y += 1
        if self.direction == Direction.UP:
            y -= 1
        if self.direction == Direction.LEFT:
            x -= 1
        if self.direction == Direction.RIGHT:
            x += 1

        # if snake hits wall
        if y >= self.board_shape[0] or y < 0 or x >= self.board_shape[1] or x < 0:
            self.done = True

        # if snake hits self
        if self.board[y, x] == 1:
            self.done = True

        # if snake eats fruit
        if self.board[y, x] == 2:
            self.reward += 1
            self._place_fruit()
        else:
            self.snake.pop()

        new_head = [y, x];
        self.snake.insert(0, new_head)
        self._update_snake_position()

        return self.board, self.reward, self.done, self.info

    def _render(self, mode='human', close=False):
        colors = [(0, 0, 0), (255, 255, 0), (255, 0, 0)]
        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]):
                rect = pygame.Rect(x*self.block_size, y*self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.window, colors[self.board[y, x]], rect)
        print(self.board)
        pygame.display.update()
