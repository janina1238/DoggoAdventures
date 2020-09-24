import gym
import gym_doggo

env = gym.make('DoggoAdventure-v0')

for t in range(25000):
    action = env.action_space.sample()

    env.step(action)
    env.render()

env.close()