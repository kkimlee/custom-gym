# -*- coding: utf-8 -*-
import gym
from tradingBot.agent import TradingAgent
import tradingBot.utils as utils

class TradingEnv(gym.Env):
    # 초기화
    def __init__(self):
        super(TradingEnv, self).__init__()
        
        # 플레이어
        self.agent = TradingAgent()
        
        # 데이터
        self.data = utils.get_data('tradingBot/data/data.csv') # 데이터 가져오기
        self.data_length = len(self.data) # 데이터의 길이 계산
        self.state_size = len(self.data.columns)
        
        # 행동
        self.action_size = 3 # 0: HOLD, 1: LONG, 2: SHORT
        self.reward = 0 # 행동에 대한 보상
        
        # 상태
        self.t = 0 # 시간
        self.state = self.data.iloc[self.t] # 상태
        self.done = False # 끝 체크
        
    def step(self):
        # 끝이면 그냥 종료
        if self.done:
            return
        
        # 플레이어 행동
        agent_act = self.agent.act(self.state, self.action_size)
        
        # 다음 시점의 데이터 읽어오기
        self.next_state = self.data.iloc[self.t+1]
        
        # agent의 행동에 대한 보상 계산
        self.reward = self.actResult(agent_act)
        
        # 시각화
        self.render()
        
        # 시점 증가
        self.t += 1
        if self.t == self.data_length-1:
            # 마지막 시점까지 온 경우 
            self.done = True
        
        # 디버깅을 위한 정보
        info = None
        
        # 다음 상태로 변화
        self.state = self.next_state
        
        return self.state, self.reward, self.done, info
    
    # 행동
    def actResult(self, action):
        # HOLD 보상 계산
        if action == 0:
            # 다음 시점에서 가격이 올랐을 경우 - 보상
            # 다음 시점에서 가격이 내렸을 경우 + 보상
            self.reward = self.state['Close'] - self.next_state['Close']
            
            return self.reward
        # LONG 보상 계산
        elif action == 1:
            # 다음 시점에서 가격이 올랐을 경우 + 보상
            # 다음 시점에서 가격이 내렸을 경우 - 보상
            self.reward = self.next_state['Close'] - self.state['Close']
            
            return self.reward
        # SHORT 보상 계산
        elif action == 2:
            # 다음 시점에서 가격이 올랐을 경우 + 보상
            # 다음 시점에서 가격이 내렸을 경우 - 보상
            self.reward = self.state['Close'] - self.next_state['Close']
            
            return self.reward
    
    # 진행 상황 시각화
    def render(self):
        print(self.t+1, 'th result: ', self.reward)
    
    # 초기 상태로 
    def reset(self):
        self.state = None
        self.t = 0
        self.done = False