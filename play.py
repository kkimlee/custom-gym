from env import TradingEnv
from agent import Agent

def play(max_episode=10):
    env = TradingEnv()
    
env = TradingEnv()
trader = Agent()

n_steps = 3000
for step in range(n_steps):
    print("Step {}".format(step + 1))
    trader.get_state(env.state)
    act = trader.act()
    print(trader.state['Close'])
    obs, reward, done, info = env.step(act)
    
    # print('obs= ', obs, 'reward= ', reward)
    # env.render()
    if done:
        print('end')
        break

