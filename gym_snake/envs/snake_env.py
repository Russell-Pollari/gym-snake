import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

class SnakeEnv(gym.Env):
    metadata = { 'render.modes': ['human'] }

    def __init__(self, board_shape=(10, 10)):
        self.board_shape = board_shape
        self.board = np.zeros(board_shape)
        self.info = {}
        self._reset()

    def _reset(self):
        self.snake = [[0, 2], [0, 1], [0, 0]]
        self.reward = 0
        self.done = False
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
        self.board = np.zeros(self.board_shape)
        (fruit_x, fruit_y) = self.fruit_pos
        self.board[fruit_x, fruit_y] = 2
        for x, y in self.snake:
            self.board[x, y] = 1

    def _step(self, action):
        [x, y] = self.snake[0]

        if action == 0:
            x += 1
        elif action == 1:
            x -= 1
        elif action == 2:
            y += 1
        elif action == 3:
            y -= 1

        # if snake hits wall
        if x >= self.board_shape[0] or x < 0 or y >= self.board_shape[1] or y < 0:
            self.done = True

        # if snake hits self
        if self.board[x, y] == 1:
            self.done = True

        # if snake eats fruit
        if self.board[x, y] == 2:
            self.reward += 1
            self._place_fruit()
        else:
            self.snake.pop()

        new_head = [x, y];
        self.snake.insert(0, new_head)
        self._update_snake_position()

        return self.board, self.reward, self.done, self.info

    def _render(self, mode='human', close=False):
        print(self.board)
