import gym
from gym_doggo.envs.doggo_pygame import DoggoPygame

class DoggoEnv(gym.Env):

    def __init__(self):
        self.doggogame = DoggoPygame()

    def render(self, mode='human'):
        self.doggogame.view()