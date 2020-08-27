from gym.envs.registration import register

register(
    id='DoggoAdventure-v0',
    entry_point='gym_doggo.envs:DoggoEnv'
)