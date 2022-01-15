from tradingBot.env import TradingEnv
    
env = TradingEnv()

n_steps = 3000
for step in range(n_steps):
    # 게임 진행
    obs, reward, done, info = env.step()
    
    if done:
        print('end')
        break

