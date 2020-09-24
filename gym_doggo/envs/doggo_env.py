import gym
from gym import spaces
from gym_doggo.envs.doggo_pygame import DoggoPygame


class DoggoEnv(gym.Env):

    def __init__(self):
        self.doggogame = DoggoPygame()
        self.action_space = spaces.Discrete(6)

    def step(self, action):
        self.doggogame.action(action)

    def render(self, mode='human'):
        self.doggogame.view()
