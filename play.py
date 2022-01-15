from tradingBot.env import TradingEnv
    
env = TradingEnv()
agent = env.agent

n_steps = 3000
for step in range(n_steps):
    print("Step {}".format(step + 1))
    agent.get_state(env.state)
    act = agent.act()
    print(agent.state['Close'])
    obs, reward, done, info = env.step(act)
    
    # print('obs= ', obs, 'reward= ', reward)
    # env.render()
    if done:
        print('end')
        break

