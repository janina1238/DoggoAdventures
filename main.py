import gym
import gym_doggo

env = gym.make('DoggoAdventure-v0')

for t in range(25000):
    env.render()